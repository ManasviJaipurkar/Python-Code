num = int(input("Enter the number: "))
if num <= 1:
    print(f"The {num} number is not Prime ")
    
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:  # Note: This else belongs to the FOR loop, not the IF statement
        print("Prime")
else:
    print("Not prime")  # Numbers <= 1 are not prime