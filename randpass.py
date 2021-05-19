import string
import random
import csv
import time

symbols = ['*', '%', '£']  # Can add more
passlist = [ ]
for i in range(10):
    password = ""
    for lngth in range(15):
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(symbols)
        print(password)
        if lngth >= 10:
            passlist.append(password)
            with open('randpass.csv', mode='a') as file_:
                file_.write(password)
                file_.write("\n")
