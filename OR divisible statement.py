a=int(input("Enter the value of A :"))
R1=a%5
R2=a%7
if(R1==0 or R2==0):
    print("Any one number is divisible")
else:
    print("Both is number is not divisible")
