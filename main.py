def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def main():
    print("STUDENT GRADE MANAGEMENT SYSTEM")

    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    marks = []

    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks in subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Average:", round(average, 2))
    print("Grade:", grade)


if __name__ == "__main__":
    main()