from setuptools import setup

setup(
    name="MarkdownToWord",
    version="1.0",
    description="Convert Markdown files to Word document",
    console=["convert_md_to_word.py"],
    options={
        "py2exe": {
            "packages": ["os", "sys", "argparse", "pathlib", "markdown", "bs4", "docx"],
            "excludes": ["tkinter", "unittest", "email", "http", "urllib", "xmlrpc"],
        }
    },
)