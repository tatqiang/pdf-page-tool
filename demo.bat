@echo off
REM Launch the interactive demo for PDF page numbering

echo.
echo ============================================================
echo      PDF Page Number Tool - Interactive Demo
echo ============================================================
echo.
echo This demo helps you choose the right format and position
echo before processing your actual PDF.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/
    pause
    exit /b 1
)

echo Starting demo...
echo.
python "%~dp0demo_page_numbers.py"

echo.
pause
