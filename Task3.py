import os
import sys
from colorama import Fore, Style, init

def print_directory_tree(directory, indent=""):
    try:
        items = sorted(os.listdir(directory))
    except PermissionError:
        print(f"{Fore.RED}{indent}[Permission Denied]{Style.RESET_ALL}")
        return

    for idx, item in enumerate(items):
        path = os.path.join(directory, item)
        connector = "└── " if idx == len(items) - 1 else "├── "
        if os.path.isdir(path):
            print(f"{indent}{connector}{Fore.BLUE}{item}{Style.RESET_ALL}")
            # Continue with one level deeper indentation
            deeper_indent = indent + ("    " if idx == len(items) - 1 else "│   ")
            print_directory_tree(path, deeper_indent)
        else:
            print(f"{indent}{connector}{Fore.GREEN}{item}{Style.RESET_ALL}")

def main():
    init(autoreset=True)
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Вкажіть шлях до директорії як аргумент!{Style.RESET_ALL}")
        sys.exit(1)
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"{Fore.RED}Вказаний шлях не є директорією: {root_dir}{Style.RESET_ALL}")
        sys.exit(1)
    print(f"{Fore.BLUE}{os.path.basename(os.path.abspath(root_dir))}{Style.RESET_ALL}")
    print_directory_tree(root_dir)

if __name__ == "__main__":
    main()
