import sqlite3

con = sqlite3.connect("e://BCA1//employement.db")
cur = con.cursor()


def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        empid INTEGER,
        name TEXT,
        designation TEXT,
        salary INTEGER
    )
    """)

    con.commit()
    print("Table created successfully")


def insert_record():
    tempid = int(input("Enter Employee ID: "))
    tempname = input("Enter Employee Name: ")
    tempdesignation = input("Enter Designation: ")
    tempsalary = int(input("Enter Salary: "))

    cur.execute(
        "INSERT INTO employee VALUES (?, ?, ?, ?)",
        (tempid, tempname, tempdesignation, tempsalary)
    )

    con.commit()
    print("Record inserted successfully")


def update_record():
    tempid = int(input("Enter Employee ID to update: "))
    tempsalary = int(input("Enter new Salary: "))

    cur.execute(
        "UPDATE employee SET salary = ? WHERE empid = ?",
        (tempsalary, tempid)
    )

    con.commit()
    print("Record updated successfully")


def delete_record():
    tempid = int(input("Enter Employee ID to delete: "))

    cur.execute(
        "DELETE FROM employee WHERE empid = ?",
        (tempid,)
    )

    con.commit()
    print("Record deleted successfully")


def select_records():
    cur.execute("SELECT * FROM employee")

    records = cur.fetchall()

    print(f"\n{'Emp ID':<10}{'Name':<20}{'Designation':<20}{'Salary':<10}")
    print("-" * 60)

    for record in records:
        print(f"{record[0]:<10}{record[1]:<20}{record[2]:<20}{record[3]:<10}")


# Menu
while True:

    print("\n===== EMPLOYEE DATABASE =====")
    print("1. Create Table")
    print("2. Insert")
    print("3. Update")
    print("4. Delete")
    print("5. Select")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_table()

    elif choice == 2:
        insert_record()

    elif choice == 3:
        update_record()

    elif choice == 4:
        delete_record()

    elif choice == 5:
        select_records()

    elif choice == 6:
        break

    else:
        print("Invalid choice")


con.close()

print("Program terminated...........")

