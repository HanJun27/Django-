# Django音乐平台（项目文件位于src文件夹中）

一个基于Django框架开发的完整在线音乐播放系统，提供音乐播放、用户管理、评论互动、搜索推荐等完整功能。

## 🎵 功能特性

- 🎶 **在线音乐播放** - 支持MP3格式音频播放
- 👥 **用户管理系统** - 注册、登录、个人中心
- 💬 **互动评论系统** - 歌曲评论和社交互动
- 🔍 **智能搜索** - 按歌曲名、歌手名搜索
- 📊 **音乐排行榜** - 热门搜索、播放、下载排行
- 📱 **响应式设计** - 支持PC和移动端访问
- 🎨 **美观界面** - 现代化的音乐主题设计

## 🚀 快速开始

### 环境要求

- Python 3.7+
- Django 2.2.5+
- MySQL 5.7+ 或 SQLite3

### 安装步骤

1. **克隆项目**
```bash
git clone <项目地址>
cd text/src
```

2. **创建虚拟环境**
```bash
python -m venv .venv

# Windows 激活
.venv\Scripts\activate

# Linux/Mac 激活
source .venv/bin/activate
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **数据库配置**

**选项A: 使用SQLite (推荐开发)**
```python
# settings.py 中配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

**选项B: 使用MySQL**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

5. **数据库初始化**
```bash
# 创建数据库表
python manage.py makemigrations
python manage.py migrate

# 创建管理员账号
python manage.py createsuperuser
```

6. **导入音乐数据**
```bash
# 自动导入本地音乐文件
python create_music_data.py
```

7. **启动服务**
```bash
python manage.py runserver
```

访问 http://127.0.0.1:8000 开始使用！

## 📁 项目结构

```
music_project/
├── index/          # 首页应用 - 核心功能
├── user/           # 用户管理应用
├── play/           # 音乐播放应用
├── comment/        # 评论系统应用
├── search/         # 搜索功能应用
├── ranking/        # 排行榜应用
├── static/         # 静态文件
│   ├── songFile/   # 音乐文件
│   ├── songImg/    # 专辑封面
│   └── songLyric/  # 歌词文件
├── templates/      # HTML模板
└── music/          # 项目配置
```

## 🎯 核心功能

### 用户系统
- **用户注册** - 支持用户名、手机号注册
- **用户登录** - 多种方式登录验证
- **个人中心** - 播放历史、个人信息管理

### 音乐播放
- **在线播放** - 流畅的音乐播放体验
- **播放列表** - 自动记录播放历史
- **歌词显示** - 同步歌词展示
- **歌曲下载** - 支持音乐文件下载

### 社交功能
- **评论互动** - 对歌曲发表评论
- **热门排行** - 多种维度排行榜
- **搜索推荐** - 智能搜索和推荐

## 🔧 配置说明

### 数据库配置
支持MySQL和SQLite数据库，在`settings.py`中配置：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或 'sqlite3'
        'NAME': 'music',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 静态文件配置
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### 自定义用户模型
```python
AUTH_USER_MODEL = 'user.MyUser'
```

## 🧪 测试说明

### 运行测试

```bash
# 运行所有测试
python manage.py test

# 运行特定应用测试
python manage.py test index
python manage.py test user

# 生成测试覆盖率报告
coverage run manage.py test
coverage report
coverage html
```

### 测试类型

- **单元测试** - 模型、表单、视图测试
- **集成测试** - 用户流程、数据库集成测试
- **性能测试** - 批量操作、查询性能测试

### 测试数据
测试使用独立数据库，不会影响生产数据。测试数据在`setUp`方法中自动创建和清理。

## 📊 API接口

### 歌曲相关接口
```
GET  /api/songs/          # 歌曲列表
GET  /api/songs/{id}/     # 歌曲详情
POST /api/songs/{id}/play # 播放歌曲
```

### 用户相关接口
```
POST /api/users/register  # 用户注册
POST /api/users/login     # 用户登录
GET  /api/users/profile   # 用户信息
```

### 评论相关接口
```
GET  /api/comments/song/{song_id}  # 歌曲评论
POST /api/comments/                # 发表评论
```

## 🐛 故障排除

### 常见问题

1. **数据库连接错误**
```bash
# 检查MySQL服务
net start mysql

# 验证数据库配置
python manage.py check
```

2. **静态文件无法访问**
```python
# 检查static配置
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

3. **音乐文件无法播放**
- 检查文件路径是否正确
- 验证文件格式（支持MP3）
- 检查文件权限

4. **用户登录问题**
- 检查用户是否激活
- 验证密码是否正确
- 检查Session配置

### 日志查看
```bash
# 查看应用日志
tail -f logs/music.log

# Django调试信息
python manage.py runserver --verbosity 2
```

## 📈 性能优化

### 数据库优化
- 使用`select_related`减少查询次数
- 添加适当的数据库索引
- 使用分页限制数据量

### 缓存策略
- 使用Redis缓存热点数据
- 静态文件CDN加速
- 数据库查询缓存

## 🔒 安全配置

### 安全措施
- 用户密码加密存储
- CSRF保护机制
- XSS攻击防护
- SQL注入防护

### 安全建议
- 定期更新依赖包
- 使用HTTPS协议
- 设置强密码策略
- 定期安全审计

## 🚀 部署指南

### 生产环境部署
1. 配置生产环境设置
2. 设置DEBUG=False
3. 配置数据库连接
4. 收集静态文件
5. 配置Web服务器

### 使用uWSGI部署
```bash
# 安装uWSGI
pip install uwsgi

# 启动服务
uwsgi --ini uwsgi.ini
```

### 使用Docker部署
```dockerfile
# Dockerfile示例
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uwsgi", "--ini", "uwsgi.ini"]
```

## 🤝 开发贡献

### 代码规范
- 遵循PEP 8编码规范
- 使用类型注解
- 编写详细的文档字符串
- 添加适当的单元测试

### 提交规范
- 使用清晰的提交信息
- 一个功能一个提交
- 提交前运行测试
- 代码审查流程

## 📄 许可证

本项目采用MIT许可证。详见[LICENSE](LICENSE)文件。

## 👥 开发团队

- **HANJUN** - 项目架构设计
- **HANJUN** - 核心功能开发
- **HANJUN** - 用户系统开发
- **HANJUN** - 前端界面设计
- **HANJUN** - 测试和文档

## 📞 技术支持

如有问题或建议，请通过以下方式联系：

1. 查看本文档的故障排除部分
2. 检查项目Issue列表
3. 提交新的Issue描述问题

---

**项目测试&主要二次开发**HANJUN
**最后更新**: 2025年11月  
**版本**: v1.0.0