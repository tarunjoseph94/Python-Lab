n=int(input("Enter the limit "))
lst=[]
prime=[]
nprime=[]
for i in range(2,n):
    lst.append(i)
for i in lst:
    flag=0
    for j in range(2,i):
        if((i%j)==0):
            nprime.append(i)
            flag=1
            break
    if(flag==0):
        prime.append(i)
print("Prime ",prime)
print("Not Prime ",nprime)
