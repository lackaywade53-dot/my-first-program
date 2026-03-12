#This is a program that asks a user
#for their name, surname, age and current_year then prints
#a message that says Hello name surname, You were
#born in year_of_birth

#Message to the user
message = "Hello Nerd, welcome to python\n"
print(message)

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
current_year = int(input("Enter the current year: "))

year_of_birth = current_year - age
print(f"Hello {name} {surname}, you were born in {year_of_birth}.")
