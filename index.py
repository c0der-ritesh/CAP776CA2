from register_action import register
from login_action import login
from Dashboard_action import dashboard
import time
import os
def message():
    print("*"*50)
    print(f"Welcome to the Gaming Era Console Application By- Ritesh Kumar")
    print(f"\n 1. User Registration \n 2. Already registered? Login from Here \n 3. Exit the menu \n ")

while(1):
    time.sleep(2)
    os.system('cls')
    message()
    ch = input("Enter your choice : ")
    match ch:

        case '1':
            os.system('cls')
            register()
        case '2':
            os.system('cls')
            login()
        case '3':
            break
        case _:
            print(f" Please, Enter the valid choice! ")
