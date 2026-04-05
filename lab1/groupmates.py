#coding:utf-8
groupmates = [
    {
        "name": "Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]

def print_students(students: list[dict]):
    print("Имя студента".ljust(15),
          "Группа".ljust(8),
          "Возраст".ljust(8),
          "Оценки".ljust(20))
    for student in students:
        print(str(student["name"]).ljust(15),
              str(student["group"]).ljust(8),
              str(student["age"]).ljust(8),
              str(student["marks"]).ljust(20))
    print("\n")

def get_filtered_students(students: list[dict], target_mark: float):
    outer_students: list = []
    
    for student in students:
        
        if student.get("marks"):
            student_marks: list[int] = student.get("marks")
            avg_mark: float = sum(student_marks) / len(student_marks)
        else:
            print(f"У студента {student.get("name")} нет оценок")
            continue
            
        if avg_mark > target_mark:
            outer_students.append(student)
    
    if len(outer_students) == 0:
        print(f"Нет ни одного студента со средней оценкой выше заданной: {target_mark}")
    else:
        print_students(students=outer_students)
    
    return outer_students

get_filtered_students(students=groupmates, target_mark=3.4)