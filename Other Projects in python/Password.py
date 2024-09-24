#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

num_count = 0
symbols_count = 0
letters_count = 0
PW = []

while letters_count < nr_letters:
    PW += random.choices(letters)
    letters_count += 1
while symbols_count < nr_symbols:
    PW += random.choices(symbols)
    symbols_count += 1
while num_count < nr_numbers:
    PW += random.choices(numbers)
    num_count += 1

PW = ''.join(random.sample(PW,len(PW)))

#print(f"This is your new password: " {PW})
print(PW)