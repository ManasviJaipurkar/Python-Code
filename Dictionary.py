data = { "name": "Manasvi", "age": 22 }
print(data)

d1 = {1: 'manasvi', 2: 'A', 3: 'M'}
print(d1)

# using dict() constructor
d2 = dict(a = "M", b = "A", c = "M")
print(d2)


d = { "name": "M", 1: "Python", (1, 2): [1,2,45] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))

#Adding and Updating Dictionary Items
d = {1: 'MANASVI', 2: 'M', 3: 'A'}
# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"
print(d)