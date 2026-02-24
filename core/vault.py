import pickle
import os

VAULT_FILE = "data/vault.dat"

def load_vault(cipher):
    """
    加载密码库
    :param cipher: Fernet加密器实例
    :return: 密码库字典
    """
    os.makedirs("data", exist_ok=True)
    
    if not os.path.exists(VAULT_FILE):
        return {}
    
    with open(VAULT_FILE, "rb") as f:
        encrypted = f.read()

    data = cipher.decrypt(encrypted)
    return pickle.loads(data)

def save_vault(cipher, data):
    """
    保存密码库
    :param cipher: Fernet加密器实例
    :param data: 密码库字典
    """
    encrypted = cipher.encrypt(pickle.dumps(data))

    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)