class Base1:
	def implicit(self):
		print("Base1 implicit( )")
class Base2:
	def implicit(self):
		print("Base2 implicit( )")
class Derived1(Base1, Base2):
	def implicit(self):
		super().implicit()
		print("Multiple inheritance achieved")
d1=Derived1()
d1.implicit()