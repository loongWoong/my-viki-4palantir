import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", "sys", "argparse", "pathlib", "markdown", "bs4", "docx"],
    "excludes": ["tkinter", "unittest", "email", "http", "urllib", "xmlrpc"],
    "optimize": 0,
}

base = None
if sys.platform == "win32":
    base = "Console"

executables = [
    Executable(
        script="convert_md_to_word.py",
        base=base,
        target_name="MarkdownToWord.exe",
    )
]

setup(
    name="MarkdownToWord",
    version="1.0",
    description="Convert Markdown files to Word document",
    options={"build_exe": build_exe_options},
    executables=executables,
)