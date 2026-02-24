import hashlib
import base64
from cryptography.fernet import Fernet

def hash_password(password: str) -> str:
    """
    对密码进行哈希处理
    :param password: 密码字符串
    :return: 哈希后的密码字符串
    """
    return hashlib.sha256(password.encode()).hexdigest()

def derive_key(password: str) -> bytes:
    """
    从主密码派生加密密钥
    :param password: 密码字符串
    :return: 派生的密钥字节串
    """
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def get_cipher(key: str):
    """
    获取加密器
    :param key: 密钥字节串
    :return: Fernet加密器实例
    """
    return Fernet(derive_key(key))
