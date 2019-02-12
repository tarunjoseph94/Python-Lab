w1='kyoto'
w1=w1[3:]+w1[:3]
print(w1)
w2='bread'
w2=w2[0]+w2[2:]
print(w2)
w3='kartasura'
w3=w3[5:]+w3[:5]
print(w3)
w4='listen'
w4=w4[2]+w4[1]+w4[0]+w4[4]+w4[5]+w4[3]
print(w4)
#or also this way
w4='listen'
w4=w4[::-1]
w4=w4[3:]+w4[1]+w4[0]+w4[2]
print(str(w4))
