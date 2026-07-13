Numbers=[]

n=int(input("Enter the Number of Elements :"))

for i in range(n):
    num=int(input("Enter the Elements : "))
    Numbers.append(num)

print("\nList Elements are :")

for i in range(n):
    print(Numbers[i])
