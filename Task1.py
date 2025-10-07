def total_salary(path):
    """
    Аналізує файл з даними про зарплати та обчислює загальну і середню суму.
    
    Args:
        path: Шлях до текстового файлу з даними про зарплати
        
    Returns:
        tuple: (загальна сума зарплат, середня зарплата)
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                line = line.strip()
                if line:  # Пропускаємо порожні рядки
                    parts = line.split(',')
                    if len(parts) == 2:
                        try:
                            salary = float(parts[1])
                            salaries.append(salary)
                        except ValueError:
                            print(f"Помилка: неможливо обробити зарплату в рядку '{line}'")
                            continue
            
            if not salaries:
                return (0, 0)
            
            total = sum(salaries)
            average = total / len(salaries)
            
            return (total, average)
    
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
        return (0, 0)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return (0, 0)


# Приклад використання
total, average = total_salary("Task1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")