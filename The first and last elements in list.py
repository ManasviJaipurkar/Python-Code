user= (input("Enter the numbers seperated by comma(,): "))
number_list = [int(i)for i in user.split(',')]
print(number_list)
new_list = [number_list[0]] + [number_list[-1]]
print("The first and last elements in list is", new_list)
