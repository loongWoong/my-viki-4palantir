import json
import os

revisions_file = os.path.join(os.path.dirname(__file__), 'docs', '.revisions.json')

if os.path.exists(revisions_file):
    with open(revisions_file, 'r', encoding='utf-8') as f:
        revisions = json.load(f)
    
    new_revisions = {}
    for key, value in revisions.items():
        new_key = key.replace('\\', '/')
        new_revisions[new_key] = value
    
    with open(revisions_file, 'w', encoding='utf-8') as f:
        json.dump(new_revisions, f, ensure_ascii=False, indent=2)
    
    print("修订记录文件路径已修复！")
else:
    print("修订记录文件不存在")
