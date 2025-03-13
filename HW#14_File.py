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
    lines: list[str] = file.readlines()

total_students: int = len(lines)
groups: dict[str, list[int]] = {}

for line in lines:
    name, group, grades_str = line.strip().split(", ")
    grades: list[int] = list(map(int, grades_str.split()))
    if group not in groups:
        groups[group] = []
    groups[group].extend(grades)

stats: list[str] = [f"Общее количество студентов: {total_students}"]

for group, grades in groups.items():
    avg_grade: float = sum(grades) / len(grades)
    num_students: int = sum(1 for line in lines if f", {group}," in line)
    stats.append(f"Группа {group}: Количество студентов: "
                 f"{num_students}, Средняя оценка: {avg_grade:.2f}")

with open(file_name, "a", encoding="utf-8") as file:
    file.write("\n" + "\n".join(stats) + "\n")

print("\n".join(stats))
