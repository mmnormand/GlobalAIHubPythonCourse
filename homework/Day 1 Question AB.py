#********************Problem A***************************

#Define the cost of a meal
cost = 40
tax = .08 * cost
tip = .10 * cost
total = cost+tax+tip

#Print the costs and total
print() #break
print() #break
print("For Problem A, The cost of the meal is " + str(cost) + " dollars. The tax on the meal is " + format(tax, ".2f") + " dollars. The Tip for the meal is " + format(tip, ".2f") + " dollars.  The total cost of the meal is " + format(total, ".2f") + " dollars.")


#**********************Problem B******************
#user input cost
cost = float(input("Please enter the cost for the meal: "))
tax = .08 * cost
tip = .10 * cost
total = cost+tax+tip

#Print the costs and total
print() #break

print("For Problem B, The tax on the meal is " + format(tax, ".2f") + " dollars. The Tip for the meal is " + format(tip, ".2f") + " dollars.  The total cost of the meal is " + format(total, ".2f") + " dollars.")



