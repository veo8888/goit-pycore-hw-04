def total_salary(path):
    """
    Функція total_salary аналізує файл із заробітними платами і повертає загальну та середню зарплату.

    Аргументи:
    path (str): шлях до текстового файлу з даними про заробітні плати.

    Повертає:
    tuple: кортеж з двох значень - загальна сума зарплат і середня зарплата.
    """
    try:
        total = 0  # Загальна сума зарплат
        workers = 0  # Кількість розробників

        # Відкриваємо файл оператором with
        with open(path, 'r', encoding='utf-8') as file:
            # Читаємо файл рядково
            for line in file:
                # Розділяємо кожен рядок на ім'я та зарплату
                _, salary = line.strip().split(',')
                # Додаємо зарплату до загальної суми
                total += float(salary)
                # Додаємо кількість працівників
                workers += 1
        
        # Обчислюємо середню зарплату
        average = total / workers if workers != 0 else 0

        # Повертаємо загальну та середню зарплату
        return total, average
    
    # Обробка помилок
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0

# Виклик функції:
total, average = total_salary("Salary calculation\salary.txt")
print(f"Загальна сума заробітної плати: {total:.2f},  Середня заробітна плата: {average:.2f}")