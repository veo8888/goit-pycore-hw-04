def get_cats_info(path):
    """
    Функція get_cats_info читає файл з інформацією про котів і повертає список словників з даними про котів.

    Аргументи:
    path (str): шлях до текстового файлу з інформацією про котів.

    Повертає:
    list: список словників, де кожен словник містить інформацію про одного кота.
    """
    cats_list = []  # Список для зберігання інформації про котів

    try:
        # Відкриваємо файл оператором with
        with open(path, 'r', encoding='utf-8') as file:
            # Читаємо файл рядково
            for line in file:
                # Розділяємо рядок на id, ім'я, вік
                cat_id, name, age = line.strip().split(',')
                
                # Створюємо окремі словники для кожного кота
                cat_dict = {"id": cat_id,"name": name,"age": age}
                
                # Додаємо словник до списку
                cats_list.append(cat_dict)

        return cats_list
    # Обробка помилок
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

# Виклик функції:
cats_info = get_cats_info("List of cat data\Cats_data.txt")
print(cats_info)
