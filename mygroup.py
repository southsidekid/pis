groupmates = [
    {
        "name": "Глеб",
        "surname": "Галыбин",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Аня",
        "surname": "Меньшикова",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Эва",
        "surname": "Караваева",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Егор",
        "surname": "Дементьев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 3, 4]
    },
    {
        "name": "Екатерина",
        "surname": "Кольцова",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


def avg_mark(students, min_average):
    result = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > min_average:
            result.append(student)
    return result

user_input = float(input("Введите минимальный средний балл: "))
filtered = avg_mark(groupmates, user_input)
print_students(filtered)

