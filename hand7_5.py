class GrandParent:
	def __init__(self):
		print("GrandParent constructor")
	def methG(self):
		print("GrandParent Method")
	def meth1(self):
		print("1")
class Parent(GrandParent):
	def __init__(self):
		print("Parent constructor")
	def methP(self):
		print("Parent Method")
	def meth1(self):
		print("2")
class Uncle:
	def methU(self):
		print("Uncle class")
class Child(Parent,Uncle):
	def __init__(self):
		super(). __init__()
		print("Child constructor")
	def methC(self):
		print("Child Method")
	def meth1(self):
		print("3")
c1=Child()
c1.methG()
c1.methP()
c1.methU()
c1.methC()
c1.meth1()