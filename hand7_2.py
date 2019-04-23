class Account:
	def __init__(self,bal=200):
		self.bal=bal
	def deposit(self):
		num=int(input("Enter how much you want to deposit"))
		self.bal+=num
	def withdraw(self):
		num=int(input("Enter how much you want to withdraw"))
		if(num>self.bal):
			print("Cannot withdraw more than current balance")
		else:
			self.bal-=num
	def dispBalance(self):
		print("Your current balance is ",self.bal)
a1=Account()
c=0
while(c!=4):
	print("1. Deposit")
	print("2. Withdraw")
	print("3. Display Balance")
	print("4. Exit")
	c=int(input("Enter your choice"))
	if(c==1):
		a1.deposit()
	elif(c==2):
		a1.withdraw()
	elif(c==3):
		a1.dispBalance()
		