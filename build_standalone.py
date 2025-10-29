"""
PDF Page Number Tool - PyInstaller Build Script
Creates a standalone Windows executable that users can run without Python
"""

import os
import subprocess
import sys
import shutil

def create_standalone_executable():
    """Create a standalone Windows executable using PyInstaller"""
    
    print("=" * 70)
    print("PDF Page Number Tool - Standalone Executable Builder")
    print("=" * 70)
    print()
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller found")
    except ImportError:
        print("⚠ PyInstaller not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        print("✓ PyInstaller installed")
    
    # Create the executable
    print("\n🔨 Building standalone executable...")
    
    # PyInstaller command options
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                    # Single executable file
        "--noconsole",                  # No console window (GUI mode)
        "--name", "PDF_PageNumber_Tool", # Name of the executable
        "--icon", "app.ico",            # Icon (if available)
        "--add-data", "README.txt;.",   # Include documentation
        "--add-data", "QUICK_GUIDE.md;.",
        "--hidden-import", "fitz",      # Ensure PyMuPDF is included
        "--distpath", "dist",           # Output directory
        "pdf_pages.py"                  # Main script
    ]
    
    try:
        # Remove --icon if no icon file exists
        if not os.path.exists("app.ico"):
            cmd.remove("--icon")
            cmd.remove("app.ico")
        
        subprocess.run(cmd, check=True)
        print("✅ Executable created successfully!")
        
        # Create distribution package
        create_distribution_package()
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def create_distribution_package():
    """Create a complete distribution package"""
    print("\n📦 Creating distribution package...")
    
    # Create distribution folder
    dist_folder = "PDF_PageNumber_Tool_Standalone"
    if os.path.exists(dist_folder):
        shutil.rmtree(dist_folder)
    os.makedirs(dist_folder)
    
    # Copy executable
    shutil.copy("dist/PDF_PageNumber_Tool.exe", dist_folder)
    
    # Copy documentation
    docs_to_copy = [
        "README.txt",
        "QUICK_GUIDE.md", 
        "VISUAL_GUIDE.md",
        "DISTANCE_GUIDE.md",
        "VERSION_SUMMARY.txt"
    ]
    
    for doc in docs_to_copy:
        if os.path.exists(doc):
            shutil.copy(doc, dist_folder)
    
    # Create launcher batch file for drag & drop
    create_launcher_batch(dist_folder)
    
    # Create installation guide
    create_install_guide(dist_folder)
    
    print(f"✅ Distribution package created: {dist_folder}/")
    print("\nPackage contents:")
    for item in os.listdir(dist_folder):
        print(f"  • {item}")

def create_launcher_batch(dist_folder):
    """Create a batch file that provides drag & drop functionality"""
    batch_content = '''@echo off
REM ============================================
REM PDF Page Number Tool - Standalone Launcher
REM ============================================

setlocal EnableDelayedExpansion

echo.
echo ============================================================
echo           PDF Page Number Tool - Standalone
echo ============================================================
echo.
echo This standalone version requires NO Python installation!
echo.

REM Check if file was provided
if "%~1"=="" (
    echo Method 1: Drag and drop a PDF file onto this batch file
    echo Method 2: Run from command line with file path
    echo.
    echo Example: PDF_PageNumber_Launcher.bat "C:\\Documents\\report.pdf"
    echo.
    
    REM Prompt for file path
    set /p "pdf_file=Enter PDF file path (or drag file here): "
    
    if "!pdf_file!"=="" (
        echo.
        echo [ERROR] No file provided
        echo.
        pause
        exit /b 1
    )
    
    REM Remove quotes if present
    set "pdf_file=!pdf_file:"=!"
    
    if not exist "!pdf_file!" (
        echo.
        echo [ERROR] File not found: !pdf_file!
        echo.
        pause
        exit /b 1
    )
    
    echo.
    echo Processing: !pdf_file!
    echo.
    "%~dp0PDF_PageNumber_Tool.exe" "!pdf_file!"
    
) else (
    echo Processing: %~1
    echo.
    "%~dp0PDF_PageNumber_Tool.exe" "%~1"
)

echo.
if errorlevel 1 (
    echo ============================================================
    echo [ERROR] Processing failed. Check the error message above.
    echo ============================================================
) else (
    echo ============================================================
    echo [SUCCESS] PDF processed successfully!
    echo Output file created in the same folder.
    echo ============================================================
)
echo.
echo Press any key to exit...
pause >nul
'''
    
    with open(os.path.join(dist_folder, "INSTALL_GUIDE.txt"), "w", encoding="utf-8") as f:
        f.write(batch_content)

def create_install_guide(dist_folder):
    """Create installation and usage guide"""
    guide_content = '''PDF Page Number Tool - Standalone Version
=========================================

✅ NO PYTHON INSTALLATION REQUIRED!

This standalone version includes everything needed to run the PDF page 
numbering tool without installing Python or any dependencies.

📁 PACKAGE CONTENTS
-------------------
• PDF_PageNumber_Tool.exe     - Main executable (standalone)
• PDF_PageNumber_Launcher.bat - Drag & drop launcher
• README.txt                  - Complete user guide
• QUICK_GUIDE.md              - Quick reference
• Additional documentation files

🚀 HOW TO USE
-------------

METHOD 1: Drag & Drop (Easiest)
1. Drag your PDF file onto "PDF_PageNumber_Launcher.bat"
2. Follow the prompts
3. Done!

METHOD 2: Command Line
1. Open Command Prompt in this folder
2. Run: PDF_PageNumber_Tool.exe "your_document.pdf"

METHOD 3: Double-click Launcher
1. Double-click "PDF_PageNumber_Launcher.bat"
2. Enter the path to your PDF file when prompted
3. Follow the prompts

📋 FEATURES
-----------
• Replace {{tag}} placeholders ({{p-x}}, {{pg-xofy}}, etc.)
• Fix Table of Contents page numbers automatically
• Add custom page numbers to blank pages
• 36 format & position combinations
• Safe operation (never modifies original file)

🔧 SYSTEM REQUIREMENTS
----------------------
• Windows 7 or later
• No additional software required
• ~15-20 MB disk space

📚 DOCUMENTATION
----------------
• README.txt - Complete user guide with all options
• QUICK_GUIDE.md - Quick reference for formats and positions

🔄 UPDATES
----------
For updates and latest version, visit:
[Your distribution website/GitHub page]

💡 TIPS
-------
• Always test on a copy of your document first
• Most popular choice: Format 6, Position 1 (Page x of y, Bottom Right)
• Choose Format 0 if you only want to replace {{tags}}
• Press Enter at prompts to use default options

🐛 TROUBLESHOOTING
------------------
If the tool doesn't work:
1. Make sure you're using the launcher batch file
2. Check that your PDF file path doesn't contain special characters
3. Try copying your PDF to a simple folder path like C:\\temp\\
4. Right-click the executable and "Run as administrator" if needed

📞 SUPPORT
----------
• Read README.txt for detailed instructions
• Check QUICK_GUIDE.md for format options
• See VERSION_SUMMARY.txt for feature overview

Version: 3.1 Standalone
Built: ''' + __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M') + '''
'''
    
    with open(os.path.join(dist_folder, "README_STANDALONE.txt"), "w", encoding="utf-8") as f:
        f.write(guide_content)

if __name__ == "__main__":
    if create_standalone_executable():
        print("\n" + "=" * 70)
        print("🎉 SUCCESS! Standalone executable created.")
        print("=" * 70)
        print()
        print("Next steps:")
        print("1. Test the executable in the PDF_PageNumber_Tool_Standalone/ folder")
        print("2. Zip the entire folder for distribution")
        print("3. Users can download, extract, and run without Python!")
        print()
        print("Distribution package: PDF_PageNumber_Tool_Standalone/")
        print("• PDF_PageNumber_Tool.exe - Main executable")
        print("• PDF_PageNumber_Launcher.bat - Drag & drop interface")
        print("• Documentation files")
        print()
        print("Users just need to:")
        print("1. Download and extract the zip file")
        print("2. Drag PDF files onto the launcher batch file")
        print("3. That's it! No Python installation needed.")
    else:
        print("\n❌ Build failed. Check error messages above.")