import os
import time
import sys
from faker import Faker

# Requrments
os.system("pip install faker")

fake = Faker()

def Cacafire():
    os.system('pkg install cacafire')
    os.system('cacafire')

def Cmatrix():
    os.system('pkg install cmatrix')
    os.system('cmatrix')

def Calculater():
    first = int(input(f"{yello}Enter Your First Number\ntype: "))
    operater = input(f"{pink}Enter Operater (+, *, -, /, %, //, **)")
    second = int(input(f"{blue}Enter Second Number\ntype: "))
    if operater == "+":
        print(f"{green}{first} + {second} = {first+second}")
    elif operater == "-":
        print(f"{green}{first} - {second} = {first-second}")
    elif operater == "*":
        print(f"{green}{first} * {second} = {first*second}")
    elif operater == "/":
        print(f"{green}{first} / {second} = {first/second}")
    elif operater == "%":
        print(f"{green}{first} % {second} = {first%second}")
    elif operater == "//":
        print(f"{green}{first} // {second} = {first//second}")
    elif operater == "**":
        print(f"{green}{first} ** {second} = {first**second}")
    else:
        exit()

def Create_Fake_Email():
    email = fake.email()
    return email

def Create_Password():
    password = fake.password()
    return password

if __name__=="__main__":
    
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    blue = "\033[1;34m"
    pink = "\033[1;35m"
    cyan = "\033[1;36m"
    print(f"""{pink}.-. . . . .   .-. .-. .-. .   .-. 
{yellow}|-  | | |\|    |  | | | | |   `-. 
{green}'   `-' ' `    '  `-' `-' `-' `-' 
{red}>>>>>>Created by Shahzaib<<<<<<""")
    user_input = input(f"""
{cyan}[1] Cacafire
{blue}[2] Cmatrix
{green}[3] Calculater
{pink}[4] Fake Email
{red}[5] Password
{yellow}[E] Exit

{blue}type: """)
    if user_input == "1":
        Cacafire()
    elif user_input == "2":
        Calculater()
    elif user_input == "3":
        Cmatrix()
    elif user_input == "4":
        print(pink, Create_Fake_Email())
    elif user_input == "5":
        print(green, Create_Password())
    elif user_input == "E":
        goodbymsg = f"\n{green}Thanks For Using my Fun Tool if You have any doubt then plz Contact the Doveloper"
        for i in goodbymsg:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
    else:
        exit()
