# 1]Check if a number is positive, negative, or zero.
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2]Check whether a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3]Find the greater of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Both are equal")

# 4]Find the greatest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("A is greatest")
elif b >= a and b >= c:
    print("B is greatest")
else:
    print("C is greatest")

# 5]Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 6]Check whether a year is a leap year.
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 7]Check if a character is a vowel or consonant.
ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 8]Check whether a number is divisible by 5 and 11.
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")


# 9]Check if a number is a multiple of both 3 and 7.
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")

# 10]10. Assign grades based on marks:
# a. 90–100: A
# b. 80–89: B
# c. 70–79: C
# d. 60–69: D
# e. Below 60: F
marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 0:
    print("Grade F")
else:
    print("Invalid marks")


# 11]Check if a character is uppercase or lowercase
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an alphabet")


# 12]Find whether the entered alphabet is a vowel using if-elif.
ch = input("Enter an alphabet: ").lower()

if ch == "a":
    print("Vowel")
elif ch == "e":
    print("Vowel")
elif ch == "i":
    print("Vowel")
elif ch == "o":
    print("Vowel")
elif ch == "u":
    print("Vowel")
else:
    print("Consonant")


# 13]Check if three sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# 14]Determine the type of triangle (Equilateral, Isosceles, Scalene).
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid Triangle")
elif a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


# 15]Find the largest among four numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("A is largest")
elif b >= a and b >= c and b >= d:
    print("B is largest")
elif c >= a and c >= b and c >= d:
    print("C is largest")
else:
    print("D is largest")


# 16]Check whether a number is a three-digit number.
num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# 17]Calculate electricity bill using slab rates.
units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity Bill:", bill)
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
    print("Electricity Bill:", bill)
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Electricity Bill:", bill)


# 18]Calculate income tax based on income slabs.
income = float(input("Enter annual income: "))

if income < 0:
    print("Invalid income")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20
else:
    tax = 112500 + (income - 1000000) * 0.30

if income >= 0:
    print("Income Tax:", tax)



# 19]Check if a student passes (minimum 35 marks in each subject).
m1 = int(input("Enter first subject marks: "))
m2 = int(input("Enter second subject marks: "))
m3 = int(input("Enter third subject marks: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Pass")
else:
    print("Fail")


# 20]Find whether a number is within a given range
num = int(input("Enter a number: "))

if 1 <= num <= 100:
    print("Number is within the range")
else:
    print("Number is outside the range")


# 21]Build a simple calculator using if-elif-else (+, -, *, /).
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")



# 22]Check if a year is a century leap year.
year = int(input("Enter year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year but not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 23]Determine the season based on the month number.
month = int(input("Enter month number (1-12): "))

if month in (12, 1, 2):
    print("Winter")
elif month in (3, 4, 5):
    print("Summer")
elif month in (6, 7, 8, 9):
    print("Monsoon")
elif month in (10, 11):
    print("Autumn")
else:
    print("Invalid month")


# 24]Find the number of days in a month.
month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month in (4, 6, 9, 11):
    print("30 days")
elif 1 <= month <= 12:
    print("31 days")
else:
    print("Invalid month")


# 25]Check whether a password meets minimum conditions (length, digits, etc.).
password = input("Enter password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Valid password")
else:
    print("Invalid password")


# 26]Determine ticket price based on age category
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket is free")
elif age <= 17:
    print("Ticket price: Rs. 100")
elif age < 60:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 150")


# 27]Calculate discount based on purchase amount.
amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 10
elif amount >= 1000:
    discount = 5
else:
    discount = 0

if amount >= 0:
    final_amount = amount - (amount * discount / 100)
    print("Discount:", discount, "%")
    print("Final amount: Rs.", final_amount)



# 28]Check if a person is eligible for a driving license (age and eyesight condition).
age = int(input("Enter age: "))
eyesight = input("Is eyesight condition satisfied? (yes/no): ")

if age < 0:
    print("Invalid age")
elif age >= 18 and eyesight.lower() == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible")


# 29]Create a login system with username and password validation.
correct_username = "isha"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")


# 30]Create a menu-driven program using if-elif-else with options like:
# a. Addition
# b. Subtraction
# c. Multiplication
# d. Division
# e. Exit
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you!")
        break

    elif choice in ("1", "2", "3", "4"):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")
    else:
        print("Invalid choice")