"""
PDF Page Number Tool - Web Application
A browser-based version that works without any installation
"""

from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import os
import tempfile
import fitz  # PyMuPDF
from werkzeug.utils import secure_filename
import shutil
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'pdf-page-number-tool-secret-key'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Import our existing functions
from pdf_pages import replace_pages_placeholder, find_toc_page, fix_toc_using_links, add_page_numbers_to_all_pages

@app.route('/')
def index():
    """Main page with file upload form"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and show options"""
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))
    
    if file and file.filename.lower().endswith('.pdf'):
        # Save uploaded file
        filename = secure_filename(file.filename)
        temp_dir = tempfile.mkdtemp()
        input_path = os.path.join(temp_dir, filename)
        file.save(input_path)
        
        # Get PDF info
        try:
            doc = fitz.open(input_path)
            total_pages = len(doc)
            
            # Check for existing placeholders
            placeholders_found = check_for_placeholders(doc)
            
            # Check for TOC
            toc_page = find_toc_page(doc)
            has_toc = toc_page is not None
            
            doc.close()
            
            # Store file info in session (simplified - in production use proper session management)
            session_data = {
                'input_path': input_path,
                'filename': filename,
                'total_pages': total_pages,
                'placeholders_found': placeholders_found,
                'has_toc': has_toc
            }
            
            return render_template('options.html', **session_data)
            
        except Exception as e:
            flash(f'Error processing PDF: {str(e)}')
            return redirect(url_for('index'))
    else:
        flash('Please upload a PDF file')
        return redirect(url_for('index'))

@app.route('/process', methods=['POST'])
def process_pdf():
    """Process the PDF with selected options"""
    try:
        # Get options from form
        input_path = request.form.get('input_path')
        filename = request.form.get('filename')
        
        # Page numbering options
        format_option = request.form.get('format', '0')
        position_option = request.form.get('position', '1')
        distance_option = request.form.get('distance', '3')
        size_option = request.form.get('size', '3')
        
        # Process the PDF
        doc = fitz.open(input_path)
        total_pages = len(doc)
        
        # Step 1: Replace placeholders
        pages_count, pages_with_placeholders = replace_pages_placeholder(doc, total_pages)
        
        # Step 2: Fix TOC
        toc_page_num = find_toc_page(doc)
        toc_count = 0
        if toc_page_num is not None:
            toc_count = fix_toc_using_links(doc, toc_page_num)
            pages_with_placeholders.add(toc_page_num)
        
        # Step 3: Add page numbers if requested
        additional_count = 0
        if format_option != '0':
            config = create_config_from_options(format_option, position_option, distance_option, size_option)
            additional_count = add_page_numbers_to_all_pages(doc, total_pages, config, pages_with_placeholders)
        
        # Save output
        base_name = os.path.splitext(filename)[0]
        output_filename = f"{base_name}_complete.pdf"
        output_path = os.path.join(os.path.dirname(input_path), output_filename)
        
        doc.save(output_path, garbage=4, deflate=True)
        doc.close()
        
        # Prepare download
        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        flash(f'Error processing PDF: {str(e)}')
        return redirect(url_for('index'))

def check_for_placeholders(doc):
    """Check if document contains any [[tag]] placeholders"""
    formats = ["[[pages]]", "[[p-x]]", "[[p-x/y]]", "[[p-xofy]]", 
               "[[pg-x]]", "[[pg-x/y]]", "[[pg-xofy]]",
               "[[pt-x]]", "[[pt-x/y]]", "[[pt-xofy]]"]
    
    found_formats = []
    total_pages = len(doc)
    
    for page_num in range(min(total_pages, 10)):  # Check first 10 pages
        page = doc[page_num]
        for format_pattern in formats:
            if page.search_for(format_pattern):
                if format_pattern not in found_formats:
                    found_formats.append(format_pattern)
    
    return found_formats

def create_config_from_options(format_opt, position_opt, distance_opt, size_opt):
    """Convert web form options to processing config"""
    format_map = {
        '1': lambda p, t: f"{p}",
        '2': lambda p, t: f"{p} / {t}",
        '3': lambda p, t: f"{p} of {t}",
        '4': lambda p, t: f"Page {p}",
        '5': lambda p, t: f"Page {p}/{t}",
        '6': lambda p, t: f"Page {p} of {t}",
    }
    
    position_map = {
        '1': 'bottom-right',
        '2': 'bottom-center', 
        '3': 'bottom-left',
        '4': 'top-left',
        '5': 'top-center',
        '6': 'top-right',
    }
    
    margin_map = {
        '1': {'x': 10, 'y': 10},
        '2': {'x': 20, 'y': 15},
        '3': {'x': 30, 'y': 20},
        '4': {'x': 50, 'y': 30},
        '5': {'x': 70, 'y': 40},
    }
    
    size_map = {
        '1': 7, '2': 8, '3': 10, '4': 12, '5': 14
    }
    
    margins = margin_map.get(distance_opt, margin_map['3'])
    
    return {
        'format': format_map[format_opt],
        'position': position_map[position_opt],
        'margin_x': margins['x'],
        'margin_y': margins['y'],
        'fontsize': size_map.get(size_opt, 10)
    }

if __name__ == '__main__':
    print("=" * 70)
    print("PDF Page Number Tool - Web Application")
    print("=" * 70)
    print()
    print("Starting web server...")
    print("Open your browser and go to: http://localhost:5000")
    print()
    print("Features:")
    print("• Upload PDF files through web browser")
    print("• Select options through web interface")
    print("• Download processed PDF")
    print("• Works on any device with a web browser")
    print("• No software installation required for users")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 70)
    
    app.run(host='0.0.0.0', port=5000, debug=True)