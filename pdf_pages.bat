@echo off
setlocal EnableDelayedExpansion
REM ============================================
REM PDF Page Number Replacement - Easy Launcher
REM ============================================

:START
cls
echo.
echo ============================================================
echo           PDF Page Number Replacement Tool
echo ============================================================
echo.
echo This tool automatically:
echo  1. Replaces page number placeholders with actual numbers
echo  2. Updates Table of Contents page numbers
echo  3. Adds page numbers to pages without placeholders
echo.
echo ============================================================
echo SUPPORTED FORMATS:
echo ============================================================
echo.
echo   Syntax           Display
echo   --------         -----------
echo   {{p-x}}          x
echo   {{p-x/y}}        x / y
echo   {{p-xofy}}       x of y
echo   {{pg-x}}         Page x
echo   {{pg-x/y}}       Page x/y
echo   {{pg-xofy}}      Page x of y
echo.
echo   Note: Thai formats ({{pt-x}}, {{pt-x/y}}, {{pt-xofy}})
echo         are also supported but may not display correctly
echo.
echo ============================================================
echo ADDITIONAL PAGE NUMBERING:
echo ============================================================
echo.
echo   Format Options (0-6):
echo   0 = None   1 = x   2 = x/y   3 = x of y
echo   4 = Page x   5 = Page x/y   6 = Page x of y
echo.
echo   Position Options (1-6):
echo   1 = Bottom Right   2 = Bottom Center   3 = Bottom Left
echo   4 = Top Left       5 = Top Center      6 = Top Right
echo.
echo   Distance Options (1-5):
echo   1 = Very Close   2 = Close   3 = Normal   4 = Far   5 = Very Far
echo.
echo   Text Size Options (1-5):
echo   1 = Very Small (7pt)   2 = Small (8pt)   3 = Normal (10pt)
echo   4 = Large (12pt)       5 = Very Large (14pt)
echo.
echo ============================================================
echo.

REM Check if Python is installed
set "PYTHON_CMD=python"

REM First try standard python command
python --version >nul 2>&1
if not errorlevel 1 goto :PYTHON_FOUND

REM Try py launcher (Windows Python Launcher)
py --version >nul 2>&1
if not errorlevel 1 (
    set "PYTHON_CMD=py"
    goto :PYTHON_FOUND
)

REM Try python3
python3 --version >nul 2>&1
if not errorlevel 1 (
    set "PYTHON_CMD=python3"
    goto :PYTHON_FOUND
)

REM Try common installation paths
if exist "C:\Python312\python.exe" (
    set "PYTHON_CMD=C:\Python312\python.exe"
    goto :PYTHON_FOUND
)
if exist "C:\Python311\python.exe" (
    set "PYTHON_CMD=C:\Python311\python.exe"
    goto :PYTHON_FOUND
)
if exist "C:\Python310\python.exe" (
    set "PYTHON_CMD=C:\Python310\python.exe"
    goto :PYTHON_FOUND
)
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    goto :PYTHON_FOUND
)
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
    goto :PYTHON_FOUND
)
if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    goto :PYTHON_FOUND
)

REM Python not found anywhere
echo ============================================================
echo [ERROR] Python is not installed or not in PATH
echo ============================================================
echo.
echo This tool requires Python to run.
echo.
echo OPTION 1: Install Python (Recommended)
echo   1. Download from: https://www.python.org/downloads/
echo   2. Run the installer
echo   3. IMPORTANT: Check "Add Python to PATH" checkbox!
echo   4. Click "Install Now"
echo.
echo OPTION 2: Python is installed but not in PATH
echo   Run "check_python.bat" for detailed diagnostics
echo   Or manually:
echo   1. Search for "python.exe" on your computer
echo   2. Copy the full path (e.g., C:\Python311\python.exe)
echo   3. Run from command line:
echo      "C:\Path\To\python.exe" "%~dp0pdf_pages.py" "your_file.pdf"
echo.
echo OPTION 3: Use Windows Store Python
echo   1. Open Microsoft Store
echo   2. Search for "Python"
echo   3. Install Python (latest version)
echo   4. Re-run this batch file
echo.
echo ============================================================
pause
exit /b 1

:PYTHON_FOUND
echo [OK] Python found: %PYTHON_CMD%
echo.

REM Get Python version for display
%PYTHON_CMD% --version 2>&1
echo.

REM Check if PyMuPDF is installed
%PYTHON_CMD% -c "import fitz" >nul 2>&1
if errorlevel 1 (
    echo [INSTALLING] PyMuPDF library...
    echo.
    %PYTHON_CMD% -m pip install PyMuPDF
    echo.
    if errorlevel 1 (
        echo [ERROR] Failed to install PyMuPDF
        echo.
        echo Try running this command manually:
        echo   %PYTHON_CMD% -m pip install PyMuPDF
        echo.
        pause
        exit /b 1
    )
    echo [OK] PyMuPDF installed successfully
    echo.
)

REM Check if file was provided
if "%~1"=="" (
    echo ============================================================
    echo                   HOW TO USE
    echo ============================================================
    echo.
    echo Method 1: Drag and drop a PDF file onto this batch file
    echo Method 2: Run from command line with file path
    echo.
    echo Example: replace_pdf_pages.bat "C:\Documents\report.pdf"
    echo.
    echo ============================================================
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
    echo ============================================================
    echo Processing: !pdf_file!
    echo ============================================================
    echo.
    %PYTHON_CMD% "%~dp0pdf_pages.py" "!pdf_file!"
    
) else (
    echo ============================================================
    echo Processing: %~1
    echo ============================================================
    echo.
    %PYTHON_CMD% "%~dp0pdf_pages.py" "%~1"
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
