#Using operator

#Example 1 checking for equality
a = 10
b = 15

print("Equality a==b:", a==b)
print("Not equal to a!=b:", a!=b)

#uaing Modulus - Getting the reminder after division

num1 = 5
num2 = 2

#Finding modulus
reminder = num1 % num2

print("The reminder from num1 % num2: ", reminder)

#checking if a number from the user is even or odd

#inputNum = int(input("Enter any number: ")) 
#rem = inputNum % 2
#if rem==0:
 #   print("The number you entered is even")
#else:
#    print("The number is not even")

mark = float(input("Please enter your mark: "))
if mark >=0 and mark<=49:
    print("Fail")
elif mark >=50 and mark<=59:
    print("Pass")
elif mark >=60 and mark<=69:
    print("Pass+")
elif mark >=70 and mark<=100:
    print("Distinction")
else:
    print("Mark is out of range between 0 and 100")


