import os
import json
from pathlib import Path

class DocScanner:
    def __init__(self, docs_path):
        self.docs_path = Path(docs_path)
        self.revisions_file = self.docs_path / '.revisions.json'
        self.revisions = self._load_revisions()

    def _normalize_path(self, path):
        if isinstance(path, Path):
            path = str(path)
        return path.replace('\\', '/')

    def _load_revisions(self):
        if self.revisions_file.exists():
            with open(self.revisions_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _save_revisions(self):
        with open(self.revisions_file, 'w', encoding='utf-8') as f:
            json.dump(self.revisions, f, ensure_ascii=False, indent=2)

    def scan_directory(self, path=None):
        if path is None:
            path = self.docs_path
        else:
            path = Path(path)

        if not path.exists():
            return []

        result = []
        for item in sorted(path.iterdir()):
            if item.name.startswith('.'):
                continue

            if item.is_dir():
                children = self.scan_directory(item)
                if children:
                    result.append({
                        'name': item.name,
                        'type': 'directory',
                        'path': str(item.relative_to(self.docs_path)),
                        'children': children
                    })
            elif item.suffix == '.md':
                result.append({
                    'name': item.stem,
                    'type': 'file',
                    'path': str(item.relative_to(self.docs_path))
                })

        return result

    def get_file_content(self, file_path):
        full_path = self.docs_path / file_path
        if not full_path.exists() or not full_path.is_file():
            return None

        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()

    def save_file_content(self, file_path, content, author):
        full_path = self.docs_path / file_path
        if not full_path.exists():
            return False

        old_content = self.get_file_content(file_path)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self._add_revision(file_path, old_content, content, author)
        return True

    def _add_revision(self, file_path, old_content, new_content, author):
        import datetime

        normalized_path = self._normalize_path(file_path)
        
        if normalized_path not in self.revisions:
            self.revisions[normalized_path] = []

        revision = {
            'timestamp': datetime.datetime.now().isoformat(),
            'author': author,
            'old_content': old_content,
            'new_content': new_content
        }

        self.revisions[normalized_path].append(revision)
        self._save_revisions()

    def get_revisions(self, file_path):
        normalized_path = self._normalize_path(file_path)
        return self.revisions.get(normalized_path, [])

    def get_diff(self, old_content, new_content):
        import difflib
        diff = difflib.unified_diff(
            old_content.splitlines(keepends=True),
            new_content.splitlines(keepends=True),
            lineterm=''
        )
        return ''.join(diff)
