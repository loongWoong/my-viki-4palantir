import os
import re
import sys
import argparse
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import markdown
from bs4 import BeautifulSoup


def get_folder_depth(file_path, base_path):
    relative_path = os.path.relpath(file_path, base_path)
    depth = relative_path.count(os.sep)
    return depth


def get_folder_structure(file_path, base_path):
    relative_path = os.path.relpath(file_path, base_path)
    folders = Path(relative_path).parent.parts
    return folders


def parse_markdown_to_html(md_content):
    return markdown.markdown(md_content, extensions=['tables', 'fenced_code'])


def add_html_to_doc(doc, html_content, base_heading_level=1, md_file_path=None, docs_path=None):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for element in soup.find_all(True):
        if element.name == 'h1':
            level = min(base_heading_level, 9)
            p = doc.add_heading(element.get_text(), level=level)
        elif element.name == 'h2':
            level = min(base_heading_level + 1, max(base_heading_level + 1, 9))
            p = doc.add_heading(element.get_text(), level=level)
        elif element.name == 'h3':
            level = min(base_heading_level + 2, max(base_heading_level + 2, 9))
            p = doc.add_heading(element.get_text(), level=level)
        elif element.name == 'h4':
            level = min(base_heading_level + 3, max(base_heading_level + 3, 9))
            p = doc.add_heading(element.get_text(), level=level)
        elif element.name == 'h5':
            level = min(base_heading_level + 4, max(base_heading_level + 4, 9))
            p = doc.add_heading(element.get_text(), level=level)
        elif element.name == 'h6':
            level = min(base_heading_level + 5, max(base_heading_level + 5, 9))
            p = doc.add_heading(element.get_text(), level=level)
        elif element.name == 'p':
            img = element.find('img')
            if img:
                img_src = img.get('src', '')
                if img_src:
                    img_path = resolve_image_path(img_src, md_file_path, docs_path)
                    if img_path and os.path.exists(img_path):
                        try:
                            p = doc.add_paragraph()
                            run = p.add_run()
                            run.add_picture(img_path, width=Inches(6))
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        except Exception as e:
                            p = doc.add_paragraph(f'[Image: {img_src}]')
                    else:
                        p = doc.add_paragraph(f'[Image not found: {img_src}]')
            else:
                text = element.get_text().strip()
                if text:
                    p = doc.add_paragraph(text)
        elif element.name == 'ul':
            for li in element.find_all('li', recursive=False):
                p = doc.add_paragraph(li.get_text(), style='List Bullet')
        elif element.name == 'ol':
            for li in element.find_all('li', recursive=False):
                p = doc.add_paragraph(li.get_text(), style='List Number')
        elif element.name == 'pre':
            code_text = element.get_text()
            p = doc.add_paragraph(code_text)
            p.style = 'No Spacing'
            for run in p.runs:
                run.font.name = 'Consolas'
                run.font.size = Pt(9)
        elif element.name == 'blockquote':
            p = doc.add_paragraph(element.get_text())
            p.style = 'Intense Quote'
        elif element.name == 'table':
            rows = element.find_all('tr')
            if rows:
                table = doc.add_table(rows=len(rows), cols=len(rows[0].find_all(['th', 'td'])))
                table.style = 'Light Grid Accent 1'
                
                for i, row in enumerate(rows):
                    cells = row.find_all(['th', 'td'])
                    for j, cell in enumerate(cells):
                        table.rows[i].cells[j].text = cell.get_text().strip()
                        if cell.name == 'th':
                            for run in table.rows[i].cells[j].paragraphs[0].runs:
                                run.bold = True


def resolve_image_path(img_src, md_file_path, docs_path):
    md_dir = os.path.dirname(md_file_path)
    
    if os.path.isabs(img_src):
        return img_src
    
    relative_path = os.path.join(md_dir, img_src)
    if os.path.exists(relative_path):
        return relative_path
    
    if docs_path:
        docs_relative_path = os.path.join(docs_path, img_src)
        if os.path.exists(docs_relative_path):
            return docs_relative_path
    
    return None


def convert_markdown_to_word(docs_path, output_path):
    doc = Document()
    doc.add_heading('Documentation', level=0)
    
    md_files = []
    
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                md_files.append(file_path)
    
    md_files.sort(key=lambda x: os.path.getctime(x))
    
    created_folders = set()
    
    for md_file in md_files:
        folder_structure = get_folder_structure(md_file, docs_path)
        depth = len(folder_structure)
        base_heading_level = depth + 1
        
        for i, folder in enumerate(folder_structure):
            folder_path = '/'.join(folder_structure[:i+1])
            if folder_path not in created_folders:
                heading_level = i + 1
                doc.add_heading(folder, level=min(heading_level, 9))
                created_folders.add(folder_path)
        
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        file_name = Path(md_file).stem
        file_name = file_name.replace('-', ' ').replace('_', ' ')
        file_name = ' '.join(word.capitalize() for word in file_name.split())
        
        doc.add_heading(file_name, level=min(base_heading_level, 9))
        
        html_content = parse_markdown_to_html(md_content)
        add_html_to_doc(doc, html_content, base_heading_level=base_heading_level + 1, 
                       md_file_path=md_file, docs_path=docs_path)
        
        doc.add_paragraph()
    
    doc.save(output_path)
    print(f'Word document created successfully: {output_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown files to Word document')
    parser.add_argument('docs_path', help='Path to the folder containing Markdown files')
    parser.add_argument('output_path', help='Path for the output Word document')
    
    args = parser.parse_args()
    
    docs_path = args.docs_path
    output_path = args.output_path
    
    if not os.path.exists(docs_path):
        print(f'Error: The specified folder does not exist: {docs_path}')
        sys.exit(1)
    
    try:
        convert_markdown_to_word(docs_path, output_path)
    except Exception as e:
        print(f'Error: {str(e)}')
        sys.exit(1)
