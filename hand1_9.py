name=input("Enter your name")
sem=input("Enter your semester")
sub1=int(input("Enter the first subject marks"))
sub2=int(input("Enter the second subject marks"))
sub3=int(input("Enter the third subject marks"))
sub4=int(input("Enter the fourth subject marks"))
sub5=int(input("Enter the fifth subject marks"))
sub6=int(input("Enter the sixth subject marks"))
add=sub1+sub2+sub3+sub4+sub5+sub6
per=(add/600)*100
print("Your percentage is "+str(per))
if(per>=90):
    print("Your grade is S+")
elif(per>=80):
    print("Your grade is S")
elif(per>=70):
    print("Your grade is A")
elif(per>=60):
    print("Your grade is B")
elif(per>=50):
    print("Your grade is C")
else:
    print("Your grade is F")
