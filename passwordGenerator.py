import random
import os

charsToUse = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/*-+!£$%^&*&[]#.,;`"

def randomChoices(times):
    password = ''.join([random.choice(charsToUse) for i in range(times)])
    return password

saved = input(f"Would you like to save the password to {os.getcwd()}\\pass.txt? (y/N) ")
times = int(input("How long would you like the password to be? "))
password = randomChoices(times)

if saved == "y":
    passwordName = input("What would you like the password name to be? ")
    f = open(os.getcwd() + "\\pass.txt", "a")
    f.write(f"{passwordName}: {password}\n")