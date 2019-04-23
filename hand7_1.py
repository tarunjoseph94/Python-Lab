class Rectangle:
	def __init__(self,height,width):
		self.height=height
		self.width=width
	def area(self):
		a=self.height*self.width
		return a 
	def peri(self):
		p=2+(self.height+self.width)
		return p
	def heightReturn(self):
		return self.height
	def widthReturn(self):
		return self.width
	def isSqaure(self):
		if(self.height==self.width):
			print("It is a square")
		else:
			print("It is not a square")
r1=Rectangle(10,10)
print(r1.area())
print(r1.peri())
print(r1.heightReturn())
print(r1.widthReturn())
r1.isSqaure()