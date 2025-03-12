# 基于深度学习的图像隐写分析系统

这是一个基于深度学习的图像隐写分析系统，用于检测图像中是否包含隐写信息。系统使用Django作为后端框架，结合PyTorch实现深度学习模型，并提供了一个美观的用户界面。

## 功能特点

- 图像上传和预览
- 基于深度学习的隐写分析
- 分析结果可视化
- 历史记录管理
- 用户友好的界面

## 技术栈

- 后端：Django 5.0+
- 深度学习：PyTorch 2.0+
- 图像处理：Pillow, OpenCV
- 前端：Bootstrap 5, jQuery
- 数据库：MySQL

## 安装说明

1. 克隆项目到本地：
```bash
git clone [项目地址]
cd [项目目录]
```

2. 创建并激活虚拟环境（推荐）：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 初始化数据库：
```bash
python manage.py makemigrations
python manage.py migrate
```

5. 创建超级用户：
```bash
python manage.py createsuperuser
```

6. 运行开发服务器：
```bash
python manage.py runserver
```

7. 访问系统：
打开浏览器访问 http://127.0.0.1:8000

## 使用说明

1. 登录系统
2. 在首页上传需要分析的图片
3. 系统会自动进行隐写分析
4. 查看分析结果和历史记录

## 项目结构

```
steganalysis/
├── analysis/              # 主应用目录
│   ├── models.py         # 数据模型
│   ├── views.py          # 视图函数
│   ├── urls.py           # URL配置
│   └── templates/        # 模板文件
├── steganalysis/         # 项目配置目录
│   ├── settings.py       # 项目设置
│   └── urls.py           # 主URL配置
├── static/               # 静态文件
├── media/                # 上传文件存储
├── requirements.txt      # 项目依赖
└── README.md            # 项目说明
```

## 开发团队

- [您的姓名]
- [其他团队成员]

## 许可证

本项目采用 MIT 许可证 