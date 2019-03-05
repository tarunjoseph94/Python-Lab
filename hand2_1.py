choice=0
while(choice!=5):
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        print("The sum is ",a+b)
    elif(choice==2):
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        print("The diffrence is ",a-b)
    elif(choice==3):
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        print("The product is ",a*b)
    elif(choice==4):
        a=int(input("Enter the first number "))
        b=int(input("Enter the second number "))
        print("The quotient is ",a/b)
    elif(choice==5):
        break
