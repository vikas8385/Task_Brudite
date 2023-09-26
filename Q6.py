number = int(input("Enter a number: "))

 
count = 1
 
for i in range(1, number + 1):
        count *= i

     
print(f"Factorial of {number} is {count}")
