# PassMgr - 简易命令行密码管理器

PassMgr 是一个用 Python 编写的简单命令行密码管理器。它通过主密码保护您的所有账号信息，并使用 Fernet 对存储的数据进行对称加密。

## 功能特点

- **主密码保护**：首次运行需设置主密码，之后每次访问都需要验证。
- **安全加密**：使用 `cryptography` 库提供的 Fernet 对称加密，确保数据在存储时的安全。
- **基本管理操作**：
  - `add`: 添加新的网站账号和密码。
  - `get`: 根据网站名称查询对应的账号和密码。
  - `list`: 列出所有已保存的网站和用户名。
  - `delete`: 删除指定的账号信息。
- **自动密码生成**：在添加新账号时，支持自动生成高强度的随机密码。

## 项目结构

- [main.py](./main.py): 项目入口，负责解析命令、身份验证和调度功能。
- [cli/](./cli/): 包含命令行交互逻辑。
  - [commands.py](./cli/commands.py): 实现具体的增删改查交互命令。
- [core/](./core/): 核心业务逻辑。
  - [auth.py](./core/auth.py): 负责主密码的设置与验证。
  - [crypto.py](./core/crypto.py): 包含加密、哈希和密钥派生逻辑。
  - [vault.py](./core/vault.py): 负责加密数据的读取和保存。
- [utils/](./utils/): 辅助工具类。
  - [password.py](./utils/password.py): 实现随机密码生成功能。
- [data/](./data/): 存放加密后的库文件和主密码哈希值。

## 安装与运行

### 环境准备

1. 确保安装了 Python 3.8.X或者更高版本。
2. 安装依赖库：

   ```bash
   pip install cryptography
   ```

### 运行程序

1. 在项目根目录下，运行 `main.py` 并指定相应的命令：

   ```bash
   python main.py [add | get | list | delete]
   ```

2. 首次运行会提示设置主密码。

## 使用示例

### 添加账号
```bash
python main.py add
```

### 查看所有网站
```bash
python main.py list
```

### 查询特定网站密码
```bash
python main.py get
```

### 删除账号
```bash
python main.py delete
```

## 注意事项

- **请务必牢记您的主密码**。如果丢失主密码，您将无法恢复加密存储的数据。
- 主密码以哈希形式存储在 `data/master.key` 中，而您的账号数据存储在 `data/vault.dat` 中。
