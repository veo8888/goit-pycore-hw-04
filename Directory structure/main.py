import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізуємо Colorama для коректної роботи з кольорами
init(autoreset=True)

def print_directory_structure(path, indent=""):
    """
    Функція рекурсивно виводить структуру директорії, змінюючи колір
    для файлів і папок.

    Аргументи:
    path (Path): Шлях до директорії.
    indent (str): Відступ для виводу вкладених файлів і папок.
    """
    # Якщо це директорія
    if path.is_dir():
        print(Fore.BLUE + f"{indent}{path.name}/")
        # Проходимо по вмісту директорії
        for item in path.iterdir():
            print_directory_structure(item, indent + "    ")
    # Якщо це файл
    elif path.is_file():
        print(Fore.GREEN + f"{indent}{path.name}")

def main():
    """
    Основна функція програми, яка перевіряє аргументи командного рядка
    і запускає візуалізацію структури директорії.
    """
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії.")
        return

    # Отримуємо шлях з аргументів командного рядка
    directory_path = Path(sys.argv[1])

    # Перевіряємо, чи існує директорія
    if not directory_path.exists() or not directory_path.is_dir():
        print(f"Директорія {directory_path} не існує або це не директорія.")
        return

    # Викликаємо функцію для виведення структури директорії
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()