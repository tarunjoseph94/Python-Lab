import sys
f = open(sys.argv[1])
line = f.read()	
print(line)
print(line.count(''))
print(line.count('\n'))
print(line.count(' ')+line.count('\n'))
