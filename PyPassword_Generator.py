# PyPassword Generator

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the password Generator!")
length = int(input("How long of a password do you need? "))

password = ""
for i in range(1,length+1):
    char = random.choice(letters)
    password += char
    sym = random.choice(symbols)
    password += sym
    no = random.choice(numbers)
    password+= no

print(password)