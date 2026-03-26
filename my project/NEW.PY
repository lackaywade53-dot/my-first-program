#message to user 
message = "hello this program lets you store and display student in your class"
print("========================================================================")
print(message)
print("========================================================================")

#ask for input from user
amount = int(input("How many students in your class: "))

#Create empty list for the students
studentlist = []

for y in range(0,amount):
    name = input("Enter student name and surname:")
    studentlist.append(name)

print(studentlist)
