from pathlib import Path

def get_cats_info(path):
    cats_info = []
    cats_dict = {}
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id_cat, name_cat, age_cat = line.split(',')                
                cats_dict = {'id': id_cat, 'name': name_cat, 'age': age_cat}                
                cats_info.append(cats_dict)
    except FileNotFoundError:
        return "File not found Error!"
    except OSError:
        return "Error while reading file!"

    return cats_info   

path = Path('path/to/cats_info.txt')
cats_info = get_cats_info(path)
print(cats_info) 
