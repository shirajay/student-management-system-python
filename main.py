import os

FILE_NAME = "students.txt"

# Load Students from File
def load_students():
    students = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    students[data[0]] = {
                        "name": data[1],
                        "age": data[2],
                        "course": data[3],
                        "marks": data[4]
                    }
    return students


# Save Students to File
def save_students(students):
    with open(FILE_NAME, "w") as file:
        for sid, info in students.items():
            file.write(f"{sid},{info['name']},{info['age']},{info['course']},{info['marks']}\n")


# Add Student
def add_student(students):
    sid = input("Enter Student ID: ")

    if sid in students:
        print("❌ Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    students[sid] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print("✅ Student Added Successfully!")


# View Students
def view_students(students):
    if not students:
        print("⚠ No Records Found!")
        return

    print("\n----- Student Records -----")
    for sid, info in students.items():
        print(f"\nID: {sid}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Course: {info['course']}")
        print(f"Marks: {info['marks']}")


# Search Student
def search_student(students):
    sid = input("Enter Student ID to Search: ")

    if sid in students:
        info = students[sid]
        print("\n✅ Student Found:")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Course: {info['course']}")
        print(f"Marks: {info['marks']}")
    else:
        print("❌ Student Not Found!")


# Update Student
def update_student(students):
    sid = input("Enter Student ID to Update: ")

    if sid in students:
        print("Enter New Details:")
        students[sid]["name"] = input("New Name: ")
        students[sid]["age"] = input("New Age: ")
        students[sid]["course"] = input("New Course: ")
        students[sid]["marks"] = input("New Marks: ")

        print("✅ Student Updated Successfully!")
    else:
        print("❌ Student Not Found!")


# Delete Student
def delete_student(students):
    sid = input("Enter Student ID to Delete: ")

    if sid in students:
        del students[sid]
        print("✅ Student Deleted Successfully!")
    else:
        print("❌ Student Not Found!")


# Main Menu
def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_students(students)
            print("💾 Data Saved Successfully. Exiting...")
            break
        else:
            print("❌ Invalid Choice! Try Again.")


if __name__ == "__main__":
    main()
