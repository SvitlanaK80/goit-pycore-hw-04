def total_salary(path):
    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Зчитуємо всі рядки у список
            
        total = 0  # Сума всіх зарплат
        count = 0  # Кількість розробників
        salaries_list = []  # Список зарплат
        
        for line in lines:
            name, salary = line.strip().split(',')  # Розділяємо ім'я та зарплату
            salaries_list.append(line.strip())  # Додаємо до списку оригінальний рядок
            total += int(salary)  # Додаємо зарплату до загальної суми
            count += 1  # Збільшуємо лічильник
        
        average = total / count if count > 0 else 0  # Обчислюємо середню зарплату
        
        return total, average, salaries_list  # Повертаємо також список зарплат

    except FileNotFoundError:
        print("Помилка: Файл не знайдено!")
        return None

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

path_to_file = "salaries.txt"  
result = total_salary(path_to_file)

if result:
    total, average, salary_list = result
    print(f"Загальна зарплата: {total}")
    print(f"Середня зарплата: {average}")

    print("\nСписок зарплат із файлу:")
    for entry in salary_list:
        print(entry)




   

