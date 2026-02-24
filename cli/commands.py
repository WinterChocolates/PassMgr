from utils.password import generate

def add(data):
    """添加密码"""
    print("添加账户和密码")
    site = input("网站：")
    user = input("用户名：")

    auto = input("是否自动生成密码？(y/n) ")
    if auto.lower() == "y":
        pwd = generate()
    else:
        pwd = input("密码：")
    
    data[site] = {
        "username": user,
        "password": pwd
    }

    print("账号添加成功")

def get(data):
    """获取密码"""
    print("获取账户和密码")
    site = input("网站：")
    if site not in data:
        print("网站不存在")
        return

    print(f"用户名：{data[site]['username']}，密码：{data[site]['password']}")

def list(data):
    """列出所有网站"""
    print("已保存的网站")

    if not data:
        print("当前没有任何记录")
        return

    for site in data:
        print(f"{site}: {data[site]['username']}")

def delete(data):
    """删除账户"""
    print("删除账户和密码")
    site = input("网站：")
    if site in data:
        del data[site]
        print("账号删除成功")
    else:
        print("网站不存在")
