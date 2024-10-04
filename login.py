import re
import csv
import getpass
import bcrypt
import os

class Userlogin:
    def __init__(self):
        self._email=""
        self.__password=""
    def setemail(self,email):
        self._email=email
    def setpass(self,password):
        self.__password=password
    def getemail(self):
        return self._email
    def check_password(self,hashed: str, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    def checkcred(self): 
        os.makedirs(os.path.dirname("C:\\data\\Userdetails.csv"), exist_ok=True)
        try:
            with open("C:\\data\\Userdetails.csv", mode='r') as file:
                csv_reader = csv.reader(file)
                
                for row in csv_reader:
                    if self._email == row[1] and self.check_password(row[2],self.__password):
                        return True 
                return False 
        except FileNotFoundError:
            with open("C:\\data\\Userdetails.csv", mode='w') as file:
                pass
            return False
