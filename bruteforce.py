#brute_force

import random
import pyautogui

all_input = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()"

all_input_list = list(all_input)

password = pyautogui.password("Enter a password: ")

guess_password = ""

while guess_password != password:
    guess_password = random.choices(all_input_list, k=len(password))

    print("<================>"+ str(guess_password) +"<================>")

    if guess_password == list(password):
        print("Your Password is : "+ "".join(guess_password))
        break
