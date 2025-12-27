# 1.Creating a Set
s1 = {1, 2, 3, 4}
print(s1)

# 2 Set with Duplicate Elements (Automatically Removed)
s2 = {1, 2, 2, 3, 3, 4}
print(s2)

# 3 Create an Empty Set 
empty_set = set()
print(type(empty_set))

# 4  Add Elements to a Set
s = {1, 2, 3}
s.add(4)
print(s)

# 5 Add Multiple Elements
s.update([5, 6, 7])
print(s)

# 6 Remove Elements
s = {1, 2, 3, 4}

s.remove(3)      
s.discard(10)    
print(s)