import re
#user prompt
fname=input("Enter the file name")
f = open(fname)

# command line argument
# import sys
# f = open(sys.argv[1])

line=1
while line:
    line = f.readline()
    matchob=re.match('^#',line,re.I)
    if (matchob):
        print (line)

