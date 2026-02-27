# Markdown 转 Word 文档工具使用说明

## 1. Python 环境准备

### 1.1 安装 Python
确保已安装 Python 3.8 或更高版本。可以通过以下命令检查：
```bash
python --version
```

如果未安装，请从 [Python官网](https://www.python.org/downloads/) 下载并安装。

### 1.2 创建虚拟环境（推荐）
在项目根目录下创建虚拟环境：
```bash
python -m venv venv
```

### 1.3 激活虚拟环境

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

## 2. 安装依赖

### 2.1 安装项目依赖
在项目根目录下运行：
```bash
pip install -r requirements.txt
```

### 2.2 依赖说明
- `python-docx`: 用于创建和操作 Word 文档
- `beautifulsoup4`: 用于解析 HTML 内容
- `markdown`: 用于将 Markdown 转换为 HTML

## 3. 使用脚本

### 3.1 使用批处理文件（推荐）
双击运行 `MarkdownToWord.bat` 文件，或在命令行中执行：

```bash
MarkdownToWord.bat "文件夹路径" "输出文件路径"
```

示例：
```bash
MarkdownToWord.bat "C:\Users\leon\Downloads\docs\foundry\DI\Applications\Code Repositories" "C:\Users\leon\Downloads\docs\foundry\DI\Applications\Code Repositories.docx"
```

批处理文件会自动检查Python环境，并提供友好的中文提示。

### 3.2 命令行参数运行
脚本支持命令行参数，可以直接指定输入文件夹和输出文件路径：

```bash
python convert_md_to_word.py "文件夹路径" "输出文件路径"
```

示例：
```bash
python convert_md_to_word.py "C:\Users\leon\Downloads\docs\foundry\DI\etl\Applications\Data Lineage" "C:\Users\leon\Downloads\docs\foundry\DI\etl\Applications\Data Lineage.docx"
```

### 3.3 在代码中调用
也可以在其他 Python 脚本中导入并使用：

```python
from convert_md_to_word import convert_markdown_to_word

docs_path = r'你的文档目录路径'
output_path = r'输出Word文档路径'

convert_markdown_to_word(docs_path, output_path)
```

## 4. 功能说明

### 4.1 支持的 Markdown 元素
- 标题 (h1-h6)
- 段落
- 图片（支持相对路径和绝对路径）
- 无序列表
- 有序列表
- 代码块
- 引用块
- 表格

### 4.2 文档结构
- 根据文件夹层级自动生成标题层级
- 文件名会自动转换为标题（将 `-` 和 `_` 替换为空格，并首字母大写）
- 图片会居中显示，宽度为 6 英寸

### 4.3 图片路径解析
脚本会按以下顺序查找图片：
1. 绝对路径
2. 相对于 Markdown 文件的路径
3. 相对于文档根目录的路径

## 5. 常见问题

### 5.1 找不到图片
确保图片路径正确，或者将图片放在与 Markdown 文件相同的目录下。

### 5.2 编码问题
脚本默认使用 UTF-8 编码读取 Markdown 文件，确保文件编码正确。

### 5.3 Word 文档打开失败
确保已安装 Microsoft Word 或兼容 WPS Office 等软件。
