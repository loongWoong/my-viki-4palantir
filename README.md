# My Viki - 文档百科系统

一个类似viki百科的palantir文档展示系统，支持左侧目录树和右侧Markdown展示，以及众包修改功能。

## 功能特性

- 左侧目录树展示文档层级结构
- 右侧Markdown文档渲染和展示
- 众包修改功能，任何人都可以修改文档
- 修订记录追踪，记录修改人和修改内容

## 安装和运行

1. 创建虚拟环境：
```bash
python -m venv venv
#Windows激活
venv\Scripts\activate
#Linux激活
source venv/bin/activate
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python app.py
```

4. 访问 http://localhost:5000

## 项目结构

```
my-viki/
├── docs/              # 文档目录
├── static/            # 静态文件
│   ├── css/
│   └── js/
├── templates/         # HTML模板
├── app.py            # Flask应用
├── requirements.txt  # 依赖列表
└── README.md         # 项目说明
```
