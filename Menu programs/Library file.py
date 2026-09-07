def library_write():
    F = open("e://BCA1//library.txt", "a")

    accno = int(input("Enter the AccNo: "))
    book_name = input("Enter the Book name: ")
    book_auth = input("Enter the Book Author: ")
    no_copies = int(input("Enter the No. of Copies: "))

    F.write(f"{accno},{book_name},{book_auth},{no_copies}\n")
    F.close()


def library_read():
    F = open("e://BCA1//library.txt", "r")

    print("-" * 80)
    print("AccNo\t\tBookName\t\tBook Author\t\tNo. of Copies")
    print("-" * 80)

    for dec in F:
        st = dec.strip().split(",")

        print(f"{st[0]:<10} {st[1]:<25} {st[2]:<25} {st[3]:<20}")

    print("-" * 60)

    F.close()


Ch = 0

while Ch != 3:

    print("\n1.Write")
    print("2.Read")
    print("3.Exit")

    Ch = int(input("Enter your choice: "))

    if Ch == 1:
        library_write()

    elif Ch == 2:
        library_read()

    elif Ch == 3:
        print("End of Program")

    else:
        print("Invalid Choice")
