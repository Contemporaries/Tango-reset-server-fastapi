# IHEP Tango REST API

基于FastAPI和PyTango的REST API服务，用于与Tango设备进行交互。

## 系统要求

- Python 3.8+
- Tango服务器环境

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/your-username/IHEP-Tango-Rest-API.git
cd IHEP-Tango-Rest-API
```

2. 创建并激活虚拟环境：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 项目结构

```
IHEP-Tango-Rest-API/
├── assets/          # 静态资源文件
├── config/          # 配置文件
│   ├── env_config.py   #配置环境变量
│   ├── log_config.py   #配置日志
├── controller/      # API控制器
│   ├── controller_attribute.py   # 属性相关接口
│   ├── controller_command.py     # 命令相关接口
│   ├── controller_db.py         # 数据库相关接口
│   ├── controller_info.py       # 信息查询接口
│   ├── controller_polling.py    # 轮询相关接口
│   └── controller_property.py   # 属性配置接口
|   └── controller_env.py       # 环境变量接口
├── exception/       # 异常处理
├── model/          # 数据模型
├── service/        # 业务逻辑层
│   ├── service_attribute.py     # 属性服务
│   ├── service_command.py       # 命令服务
│   ├── service_db.py           # 数据库服务
│   ├── service_info.py         # 信息查询服务
│   ├── service_polling.py      # 轮询服务
│   └── service_property.py     # 属性配置服务
│   └── service_env.py       # 属性环境变量服务
├── test/           # 测试文件
├── tools/          # 工具函数
├── enums/          # 枚举定义
├── main.py         # 应用入口
└── requirements.txt # 项目依赖
└── .env            # 环境变量
```


## 开发指南

### 1. 添加新API

1. 在`controller`目录下创建新的控制器文件
2. 在`service`目录下实现业务逻辑
3. 在`main.py`中注册路由

### 2. 错误处理

使用`GlobalException`进行统一的错误处理：

```python
from exception.global_exception import GlobalException

try:
    # 业务逻辑
except Exception as e:
    raise GlobalException(str(e))
```

### 3. 响应模型

使用`ResponseModel`确保统一的响应格式：

```python
from model.response_models import ResponseModel

return ResponseModel(
    success=True,
    message="success",
    data=# 具体数据

)
```