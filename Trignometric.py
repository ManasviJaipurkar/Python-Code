def factorial(num):
    fact = 1
    for i in range(1, num + 1):   
        fact = fact * i
    return fact 

import math
x = math.radians(float(input("Enter the value of x:  ")))
n = int(float(input("Enter the value of n: ")))
print("x in radian is ", x)
print("The value of n is ", n)
series_approx = 0
list_of_each_term = []
def sin_funcation(x, n):
    for i in range(n+1):
        numeritor = (-1)**i * (x**(2*i + 1))
        denominator = factorial(2*i + 1)
        each_term = numeritor / denominator
        list_of_each_term.append(each_term)
        output = sum(list_of_each_term)
    return list_of_each_term, output

EACH_TERM , OUTPUT = sin_funcation(x,n)

print(f"\nThe values of Each term is:  {EACH_TERM}\n")
print(f"The output of Series approximation: {OUTPUT}\n") 
print(f"The value of math.sin is: {math.sin(x)}\n")
print(f"The absolute Error is: {math.sin(x) - OUTPUT}")




