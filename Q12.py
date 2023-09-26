number=int(input("enter a number"))

digit_sum=0
count=0
while number > 0:
        digit_sum += number % 10
        number //= 10
while digit_sum >0:
    count += digit_sum % 10
    digit_sum //=10
print(count)