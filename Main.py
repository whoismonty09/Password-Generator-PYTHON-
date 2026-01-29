import random
import string

print("🔐 Welcome to Password Generator developed be Monty")

length = int(input("Enter the length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your generated password is:", password)
