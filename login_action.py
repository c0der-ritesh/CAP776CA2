from login import Userlogin
from register import Userregister
from register_action import validate_password, hash_password, checkemail
from Dashboard_action import dashboard
import time
import random
import string
import csv
import msvcrt
import os
from datetime import datetime

wrong_cred_count=0
def logout():
    pass

def action():
    global wrong_cred_count
    email = input("Enter your email : ")
    print(f"Enter your password (must have atleast 8 characters, 1 Uppercase, 1 lowercase, 1 digit and 1 special character...) : ")
    password = masked_input()
    cap = generate_random_string()
    l = strikethrough(cap)      
    print(f"\n {l} \n")
    captcha = input("Enter the given captcha : ")
    if captcha == cap:
        ulogin = Userlogin()
        ulogin.setemail(email)
        ulogin.setpass(password)
        time.sleep(1)
        if ulogin.checkcred():
            print("logged in successfull !")
            # with open("C:\\data\\Userdetails.csv", mode='r') as file:
            #     reader = list(csv.reader(file))
            # current_datetime = datetime.now()
            # updated_rows=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            # with open("C:\\data\\Userdetails.csv", mode='a') as file:
            #     writer = csv.writer(file)
            #     writer.writerow([updated_rows])
            current_datetime = datetime.now()
            login_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            log_login(email, login_time)
            time.sleep(2)
            os.system('cls')
            dashboard(email)
            current_datetime = datetime.now()
            logout_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            log_logout(email, logout_time)
        else:
            print("wrong credentials...")
            wrong_cred_count+=1
            print(f"attempt remaining {5-wrong_cred_count}")
    else:
        print(f"\n Wrong Captcha please try again... \n")
        return


def log_login(email, login_time):
    with open("log.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, login_time, ''])  # Log login with an empty logout time initially


# Function to update the logout time in the CSV file
def log_logout(email, logout_time):
    rows = []

    # Read all rows from the CSV file
    with open("log.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Update the logout time for the last login entry of this email
    for row in rows[::-1]:  # Reverse to find the last login faster
        if row[0] == email and row[2] == '':  # Find the entry with no logout time
            row[2] = logout_time
            break

    # Write the updated rows back to the CSV file
    with open("log.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)




def login():
    global wrong_cred_count
    if wrong_cred_count<5:
        print(f" 1. Enter your Credentials :\n 2. Forgot Password ?")
        ch = input("Enter your response : ")
        if ch=='1':
            action()
        elif ch=='2':
            forgot()
        else :
            print("Invalid response !")
    else:
        print(f"\n You Exceeded maximum number of wrong attempts kindly wait.....")

def forgot():
    n = input("Enter the email : ")
    if checkemail(n):
        print(f"\n Enter the security question's answer : ")
        ans = input()
        if checksec(ans,n):
            time.sleep(2)
            print(f" verified !!")
            update()
        else:
            print(f" wrong answer try again !!")
    else:
        print(f" No user found for {n} email address !!")
    


def update():
    email = input("enter your email : ")
    if checkemail(email):
        print(f"Enter your password (must have atleast 8 characters, 1 Uppercase, 1 lowercase, 1 digit and 1 special character...) : ")
        Password = masked_input()
        if validate_password(Password):
            password = hash_password(Password)
            cnf = input("Confirm your passowrd : ")
            if Password!=cnf:
                print(f" Password and Confirm password not matched !!")
                return
            log = Userregister()
            if(log.updatepass(email,password)):
                print(f" Password Updated for user {email}")
            else:
                print(f" Password not updated !!")
    else:
        print(f" No user found for {email} email address !!")

def checksec(ans,email):
        with open("C:\\data\\Userdetails.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if email == row[1] and ans == row[3]:
                    return True 
            return False 


def generate_random_string(length=5):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def strikethrough(text):
    return ''.join(char + '\u0336' for char in text)

def masked_input(prompt=''):
    print(prompt, end='', flush=True)  # Display prompt
    password = ''
    
    while True:
        char = msvcrt.getch()
        if char in (b'\r', b'\n'): 
            print()  
            break
        elif char == b'\x08': 
            password = password[:-1] 
            print('\b \b', end='', flush=True) 
        else:
            password += char.decode() 
            print('*', end='', flush=True) 
    
    return password

    