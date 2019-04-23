class Box():
	def __init__(self,val):
		self.value=val
	def __nonzero__(self):
		if(self.value%2==0):
			return True
		else:
			return False
aBox=Box(3)
if aBox:
	print("Yay")
else:
	print("Boo")