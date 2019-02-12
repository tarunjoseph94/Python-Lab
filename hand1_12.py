comp_price=int(input("Enter the price of a computer"))
comp_sold=int(input("Enter how many computers have been sold"))
bonus=200*comp_sold
com=(comp_price/100)*2
grossSal=bonus+com+1500
print("The gross Salary is "+str(grossSal))
