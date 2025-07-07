import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mohan@2005",
    database="student_crud"
)

cursor = db.cursor()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    email = input("Enter email: ")
    query = "INSERT INTO students (name, age, grade, email) VALUES (%s, %s, %s, %s)"
    values = (name, age, grade, email)
    cursor.execute(query, values)
    db.commit()
    print("✅ Student added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_student():
    sid = int(input("Enter student ID to update: "))
    name = input("New name: ")
    age = int(input("New age: "))
    grade = input("New grade: ")
    email = input("New email: ")
    query = "UPDATE students SET name=%s, age=%s, grade=%s, email=%s WHERE id=%s"
    values = (name, age, grade, email, sid)
    cursor.execute(query, values)
    db.commit()
    print("🔁 Student updated!")

def delete_student():
    sid = int(input("Enter student ID to delete: "))
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (sid,))
    db.commit()
    print("🗑️ Student deleted!")

# Menu loop
while True:
    print("\n=== Student Management System ===")
    print("1. Add student")
    print("2. View students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("❌ Invalid choice!")

cursor.close()
db.close()
