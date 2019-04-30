import sys
f = open(sys.argv[1])

line=1
i=0
word=[]
charcount=''
while line:
	line = f.readline()
	if line!="":
		charcount+=line
	 
		
		i+=1
	print(line)

print(i)
print(len(charcount))
word=charcount.split(" ")
print(word)
print(len(word))