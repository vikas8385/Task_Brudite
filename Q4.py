first_number =int(input("Enter first number"))
second_number=int(input("Enter second number"))
count=0
for i in range(first_number,second_number):
    if i % 2 ==1:
        count += i
print(count)