number = int(input("Enter a number"))
count=0
for i in range(1,number):
    if(number % i==0):
        count=count+i
if(count == number):
    print("Number is perfect")
else:
    print("Number is not perfect")