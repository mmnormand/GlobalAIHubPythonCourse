#********Intro to Python Homework DAY 3*******

#User Login Application: 
#- Get Username and Password Values from the user
#-Check the values in an if statement and tell the user if they were successful
username = "me"
password = "mypassword"

username1 = input("Enter Username: ")
password1 = input("Enter Password: ")
if (username1 != username and password1 != password):
    print("Invalid Username and Password")

elif (username1 == username and password1 != password):
    print("Invalid Password.")

elif (username1 != username and password1 == password):
    print("Invalid Username.")

else:
    print("You are now logged in.")




#Extra:
#-Try building the same user login application, but this time, use a dictionary

user = {"username": "me", "password": "mypassword"}


username1 = input("Enter Username (Dictionary Example): ")
password1 = input("Enter Password (Dictionary Example): ")
if (username1 != user["username"] and password1 != user["password"]):
    print("Invalid Username and Password")

elif (username1 == user["username"] and password1 != user["password"]):
    print("Invalid Password.")

elif (username1 != user["username"] and password1 == user["password"]):
    print("Invalid Username.")

else:
    print("You are now logged in (Dictionary Example).")