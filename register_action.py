from register import Userregister
import re
import csv
import getpass
import bcrypt
import os
def register():
    name = input("Enter the Full name : ")
    email = input("Enter the email : ")
    if validate_email(email):
        print(f"Your Email is valid....")
    else:
        print(f"Your Email is Invalid !!")
        return
    Password = getpass.getpass("Enter the password (must have atleast 8 characters, 1 Uppercase, 1 lowercase, 1 digit and 1 special character...): ")
    if validate_password(Password):
        password = hash_password(Password)
        cnf = input("Confirm your passowrd : ")
        if Password!=cnf:
            print(f"Password and Confirm password not matched !!")
            return
        else:
            print(f"\n Please ans one of the question which helps you to recover password in future !!\n  What is your nick name \n")
            secret_question = input("Enter your answer for the question : ")
            print(f"\n Answer noted !! \n")
            user=Userregister()
            user.setname(name)
            user.setemail(email)
            user.setpass(password)
            user.setques(secret_question)
            if checkemail(email):
                print(f"User Already registered")
                return
            user.savedata()
    else:
        print(f" Password must have atleast 8 characters, 1 Uppercase, 1 lowercase, 1 digit and 1 special character...")


def validate_password(password):
    if (len(password) >= 8 and
        re.search(r'[a-z]', password) and  
        re.search(r'[A-Z]', password) and  
        re.search(r'[0-9]', password) and    
        re.search(r'[@#$%^&+=]', password)): 
        return True
    else:
        return False

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(email_regex, email):
        return True
    else:
        return False

def checkemail( email):
    os.makedirs(os.path.dirname("C:\\data\\Userdetails.csv"), exist_ok=True)
    try:
        with open("C:\\data\\Userdetails.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            
            for row in csv_reader:
                if email == row[1]:
                    return True 
        return False 
    except FileNotFoundError:
        with open("C:\\data\\Userdetails.csv", mode='w') as file:
            pass
        return False


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')