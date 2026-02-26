class VikiApp {
    constructor() {
        this.currentFile = null;
        this.currentContent = null;
        this.init();
    }

    async init() {
        await this.loadTree();
        this.bindEvents();
    }

    async loadTree() {
        try {
            const response = await fetch('/api/tree');
            const tree = await response.json();
            this.renderTree(tree);
        } catch (error) {
            console.error('Failed to load tree:', error);
            document.getElementById('treeContainer').innerHTML = '<div class="loading">加载失败</div>';
        }
    }

    renderTree(nodes, container = document.getElementById('treeContainer')) {
        container.innerHTML = '';
        
        if (nodes.length === 0) {
            container.innerHTML = '<div class="loading">没有找到文档</div>';
            return;
        }

        nodes.forEach(node => {
            const nodeElement = this.createTreeNode(node);
            container.appendChild(nodeElement);
        });
    }

    createTreeNode(node) {
        const nodeDiv = document.createElement('div');
        nodeDiv.className = 'tree-node';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'tree-node-content';
        contentDiv.dataset.path = node.path;
        contentDiv.dataset.type = node.type;

        if (node.type === 'directory') {
            const toggle = document.createElement('span');
            toggle.className = 'tree-toggle';
            toggle.textContent = '▶';
            contentDiv.appendChild(toggle);

            const icon = document.createElement('span');
            icon.className = 'tree-icon';
            icon.textContent = '📁';
            contentDiv.appendChild(icon);

            const name = document.createElement('span');
            name.textContent = node.name;
            contentDiv.appendChild(name);

            const childrenDiv = document.createElement('div');
            childrenDiv.className = 'tree-children';

            contentDiv.addEventListener('click', () => {
                toggle.classList.toggle('expanded');
                childrenDiv.classList.toggle('expanded');
            });

            nodeDiv.appendChild(contentDiv);
            nodeDiv.appendChild(childrenDiv);

            if (node.children && node.children.length > 0) {
                node.children.forEach(child => {
                    const childElement = this.createTreeNode(child);
                    childrenDiv.appendChild(childElement);
                });
            }
        } else {
            const spacer = document.createElement('span');
            spacer.className = 'tree-toggle';
            spacer.textContent = '';
            contentDiv.appendChild(spacer);

            const icon = document.createElement('span');
            icon.className = 'tree-icon';
            icon.textContent = '📄';
            contentDiv.appendChild(icon);

            const name = document.createElement('span');
            name.textContent = node.name;
            contentDiv.appendChild(name);

            contentDiv.addEventListener('click', () => {
                this.selectFile(node.path, node.name, contentDiv);
            });

            nodeDiv.appendChild(contentDiv);
        }

        return nodeDiv;
    }

    async selectFile(path, name, element) {
        document.querySelectorAll('.tree-node-content').forEach(el => {
            el.classList.remove('active');
        });
        element.classList.add('active');

        this.currentFile = path;
        document.getElementById('documentTitle').textContent = name;
        document.getElementById('editBtn').style.display = 'block';
        document.getElementById('revisionsBtn').style.display = 'block';

        await this.loadContent(path);
        await this.loadRevisions(path);
    }

    async loadContent(path) {
        try {
            const response = await fetch(`/api/content/${path}`);
            const data = await response.json();

            if (data.error) {
                console.error(data.error);
                return;
            }

            this.currentContent = data.content;
            document.getElementById('markdownContent').innerHTML = data.html;
            document.getElementById('markdownEditor').value = data.content;
        } catch (error) {
            console.error('Failed to load content:', error);
        }
    }

    async loadRevisions(path) {
        try {
            const response = await fetch(`/api/revisions/${path}`);
            const revisions = await response.json();
            this.renderRevisions(revisions);
        } catch (error) {
            console.error('Failed to load revisions:', error);
        }
    }

    renderRevisions(revisions) {
        const panel = document.getElementById('revisionsPanel');
        const list = document.getElementById('revisionsList');

        list.innerHTML = '';

        if (revisions.length === 0) {
            const noRevisions = document.createElement('div');
            noRevisions.className = 'no-revisions';
            noRevisions.textContent = '暂无修订记录';
            list.appendChild(noRevisions);
            return;
        }

        revisions.slice().reverse().forEach(revision => {
            const item = document.createElement('div');
            item.className = 'revision-item';

            const header = document.createElement('div');
            header.className = 'revision-header';

            const author = document.createElement('span');
            author.className = 'revision-author';
            author.textContent = `修改人: ${revision.author}`;

            const time = document.createElement('span');
            time.className = 'revision-time';
            time.textContent = new Date(revision.timestamp).toLocaleString('zh-CN');

            header.appendChild(author);
            header.appendChild(time);

            const diff = document.createElement('div');
            diff.className = 'revision-diff';
            diff.textContent = this.getDiff(revision.old_content, revision.new_content);

            item.appendChild(header);
            item.appendChild(diff);
            list.appendChild(item);
        });
    }

    toggleRevisions() {
        const panel = document.getElementById('revisionsPanel');
        const viewMode = document.getElementById('viewMode');
        const revisionsBtn = document.getElementById('revisionsBtn');
        
        if (panel.style.display === 'none' || panel.style.display === '') {
            viewMode.style.display = 'none';
            panel.style.display = 'block';
            revisionsBtn.classList.add('active');
        } else {
            viewMode.style.display = 'block';
            panel.style.display = 'none';
            revisionsBtn.classList.remove('active');
        }
    }

    getDiff(oldContent, newContent) {
        const oldLines = oldContent.split('\n');
        const newLines = newContent.split('\n');
        
        let diff = '';
        let i = 0, j = 0;
        
        while (i < oldLines.length || j < newLines.length) {
            if (i < oldLines.length && j < newLines.length && oldLines[i] === newLines[j]) {
                i++;
                j++;
            } else if (j < newLines.length && (i >= oldLines.length || !oldLines.includes(newLines[j]))) {
                diff += `+ ${newLines[j]}\n`;
                j++;
            } else if (i < oldLines.length && (j >= newLines.length || !newLines.includes(oldLines[i]))) {
                diff += `- ${oldLines[i]}\n`;
                i++;
            } else {
                i++;
                j++;
            }
        }
        
        return diff || '无变化';
    }

    bindEvents() {
        const editBtn = document.getElementById('editBtn');
        const revisionsBtn = document.getElementById('revisionsBtn');
        const saveBtn = document.getElementById('saveBtn');
        const cancelBtn = document.getElementById('cancelBtn');

        editBtn.addEventListener('click', () => this.enterEditMode());
        revisionsBtn.addEventListener('click', () => this.toggleRevisions());
        saveBtn.addEventListener('click', () => this.saveContent());
        cancelBtn.addEventListener('click', () => this.exitEditMode());
    }

    enterEditMode() {
        document.getElementById('viewMode').style.display = 'none';
        document.getElementById('editMode').style.display = 'flex';
        document.getElementById('editBtn').style.display = 'none';
    }

    exitEditMode() {
        const revisionsBtn = document.getElementById('revisionsBtn');
        const revisionsPanel = document.getElementById('revisionsPanel');
        
        if (revisionsBtn.classList.contains('active')) {
            document.getElementById('viewMode').style.display = 'none';
        } else {
            document.getElementById('viewMode').style.display = 'block';
        }
        
        document.getElementById('editMode').style.display = 'none';
        document.getElementById('editBtn').style.display = 'block';
    }

    async saveContent() {
        const author = document.getElementById('authorName').value.trim();
        const content = document.getElementById('markdownEditor').value;

        if (!author) {
            alert('请输入修改人姓名');
            return;
        }

        if (!this.currentFile) {
            alert('请先选择一个文档');
            return;
        }

        try {
            const response = await fetch('/api/save', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    path: this.currentFile,
                    content: content,
                    author: author
                })
            });

            const data = await response.json();

            if (data.success) {
                alert('保存成功！');
                this.currentContent = content;
                await this.loadContent(this.currentFile);
                await this.loadRevisions(this.currentFile);
                this.exitEditMode();
            } else {
                alert('保存失败: ' + (data.error || '未知错误'));
            }
        } catch (error) {
            console.error('Failed to save content:', error);
            alert('保存失败: 网络错误');
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new VikiApp();
});
