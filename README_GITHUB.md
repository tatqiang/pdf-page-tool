# 📄 PDF Page Number Tool

A free web-based tool to add page numbers to PDF files and fix Table of Contents automatically.

## 🌟 Features

- **Replace [[tag]] placeholders** - Automatically converts `[[p-x]]`, `[[pg-xofy]]` to actual page numbers
- **Fix Table of Contents** - Updates TOC page references using PDF link analysis
- **Add page numbers** - Optionally add page numbers to pages without placeholders
- **36 format combinations** - 6 formats × 6 positions
- **Web-based** - No software installation required
- **100% free** - Forever!

## 🚀 Live Demo

Visit: **[Your URL will be here after deployment]**

## 📝 Supported Tag Formats

```
[[p-x]]       → 5
[[p-x/y]]     → 5 / 28  
[[p-xofy]]    → 5 of 28
[[pg-x]]      → Page 5
[[pg-x/y]]    → Page 5/28
[[pg-xofy]]   → Page 5 of 28
```

## 🎯 How to Use

1. **Upload your PDF** - Drag and drop or click to upload
2. **Select options** - Choose format, position, size, and distance
3. **Process** - Click "Process PDF" button
4. **Download** - Get your processed PDF with page numbers!

## 💻 Local Development

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/pdf-page-tool.git
cd pdf-page-tool

# Install dependencies
pip install -r requirements.txt

# Run the application
python web_app.py

# Open browser to http://localhost:5000
```

## 📦 Deployment

This app is deployed on Render.com for free!

See `RENDER_DEPLOYMENT.txt` for detailed deployment instructions.

## 🛠️ Technology Stack

- **Backend**: Python 3.11, Flask
- **PDF Processing**: PyMuPDF (fitz)
- **Frontend**: HTML, CSS, JavaScript
- **Hosting**: Render.com (free tier)

## 📋 Requirements

- Python 3.11+
- Flask 3.1.2
- PyMuPDF 1.24.13
- Gunicorn 23.0.0

## 📄 License

Free to use for personal and commercial projects.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

Made with ❤️ for easy PDF page numbering
