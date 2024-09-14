from pathlib import Path

def total_salary(path):
    salary = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                salary.append(int(line.split(",")[1]))
            total = sum(salary)
            avarage = int(total / len(salary))
    except FileNotFoundError:
        return "File not found Error!" 
    except OSError:
        return "Error while reading file!"
    except ValueError:
        return "Error: File does not contain integers!"  
    return total, avarage  

path = Path('path/to/salary_file.txt') 
total, avarage = total_salary(path)
print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {avarage}')
