input_string = input("Enter a string: ")
num_number = 0
num_alph = 0
 
for char in input_string:
     
    if char.isdigit():
        num_number += 1
    
    elif char.isalpha():
        num_alph += 1
print(f"Number of letters: {num_alph}")
print(f"Number of digits: {num_number}")
