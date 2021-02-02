########*******Day 2******

########1: Create a list and swap the second half of the list with the first half of the list, print the list on the screen.

#declare initial list1
list1 = [0,1,2,3,4,5,6,7,8,9]  
print ("The initial list is ", list1)
 
#extend list1 with the last 5 values of list1
list1.extend(list1[0:5])

#delete the first 5 values of list 1 
del list1[:5]  
print ("The swapped list is", list1)


########2: Ask the user to input a single digit variable named n.  Then print out all the even numbers from 0-n.

n = int(input("Please enter a positive integer to find all even entries up to that integer. "))
if n < 0:
    n= int(input("Please enter a POSITIVE integer to find all even entries up to that integer. "))

if n % 2==0:
    evenlist = [i for i in range(n+1) if i % 2 == 0]
    print("The list of even numbers from 0 to your entry is ",evenlist)
else: 
    evenlist = [i for i in range(n) if i % 2 == 0]
    print("The list of even numbers from 0 to your entry is ", evenlist)   