import string
import random

symbols = ['*', '%', '£'] # Can add more

for i in range(100):
        time.sleep(1)
	password = ""
	for _ in range(9):
	    password += random.choice(string.ascii_lowercase)
	password += random.choice(string.ascii_uppercase)
	password += random.choice(string.digits)
	password += random.choice(symbols)
	print(password)
