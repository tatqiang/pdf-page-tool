@echo off
REM ============================================
REM Python Installation Checker
REM Helps diagnose Python installation issues
REM ============================================

echo.
echo ============================================================
echo           Python Installation Checker
echo ============================================================
echo.
echo This tool checks if Python is properly installed.
echo.
echo ============================================================
echo.

echo Checking Python installations...
echo.

REM Check 1: Standard python command
echo [1] Testing: python
python --version >nul 2>&1
if not errorlevel 1 (
    echo    [FOUND] python command works
    python --version
    set FOUND_PYTHON=1
) else (
    echo    [NOT FOUND] python command not available
)
echo.

REM Check 2: Python Launcher
echo [2] Testing: py (Windows Python Launcher)
py --version >nul 2>&1
if not errorlevel 1 (
    echo    [FOUND] py launcher works
    py --version
    set FOUND_PY=1
) else (
    echo    [NOT FOUND] py launcher not available
)
echo.

REM Check 3: python3 command
echo [3] Testing: python3
python3 --version >nul 2>&1
if not errorlevel 1 (
    echo    [FOUND] python3 command works
    python3 --version
    set FOUND_PYTHON3=1
) else (
    echo    [NOT FOUND] python3 command not available
)
echo.

REM Check 4: Common installation paths
echo [4] Checking common installation directories...
echo.

if exist "C:\Python312\python.exe" (
    echo    [FOUND] C:\Python312\python.exe
    "C:\Python312\python.exe" --version
    set FOUND_DIR=1
)

if exist "C:\Python311\python.exe" (
    echo    [FOUND] C:\Python311\python.exe
    "C:\Python311\python.exe" --version
    set FOUND_DIR=1
)

if exist "C:\Python310\python.exe" (
    echo    [FOUND] C:\Python310\python.exe
    "C:\Python310\python.exe" --version
    set FOUND_DIR=1
)

if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    echo    [FOUND] %LOCALAPPDATA%\Programs\Python\Python312\python.exe
    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" --version
    set FOUND_DIR=1
)

if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    echo    [FOUND] %LOCALAPPDATA%\Programs\Python\Python311\python.exe
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" --version
    set FOUND_DIR=1
)

if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    echo    [FOUND] %LOCALAPPDATA%\Programs\Python\Python310\python.exe
    "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" --version
    set FOUND_DIR=1
)

if not defined FOUND_DIR (
    echo    [NOT FOUND] No Python installation in common directories
)
echo.

REM Check 5: PATH environment variable
echo [5] Checking PATH environment variable...
echo.
echo    Current PATH contains:
echo %PATH% | findstr /I "python" >nul 2>&1
if not errorlevel 1 (
    echo    [FOUND] Python directory in PATH
    echo %PATH% | findstr /I "python"
) else (
    echo    [NOT FOUND] No Python directory in PATH
    echo.
    echo    This is the most common problem!
    echo    Python is installed but not added to PATH.
)
echo.

REM Summary
echo ============================================================
echo                         SUMMARY
echo ============================================================
echo.

if defined FOUND_PYTHON (
    echo [SUCCESS] Python is installed and accessible via "python" command
    echo           You can use: python pdf_pages.py "file.pdf"
    goto :END_SUCCESS
)

if defined FOUND_PY (
    echo [SUCCESS] Python is installed and accessible via "py" command
    echo           You can use: py pdf_pages.py "file.pdf"
    goto :END_SUCCESS
)

if defined FOUND_PYTHON3 (
    echo [SUCCESS] Python is installed and accessible via "python3" command
    echo           You can use: python3 pdf_pages.py "file.pdf"
    goto :END_SUCCESS
)

if defined FOUND_DIR (
    echo [PARTIAL] Python is installed but NOT in PATH
    echo.
    echo SOLUTION 1: Add Python to PATH
    echo   1. Search for "Environment Variables" in Windows
    echo   2. Click "Environment Variables" button
    echo   3. Under "User variables", select "Path"
    echo   4. Click "Edit"
    echo   5. Click "New"
    echo   6. Add the Python directory (shown above)
    echo   7. Click OK on all dialogs
    echo   8. Close and reopen Command Prompt
    echo.
    echo SOLUTION 2: Use full path
    echo   Run: "C:\Path\To\python.exe" pdf_pages.py "file.pdf"
    echo.
    goto :END_PARTIAL
)

echo [FAILED] Python is NOT installed
echo.
echo SOLUTION: Install Python
echo   1. Download from: https://www.python.org/downloads/
echo   2. Run the installer
echo   3. IMPORTANT: Check "Add Python to PATH" checkbox!
echo   4. Click "Install Now"
echo   5. Restart your computer
echo   6. Run this checker again
echo.
echo Alternative: Install from Microsoft Store
echo   1. Open Microsoft Store
echo   2. Search for "Python"
echo   3. Install Python 3.12 or later
echo.
goto :END_FAILED

:END_SUCCESS
echo.
echo The pdf_pages.bat tool should work correctly.
echo.
goto :END

:END_PARTIAL
echo.
echo The pdf_pages.bat tool will work with some manual setup.
echo.
goto :END

:END_FAILED
echo.
echo The pdf_pages.bat tool will NOT work until Python is installed.
echo.

:END
echo ============================================================
echo.
pause
