import secrets
import string

def generate(length=16):
    """
    生成随机密码
    :param length: 密码长度，默认16
    :return: 随机密码字符串
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(length))