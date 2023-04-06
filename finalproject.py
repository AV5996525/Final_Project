#Name:          finalproject.py
#Author:        AJ Varatharajan
#Date Created:  April 5, 2023
#Date Last Modified: April 8, 2023
#Purpose: This program will store an entire student database. Grades, notes, report cards, progress, academic offenses, and status will be all recorded. 
#The database will alert the user if a student is failing. A report card may be generated and saved to a text file named 'reportcard.txt'
#Metric data will also be available in the form of a graph for analysis

class Student:
    def __init__(self, firstname, lastname, studN):
        self.firstname = firstname
        self.lastname = lastname
        self.studN = studN
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
    selection = int(input("Pick from one of the following options:\n1. Student Profile Creation \n2. Grades \n3. Class Progression Chart \n4. Export Report Card\n5.Enrollment Management\n6.Quit\n"))
    return selection
P = ("Programming",)
#Main Body
greeting()
dict = {}
dict2 = {}
flag3 = False
while (flag3==False):
    mainmenu()#Calling main menu
    match mainmenu(): #Matching input using switch case selection
        case 1 :
            print("Student creation - Add students at anytime without any overwriting.")
            population = input("Enter the number of students in your classroom:\n")
            
            for x in range(0,int(population)):
                x = Student(input(),input(),input())
                
                print(x)
                dict[x] = x.firstname,x.lastname,x.studN
                print(dict[x])
            for x,y in zip(range(len(dict)),dict.values()):
                dict2[x+1] = y          
        case 2 :
            #Make exeption to prevent user from accesing grades w/o making student list
            #print(dict2)
            #print(dict2.keys())
            #print(dict2.values())
            gradeM = input("Enter the student number associated with student you would like to review:\n")
            for x,y in dict2.items():
                if x == int(gradeM):
                    fHolder = y[0]
                    lHolder = y[1]
            classSel = input("Enter the course you wish to modify the grade for student {} {} : \n 1. PROG1783\n 2. INFO1145\n 3. INFO1385\n".format(fHolder,lHolder))
            for x,y in dict2.items():
                if x == int(gradeM):
                    qq = ("{}".format(classSel),)
                    mm = ("PROG1783",)
                    qq += mm
                    zz = tuple(zip(qq[:-1], qq[1:]))
                    y += zz
                    #y += P
                    print(y)
            print(dict2.items())           
        case 3 :   
            #for x,y in dict2.items():
                #print(x)
                #print(y[2])
                #for z in y:
                    #print(y[int(gradeM)])
                    #print(z[int(gradeM)])
            #for k, v in dict2.items():
                #if v[2] == 2:
                     #print(k)
            
                #for z in y:
                    #print(y[int(gradeM)])
                    #print(z[int(gradeM)])         
            print("")     
        case 4 :
            print("")
        case 5 :
            print("Enrollment management:")
        case 6 :
            exit()
            break
        case _:
            print("invalid response")

 
