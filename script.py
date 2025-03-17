import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізуємо colorama 
init(autoreset=True)

def print_directory_structure(directory: Path, prefix=""):
    """Рекурсивно виводить структуру директорії з кольоровим форматуванням у вигляді дерева."""
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + "Помилка: Вказана директорія не існує або не є папкою.")
        return

    items = sorted(directory.iterdir())  # Сортуємо елементи для гарного виводу
    for index, item in enumerate(items):
        is_last = index == len(items) - 1  # Чи останній елемент у списку
        connector = "└── " if is_last else "├── "
        
        if item.is_dir():
            print(prefix + Fore.BLUE + connector + f"[{item.name}]" + Style.RESET_ALL)
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_directory_structure(item, new_prefix)  # Рекурсія для папок
        else:
            print(prefix + Fore.GREEN + connector + item.name + Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python script.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    print(Fore.YELLOW + "\n📂 Структура директорії:\n" + Style.RESET_ALL)
    print_directory_structure(directory_path)
