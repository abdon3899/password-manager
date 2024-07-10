
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'נ', 'K', 'L',
           'M', 'N', '0', 'P', 'Q', 'R', 'S', 'T', '', '', 'w', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




def generate_password():
    password = []
    for char in range(random.randint(8,10)):
        random_char=random.choice(letters)
        password+=random_char

    for numm in range(random.randint(2,4)):
        random_num=random.choice(numbers)
        password+=random_num

    for symm in range(random.randint(2,4)):
        random_sym=random.choice(symbols)
        password+=random_sym

    random.shuffle(password)
    passwordd = ""
    for char in range(1, len(password)):
        passwordd += password[char]

    return passwordd

#
# a=generate_password()
#
# print(f"your password is {a}")