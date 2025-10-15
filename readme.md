# AMCP Flask Server
https://github.com/zhouwuqi/amcp-remote-access-simple

## 项目简介
这是一个基于Flask框架实现的AMCP（AgentPlus Model Context Protocol）服务端，用于远程访问和管理系统资源。该项目提供了一套RESTful API接口，允许客户端通过HTTP请求获取系统信息、文件内容和执行其他管理操作。

## 功能特性
- **系统监控**：查看文件夹内容、运行进程、NVIDIA GPU状态、内存使用情况和磁盘使用情况
- **文件操作**：读取文件内容、在文件中搜索关键词
- **安全验证**：通过密码验证确保API访问的安全性
- **高性能部署**：使用Gunicorn和Gevent进行生产级部署

## 技术栈
- Python 3.x
- Flask Web框架
- Gunicorn WSGI服务器
- Gevent异步网络库
- Requests HTTP库

## 安装依赖
```bash
pip install -r requirements.txt
```

## 快速启动
```bash
chmod +x run.sh
./run.sh
```

服务将在 `http://0.0.0.0:3400` 上运行。

## API接口说明

### 主要端点
- `POST /amcp/mini-machine` - 执行各种系统管理指令

### 支持的指令
1. `tell-folder` - 查看文件夹内容
2. `tell-process` - 查看运行中的进程
3. `tell-nvidia` - 查看NVIDIA GPU状态
4. `tell-memory` - 查看内存使用情况
5. `tell-disk` - 查看磁盘使用情况
6. `read-file` - 读取文件内容
7. `search-in-file` - 在文件中搜索关键词
8. `tell-cpu` - 获取cpu信息
8. `search-file` - 搜索特定文件

### agentplus中配置config格式
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
          "description": "instruction that you want to interact with this system,choose from here:(1)'tell-folder':tell what is inside the folder,require path like /home.(2)'tell-process':tell what process is running.(3)'tell-nvidia':tell about the nvidia GPU's status (if have one).(4)'tell-memory':tell memory usage.(5)'tell-disk':tell disk usage.(6)'read-file':read file by path and row,require path and row,path like /folder/code.py, and the row parameter decides where you start reading,basiclly you should input 1 to read from first line.(7)'search-in-file':search any keyword or sentence in a file,require path and value.(8)'search-file':to find file or folder under the path,require path and value,path for the searching range,value for target file's name(or folder)."
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

## 配置说明
- 服务端口：3400
- 密码验证：在`views.py`中设置`PASSWORD`常量
- 工作进程数：在`run.sh`中配置`NUM_WORKERS`变量

## 安全注意事项
1. 请务必修改默认密码以确保安全性
2. 建议在生产环境中使用HTTPS协议
3. 不要在公开网络上暴露此服务，除非采取适当的安全措施

## 目录结构
```
.
├── amcp_config_sample/      # 配置文件示例目录
├── __pycache__/             # Python缓存目录
├── commands.py              # 系统命令执行逻辑
├── main.py                  # Flask应用主入口
├── readme.md                # 项目说明文档
├── requirements.txt         # Python依赖包列表
├── run.sh                   # 服务启动脚本
├── terminal.py              # 终端命令执行模块
└── views.py                 # API路由和业务逻辑
```

## 贡献指南
欢迎提交Issue和Pull Request来改进这个项目。在贡献代码前，请确保：
1. 遵循现有的代码风格
2. 添加适当的测试用例
3. 更新相关文档

## 许可证
[待补充具体的许可证信息]

## 联系方式
如需技术支持或有任何疑问，请联系项目维护者。