#Name:          finalproject.py
#Author:        AJ Varatharajan
#Date Created:  April 5, 2023
#Date Last Modified: April 8, 2023
#Purpose: This program will store an entire student database. Grades, notes, report cards, progress, academic offenses, and status will be all recorded. 
#The database will alert the user if a student is failing. A report card may be generated and saved to a text file named 'reportcard.txt'
#Metric data will also be available in the form of a graph for analysis



userCu = {}
student = {}
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
#Main Body
#greeting()
final = {}
dict = {}
dict2 = {}
flag3 = False
flag4 = False
while (flag3==False):
    mainmenu()#Calling main menu
    match mainmenu(): #Matching input using switch case selection
        case 1 :
            print("Student creation - Add students at anytime without any overwriting.")
            population = input("Enter the number of students in your classroom:\n")
            for x in range(0,int(population)):
                student[x+1] = {}
                firstname = input("Enter first name:")
                lastname = input("Enter last name")
                student[x+1] = {"Firstname": firstname, "Lastname":lastname}
            print(student.items())   
            continue    
        case 2 :           
            gradeM = int(input("Enter the student number associated with student you would like to review:\n"))
            classSel = int(input("Enter the course you wish to modify the grade for student {} {} : \n 1. PROG1783\n 2. INFO1145\n 3. INFO1385\n".format((student[gradeM]['Firstname']),(student[gradeM]['Lastname']))))
            if classSel == 1:
                gradeEntry = input("Enter the PROG1783 grade value:\n")
                student[gradeM]['PROG1783'] = int(gradeEntry) 

            elif classSel == 2:
                gradeEntry = input("Enter the INFO1145 grade value:\n")
                student[gradeM]['INFO1145'] = int(gradeEntry) 
            
            elif classSel == 3:
                gradeEntry = input("Enter the INFO1385 grade value:\n")
                student[gradeM]['1385'] = int(gradeEntry) 
            elif classSel == 4:
                print(student.items())
                print(student)       
        case 3 :   
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

 
