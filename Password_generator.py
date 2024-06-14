import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '_', '-']

print("Welcome to Password Generator! \n")

options = input("Choose password complexity:\n1. Easy\n2. Hard\nEnter the corresponding number: ")

while options not in ['1', '2']:
    print("Invalid input. Please enter 1 for Easy or 2 for Hard.")
    options = input("Choose password complexity:\n1. Easy\n2. Hard\nEnter the corresponding number: ")

easy_password = options == '1'

length = 12
n_letters = random.randint(1, length - 2)
n_symbols = random.randint(1, length - n_letters - 1)
n_numbers = length - n_letters - n_symbols

password_list = []

for _ in range(n_letters):
    password_list.append(random.choice(letters))

for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

for _ in range(n_numbers):
    password_list.append(random.choice(numbers))

if not easy_password:
    random.shuffle(password_list)

password = ""
for i in password_list:
    password+=i
print(password)
