import os
import getpass
from .crypto import hash_password
 
MASTER_FILE = "data/master.key"

def setup_master():
    """设置主密码"""

    os.makedirs("data", exist_ok=True)

    if os.path.exists(MASTER_FILE):
        return
    
    print("设置主密码")
    pwd = getpass.getpass("请输入主密码：")

    with open(MASTER_FILE, "w") as f:
        f.write(hash_password(pwd))

    print("主密码设置成功")

def verify_master():
    """验证主密码"""
    pwd = getpass.getpass("请输入主密码：")

    with open(MASTER_FILE) as f:
        saved = f.read()

    if hash_password(pwd) != saved:
        print("主密码错误")
        return None
    
    return pwd