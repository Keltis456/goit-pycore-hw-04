def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cat_dict = {"id": cat_id, "name": name, "age": age}
                        cats_info.append(cat_dict)
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
    return cats_info

cats = get_cats_info('Task2.txt')
print(cats)