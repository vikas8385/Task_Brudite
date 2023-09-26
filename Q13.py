number = int(input("enter a number"))
count=0
while number > 0:
    count = number %10
     
    print(count,end="")
    number //=10