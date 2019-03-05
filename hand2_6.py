a=int(input("Enter a number "))
b=int(input("Enter a number "))
x=b
while(x!=1):
    if((a%x==0) and (b%x==0)):
        break
    else:
        x-=1
print("The GCD of ",a," and ",b," is ",x)
