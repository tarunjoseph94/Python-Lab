class Test:
	a=10
	def meth(self):
		Test.a+=1
a1=Test()
a2=Test()
print(a1.a)
print(a2.a)
print(Test.a)
a1.meth()
print(a1.a)
print(a2.a)