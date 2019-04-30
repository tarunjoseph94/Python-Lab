#user prompt
# fname=input("Enter the file name")
# f = open(fname)

# command line argument
import sys
f = open(sys.argv[1])

line=1
lst=[]
while line:
    line = f.readline()
    line=line.rstrip()
    if(line!=''):
    	lst.append(int(line))



for i in range(len(lst)):
	for j in range(len(lst)):
		if(lst[i]<lst[j]):
			temp=lst[j]
			lst[j]=lst[i]
			lst[i]=temp
print(lst)