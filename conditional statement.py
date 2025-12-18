num = 10

if num > 0:
    print("Number is positive")


num = -5

if num >= 0:
    print("Number is positive or zero")
else:
    print("Number is negative")



num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# Nested if Statement
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")


# Real-Life Example (Student Result)
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")