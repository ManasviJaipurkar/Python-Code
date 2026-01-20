import math
def f(x):
    return math.cos(x)
x = 0.5

for i in range(10):
    x_new = f(x)
    print(f"step{i+1} : x ={x}")
    x = x_new
    diff = x_new - x
    print(diff)

print(f"After 10 steps: x~~ {x}")
print(f"Check cos({x}) = {math.cos(x)}") 

diff = x_new - x
print(diff)