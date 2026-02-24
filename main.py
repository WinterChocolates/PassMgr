import argparse

from core.auth import setup_master, verify_master
from core.crypto import get_cipher
from core.vault import load_vault, save_vault

from cli import commands


def main():

    parser = argparse.ArgumentParser(description="简易密码管理器")

    parser.add_argument(
        "command",
        choices=["add", "get", "list", "delete"],
        help="可用命令"
    )

    args = parser.parse_args()

    setup_master()

    pwd = verify_master()
    if not pwd:
        return

    cipher = get_cipher(pwd)

    data = load_vault(cipher)

    if args.command == "add":
        commands.add(data)

    elif args.command == "get":
        commands.get(data)

    elif args.command == "list":
        commands.list(data)

    elif args.command == "delete":
        commands.delete(data)

    save_vault(cipher, data)


if __name__ == "__main__":
    main()