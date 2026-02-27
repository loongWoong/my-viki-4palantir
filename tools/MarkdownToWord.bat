@echo off
chcp 65001 >nul
echo ========================================
echo Markdown to Word Converter
echo ========================================
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not detected
    echo.
    echo Please install Python 3.6 or higher first
    echo Download: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

if "%~1"=="" (
    echo Usage: MarkdownToWord.bat ^<folder_path^> ^<output_file_path^>
    echo.
    echo Example:
    echo   MarkdownToWord.bat "C:\path\to\markdown\files" "C:\path\to\output.docx"
    echo.
    pause
    exit /b 1
)

if "%~2"=="" (
    echo Error: Missing output file path
    echo.
    echo Usage: MarkdownToWord.bat ^<folder_path^> ^<output_file_path^>
    echo.
    pause
    exit /b 1
)

echo Converting Markdown files to Word document...
echo Input folder: %~1
echo Output file: %~2
echo.

python "%~dp0convert_md_to_word.py" "%~1" "%~2"

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Conversion completed successfully!
    echo ========================================
) else (
    echo.
    echo ========================================
    echo Conversion failed, please check error messages
    echo ========================================
)

echo.
pause