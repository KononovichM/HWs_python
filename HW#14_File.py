file_name = "students.txt"

students_data = [
    "Иванов Иван, 101, 5 4 3",
    "Петров Петр, 102, 4 4 5",
    "Сидоров Алексей, 103, 3 3 4",
    "Алексеев Алексей, 101, 4 5 5",
    "Морозов Виктор, 102, 3 4 4",
    "Пупкин Василий, 103, 5 4 4"
]

with open(file_name, "w", encoding="utf-8") as file:
    file.write("\n".join(students_data) + "\n")

with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

total_students = len(lines)
groups = {}
for line in lines:
    name, group, grades = line.strip().split(", ")
    grades = list(map(int, grades.split()))
    if group not in groups:
        groups[group] = []
    groups[group].extend(grades)

stats = [f"Общее количество студентов: {total_students}"]
for group, grades in groups.items():
    avg_grade = sum(grades) / len(grades)
    stats.append(f"Группа {group}: Количество студентов: {len([l for l in lines if f', {group},' in l])}, "
                 f"Средняя оценка: {avg_grade:.2f}")

with open(file_name, "a", encoding="utf-8") as file:
    file.write("\n" + "\n".join(stats) + "\n")

print("\n".join(stats))
