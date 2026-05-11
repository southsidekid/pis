groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Алесей",
        "surname": "Никитин",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Петр",
        "surname": "Морозов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 2, 3]
    },
    {
        "name": "Максим",
        "surname": "Белов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 4, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)

user_input = float(input("Введите минимальный средний балл: "))

filtered_students = []

for student in groupmates:
    average_mark = sum(student["marks"]) / len(student["marks"])
    
    if average_mark > user_input:
        filtered_students.append(student)

print("\nРезультаты фильтрации:")
print_students(filtered_students)