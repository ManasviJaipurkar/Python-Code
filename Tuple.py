# 1. Creating a Tuple
t1 = (1, 2, 3)
print(t1)

# 2. Tuple with Different Data Types
t2 = (1, "Python", 3.5, True)
print(t2)


# 3 Single-Element Tuple
t3 = (5,)
print(type(t3))


# 4 Access Tuple Elements
t = (10, 20, 30, 40)

print(t[0])    # First element
print(t[-1])   # Last element

# 5 Tuple Slicing
t = (1, 2, 3, 4, 5)

print(t[1:4])
print(t[:3])
print(t[::2])

# 6 Tuple Operations
t1 = (1, 2, 3)
t2 = (4, 5)

print(t1 + t2)    # Concatenation
print(t1 * 2)     # Repetition