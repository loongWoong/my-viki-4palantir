from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import markdown
from doc_scanner import DocScanner
import os
import re

app = Flask(__name__)
CORS(app)

DOCS_PATH = os.path.join(os.path.dirname(__file__), 'docs')
scanner = DocScanner(DOCS_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tree')
def get_tree():
    tree = scanner.scan_directory()
    return jsonify(tree)

def process_image_links(content, file_path):
    def replace_image(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        
        if image_path.startswith('http://') or image_path.startswith('https://'):
            return match.group(0)
        
        doc_dir = os.path.dirname(file_path)
        full_image_path = os.path.join(doc_dir, image_path)
        relative_path = os.path.relpath(full_image_path, '').replace('\\', '/')
        
        return f'![{alt_text}](/docs/{relative_path})'
    
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    return re.sub(pattern, replace_image, content)

@app.route('/api/content/<path:file_path>')
def get_content(file_path):
    if not file_path.endswith('.md'):
        file_path += '.md'
    
    content = scanner.get_file_content(file_path)
    if content is None:
        return jsonify({'error': 'File not found'}), 404
    
    processed_content = process_image_links(content, file_path)
    html_content = markdown.markdown(processed_content, extensions=['fenced_code', 'tables'])
    return jsonify({
        'content': content,
        'html': html_content,
        'path': file_path
    })

@app.route('/api/save', methods=['POST'])
def save_content():
    data = request.json
    file_path = data.get('path')
    content = data.get('content')
    author = data.get('author', 'Anonymous')
    
    if not file_path or content is None:
        return jsonify({'error': 'Missing required fields'}), 400
    
    success = scanner.save_file_content(file_path, content, author)
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'error': 'Failed to save file'}), 500

@app.route('/api/revisions/<path:file_path>')
def get_revisions(file_path):
    if not file_path.endswith('.md'):
        file_path += '.md'
    
    revisions = scanner.get_revisions(file_path)
    return jsonify(revisions)

@app.route('/docs/<path:file_path>')
def serve_docs(file_path):
    return send_from_directory(DOCS_PATH, file_path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
