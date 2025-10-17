
# AMCP Flask Server  
🔗 GitHub 地址：[https://github.com/zhouwuqi/amcp-remote-access-simple](https://github.com/zhouwuqi/amcp-remote-access-simple)

## 📘 项目简介

这是一个基于 **Flask 框架** 实现的 **AMCP（AgentPlus Model Context Protocol）服务端**，用于远程访问和管理系统资源。它提供了一套 RESTful API 接口，支持客户端通过 HTTP 请求获取系统信息、文件内容以及执行其他管理任务。

---

## ⚙️ 核心功能

### 🖥️ 系统监控
- `tell-folder`: 查看文件夹内容  
- `tell-process`: 查看运行中的进程  
- `tell-nvidia`: 查看 NVIDIA GPU 状态  
- `tell-memory`: 查看内存使用情况  
- `tell-disk`: 查看磁盘使用情况  
- `tell-cpu`: 获取 CPU 信息  

### 📁 文件操作
- `read-file`: 读取本地文件内容（按行分页）  
- `search-in-file`: 在本地文件中搜索关键词  
- `search-file`: 搜索特定文件或目录  

### 🌐 Git 支持（新增）
- `tell-git`: 获取 GitHub 公开仓库的基本信息（默认分支 + 文件列表）  
- `read-git-file`: 读取 GitHub 公开仓库中任意文本文件的内容（按行分页）

> ⚠️ 注意：目前这两个接口仅支持公开仓库。若需访问私有仓库，请配置有效的 GitHub Token。

---

## 💻 技术栈

- Python 3.x  
- Flask Web 框架  
- Gunicorn WSGI 服务器  
- Gevent 异步网络库  
- Requests HTTP 库  

---

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

---

## ▶️ 快速启动

```bash
chmod +x run.sh
./run.sh
```

服务默认在 `http://0.0.0.0:3400` 上运行。

---

## 🌐 API 接口说明

### 主要端点：
- `POST /amcp/mini-machine` —— 执行各种系统管理指令。

### 支持的所有指令如下：

| 指令 | 描述 |
|------|------|
| `tell-folder` | 查看文件夹内容 |
| `tell-process` | 查看运行中的进程 |
| `tell-nvidia` | 查看 NVIDIA GPU 状态 |
| `tell-memory` | 查看内存使用情况 |
| `tell-disk` | 查看磁盘使用情况 |
| `read-file` | 读取文件内容 |
| `search-in-file` | 在文件中搜索关键词 |
| `tell-cpu` | 获取 CPU 信息 |
| `search-file` | 搜索特定文件 |
| `tell-git` | 获取 GitHub 仓库信息 |
| `read-git-file` | 读取 GitHub 文件内容 |

---

## 🧾 agentplus 中配置 config 格式

```json
{
  "url": "http://1.2.3.4:3400/amcp/mini-machine",
  "function":{
    "name": "access_remote_machine",
    "description": "AMCP(agentplus model context protocol) that can access to remote machine.",
    "parameters": {
      "type": "object",
      "properties": {
        "instruction": {
          "type": "string",
          "description": "instruction that you want to interact with this system,choose from here:(1)'tell-folder':tell what is inside the folder,require path like /home.(2)'tell-process':tell what process is running.(3)'tell-nvidia':tell about the nvidia GPU's status (if have one).(4)'tell-memory':tell memory usage.(5)'tell-disk':tell disk usage.(6)'read-file':read file by path and row,require path and row,path like /folder/code.py, and the row parameter decides where you start reading,basiclly you should input 1 to read from first line.(7)'search-in-file':search any keyword or sentence in a file,require path and value.(8)'search-file':to find file or folder under the path,require path and value,path for the searching range,value for target file's name(or folder).(9)'tell-cpu':get cpu info.(10)'tell-git':check a git repository by inputing a path parameter with a like {'owner':owner's name,'repo':repository's name},then you will get the information of that repository(11)'read-git-file':check a file in inside a git repository by inputing path parameter with  like {'owner':owner's name,'repo':repository's name,'filename':file's name inside that git like 'readme.md' or 'folder/file.xx'}, and maybe the row parameter ,that decides where you start reading,basiclly you should input 1 to read from first line."
        },
        "path": {
          "type": "string",
          "description": "the path of folder or file that you want.leave 0 if you do not need it."
        },
        "row": {
          "type": "number",
          "description": "the row when you are reading a file,basiclly you can input 1 if you want read from the first line,leave 0 if you do not need it."
        },
        "value": {
          "type": "string",
          "description": "keyword or sentence if you are searching in a file,leave 0 if you do not need it."
        }
      }
    }
  },
  "frontend":{
    "title":"remote access(simple)",
    "tips":"tell users what your tool can do."
  },
  "params": {
    "password": ".........."
  }
}
```

---

## 🔧 配置说明

- 默认端口为 `3400`
- 可在 `views.py` 中设置密码常量 `PASSWORD`
- 工作进程数量可在 `run.sh` 中配置 `NUM_WORKERS`

---

## 🔐 安全建议

1. 修改默认密码以增强安全性。
2. 生产环境推荐启用 HTTPS 协议。
3. 不应在公网上直接暴露该服务，除非有额外防护措施。

---

## 🗂️ 目录结构

```
.
├── amcp_config_sample/      # 配置文件示例目录
├── __pycache__/             # Python 缓存目录
├── commands.py              # 系统命令执行逻辑 & Git 功能封装
├── git.py                   # GitHub 交互核心逻辑
├── main.py                  # Flask 应用主入口
├── readme.md                # 项目说明文档
├── requirements.txt         # Python 依赖包列表
├── run.sh                   # 服务启动脚本
├── terminal.py              # 终端命令执行模块
└── views.py                 # API 路由和业务逻辑
```

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目。在贡献代码前，请确保：

1. 遵循现有的代码风格  
2. 添加适当的测试用例  
3. 更新相关文档  

---

## 📜 许可证

[待补充具体的许可证信息]

---

## 📬 联系方式

如需技术支持或有任何疑问，请联系项目维护者。

