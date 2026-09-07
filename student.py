def write():
    F = open("e://BCA1//student.txt", "a")

    rno = int(input("Enter the Student Roll No: "))
    name = input("Enter the student name: ")
    address = input("Enter the student Address: ")
    mark1 = int(input("Enter the student mark: "))

    F.write(f"{rno},{name},{address},{mark1}\n")
    F.close()


def read():
    F = open("e://BCA1//student.txt", "r")

    print("-" * 60)
    print(f"{'Rno':<10} {'Name':<20} {'Address':<20} {'Mark':<10}")
    print("-" * 60)

    for rec in F:
        st = rec.strip().split(",")
        print(f"{st[0]:<10} {st[1]:<20} {st[2]:<20} {st[3]:<10}")

    F.close()


ch = 0

while ch != 3:
    print("1... Write")
    print("2... Read")
    print("3... Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        write()

    elif ch == 2:
        read()

    elif ch == 3:
        print("END OF PROGRAM......")

    else:
        print("Invalid Choice")




