#Name:          finalproject.py
#Author:        AJ Varatharajan
#Date Created:  April 5, 2023
#Date Last Modified: April 6, 2023
#Purpose: This program will store an entire student database. Grades, notes, report cards, progress, academic offenses, and status will be all recorded. 
#The database will alert the user if a student is failing. A report card may be generated and saved to a text file named 'reportcard.txt'
#Metric data will also be available in the form of a graph for analysis
class Student:
    def __init__(self, firstname, lastname, studN):
        self.firstname = firstname
        self.lastname = lastname
        self.studN = studN
        
    def info(self):
        info = {"First name": self.firstname,"Last name": self.lastname, "Student number": self.studN}
        print(info)
        return info




userCu = {}
userCp = {}
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
                    
                    userN = input("Enter your username:\n")
                    userP = input("Enter your password:\n")
                    userCu = {"Username": "{}".format(userN)}
                    userCp = {"Password":"{}".format(userP)}
                    
                    continue
                elif logC == 'L' or logC == 'L':
                    userV = input("Enter your username:\n")
                    passV = input("Enter your password:\n")
                    if userV == userCu["Username"] and passV == userCp["Password"]:
                        print("Login succesful!")
                        flag2 = True
                        if flag2 == True:
                            break     
    return  userCu, userCp
def mainmenu():
    selection = int(input("Pick from one of the following options:\n1. Student Profile Creation \n2. Grades \n3. Class Progression Chart \n4. Export Report Card\n"))
    return selection


greeting()
dict = {}
flag3 = False
while (flag3==False):
    mainmenu()
    match mainmenu():
        case 1 :
            print("Student creation:")
            population = input("Enter the number of students in your classroom:\n")
            
            for x in range(0,int(population)):
                x = Student(input(),input(),input())
                dict[x] = x.firstname,x.lastname,x.studN
                print(dict[x])
                
        case 2 :
            search = input("Enter either student name or number")
            print(dict[1])
        case 3 :   
            print("")     
        case 4 :
            print("")
        case _:
            print("invalid response")

 
