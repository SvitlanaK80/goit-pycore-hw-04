import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізуємо colorama (для Windows)
init(autoreset=True)

def create_test_structure(directory: Path):
    """Створює тестову структуру директорії, якщо її ще немає."""
    try:
        # Створюємо папки
        (directory / "picture").mkdir(exist_ok=True)
        (directory / "picture" / "Logo").mkdir(exist_ok=True)
        print(Fore.YELLOW + "✅ Папки створено!")

        # Створюємо файли
        files = [
            "picture/Logo/IBM+Logo.png",
            "picture/Logo/ibm.svg",
            "picture/Logo/logo-tm.png",
            "picture/bot-icon.png",
            "picture/mongodb.jpg"
        ]

        for file in files:
            file_path = directory / file
            if not file_path.exists():
                file_path.touch()  # Створює порожній файл
                print(Fore.YELLOW + f"✅ Файл створено: {file_path}")
            else:
                print(Fore.CYAN + f"ℹ️ Файл вже існує: {file_path}")

    except Exception as e:
        print(Fore.RED + f"❌ Помилка під час створення структури: {e}")