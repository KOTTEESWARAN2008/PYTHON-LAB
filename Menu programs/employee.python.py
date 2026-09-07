def writee():
    f = open("e://BCA1//emp.txt", "a")

    eid = int(input("Enter the Employee ID: "))
    ename = input("Enter the Employee Name: ")
    edesign = input("Enter Employee Designation: ")
    esalary = int(input("Enter the Salary: "))

    f.write(f"{eid},{ename},{edesign},{esalary}\n")
    f.close()


def readee():
    f = open("e://BCA1//emp.txt", "r")

    print("-" * 60)
    print(f"{'Employee ID':<7} {'Employee Name':<23} {'Employee Designation':<20} {'Salary':<10}")
    print("-" * 60)

    for rec in f:
        rt = rec.strip().split(",")
        print(f"{rt[0]:<7} {rt[1]:<23} {rt[2]:<20} {rt[3]:<10}")

    f.close()


ch = 0

while ch != 3:
    print("1... Write")
    print("2... Read")
    print("3... Exit")

    ch = int(input("Enter your Choice: "))

    if ch == 1:
        writee()

    elif ch == 2:
        readee()

    elif ch == 3:
        print("End of Program")

    else:
        print("Invalid Choice")
