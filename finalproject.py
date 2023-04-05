#Name:          finalproject.py
#Author:        AJ Varatharajan
#Date Created:  April 5, 2023
#Date Last Modified: April 6, 2023
#Purpose: This program will store an entire student database. Grades, notes, report cards, progress, academic offenses, and status will be all recorded. 
#The database will alert the user if a student is failing. A report card may be generated and saved to a text file named 'reportcard.txt'
#Metric data will also be available in the form of a graph for analysis

def greeting():
    print("Welcome to the Conestoga Student DataBase, only permited staff members may access this database!")
    flag1 = False
    while (flag1 == False):
        try:
            logQ = input("Are you ready to log in?")
            if logQ.isdecimal():
                raise ValueError
            elif logQ == "no" or logQ == "No" or logQ == "N" or logQ == "n":
                exit()
                break
            elif logQ == "yes" or logQ == "Yes" or logQ == "Y" or logQ == "y":
                flag1 = True
                if flag1 == True:
                    break
        except ValueError:
            print("Please enter Yes or No")
        finally:
            flag2 = False
            while (flag2 == False):
                logC = input("Enter 'L' to login or if you do not have an account type in 'C' to create a new account ")
                if logC == 'C' or logC == 'c':
                    userC = {}
                    userN = input("Enter your username:\n")
                    userP = input("Enter your password:\n")
                    userC = {"Username": "{}","Password":"{}".format(userN,userP)}
                    continue
                elif logC == 'L' or logC == 'L':
                    userV = input("Enter your username:\n")
                    passV = input("Enter your password:\n")
                    if userV == userC["Username"] and passV == userC["Password"]:
                        print("Login succesful!")
                        break
            
    return userN, userP, userC



greeting()


