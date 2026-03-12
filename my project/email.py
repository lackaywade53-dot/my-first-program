#Created by wade lackay
#Default login data
username = "admin"
password = "admin@2026"


#Getting input from user
user_input= input("Please enter your username: ")
pass_input = input("Please enter your password: ")


#Check if both the username and password are wrong 
if user_input != username and pass_input != password:
    print("Username and Password are wrong")

elif user_input != username:
    print("Username is wrong")
elif pass_input != password:
    print("Password is wrong")

else:
    print("You have successfully Logged in")
