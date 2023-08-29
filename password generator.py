
# Author - Abhiraj Singh
# Task - Password Generator


import random
import string
print(' Welcome to Password generator!')
length = int(input('\nEnter the length of password: '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = upper +  lower+ symbols +  num
temp = random.sample(all,length)
password = "".join(temp)
print(password)
