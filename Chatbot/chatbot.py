# Функція для розбору введених користувачем команд
def parse_input(user_input):
    """
    Розбирає вхідний рядок на команду і аргументи.
    
    Параметри:
    user_input (str): Рядок введений користувачем.

    Повертає:
    tuple: Команда та аргументи (якщо є).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Переводить команду в нижній регістр і видаляє зайві пробіли
    return cmd, *args

# Функція для додавання контакту у словник
def add_contact(args, contacts):
    # Перевірка (args) на наявність двох елементів
    if len(args) != 2:
        return "Error: Please provide your name and telephone number, separated by a space"
    """
    Додає новий контакт до словника.

    Параметри:
    args (list): Ім'я та номер телефону.
    contacts (dict): Словник з контактами.

    Повертає:
    str: Повідомлення про успішне додавання.
    """
    name, phone = args  # Отримуємо ім'я та телефон з аргументів
    contacts[name] = phone  # Додаємо контакт до словника
    return "Contact added."

# Функція для зміни номера телефону існуючого контакту
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide your name and telephone number,separated by a space"
    """
    Змінює номер телефону для існуючого контакту.

    Параметри:
    args (list): Ім'я та новий номер телефону.
    contacts (dict): Словник з контактами.

    Повертає:
    str: Повідомлення про успішне оновлення або помилку.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone  # Оновлюємо номер телефону
        return f"Contact {name} updated."
    else:
        return f"Contact {name} not found."

# Функція для виведення номера телефону за іменем
def get_phone(args, contacts):
    """
    Виводить номер телефону для зазначеного контакту.

    Параметри:
    args (list): Ім'я контакту.
    contacts (dict): Словник з контактами.

    Повертає:
    str: Номер телефону або повідомлення про відсутність контакту.
    """
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"Contact {name} not found."

# Функція для виведення всіх контактів
def show_all_contacts(contacts):
    """
    Виводить усі збережені контакти.

    Параметри:
    contacts (dict): Словник з контактами.

    Повертає:
    str: Список усіх контактів або повідомлення про порожню записну книжку.
    """
    if contacts:
        all_contacts = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return f"All contacts:\n{all_contacts}"
    else:
        return "No contacts found."

# Основна функція
def main():
    """
    Основна функція програми. Відповідає за взаємодію з користувачем і обробку команд.
    """
    contacts = {}  # Ініціалізація словника для контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)  # Обробка введеної команди

        if command in ["close", "exit"]:
            print("Good bye!")  # Повідомлення перед завершенням
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()  # Запуск основної функції
