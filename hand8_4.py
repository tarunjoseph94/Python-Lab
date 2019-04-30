import sys

wordlst={}
word=[]
f = open(sys.argv[1])

line=1
charcount=''
while line:
	line = f.readline()
	if line!="":
		charcount+=line
word=charcount.split(" ")
print(word)
for i in word:
	if(i in wordlst):
		wordlst[i]+=1
	else:
		wordlst[i]=1
print(wordlst)

#make sure the file you are using is formatted for proper results