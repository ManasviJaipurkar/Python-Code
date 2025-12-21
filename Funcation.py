# 1. Function Without Parameters

def greet():
    print("Hello all, Welcome to the world")
greet()

# 2. Function With Parameters
def greet(name):
    print("Hello", name)

greet("Manasvi")


# 3. Function With Return Value

def add(a, b):
    return a + b 
result = add(3, 6)
print("The sum of a and b is:  ", result)


def calculate(a, b):
    return a + b, a - b, a * b

sum, diff, prod = calculate(10, 5)
print(sum, diff, prod)


def student(name, age):
    print("Name: ", name)
    print("Age: " , age)
student(name = "Manasvi", age = 22)