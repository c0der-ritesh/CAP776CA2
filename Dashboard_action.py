#from Dashboard import Userdashboard
from APImodule import mainApicall
from login import Userlogin
import csv
def dashboard(email):
    print("-"*20)
    name = getusername(email)
    print(f"\n Welcome, {name}")
    print(f"\n ")
    mainApicall()


def getusername(email):
    with open("C:\\data\\Userdetails.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if email == row[1]:
                    name = row[0]
                    return name 