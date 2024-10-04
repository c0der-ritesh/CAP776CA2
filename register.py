import csv
import os
class Userregister:
    def __init__(self):
        self.__name=""
        self.__email=""
        self.__password=""
        self.__sq=""
    def setname(self,name):
        self.__name=name
    def setemail(self,email):
        self.__email=email
    def setpass(self,password):
        self.__password=password
    def setques(self,ques):
        self.__sq=ques
    def savedata(self):
         with open("C:\\data\\Userdetails.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.__name, self.__email, self.__password, self.__sq])
         print(f"\n User registered successfully!")

    def updatepass(self, email, new_password):
        updated_rows = []
        user_found = False
        if os.path.exists("C:\\data\\Userdetails.csv"):
            with open("C:\\data\\Userdetails.csv", mode='r') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if row[1] == email: 
                        row[2] = new_password  
                        user_found = True
                    updated_rows.append(row)
        with open("C:\\data\\Userdetails.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        if user_found:
            return True
        else:
            return False