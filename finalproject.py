#Name:          finalproject.py
#Author:        AJ Varatharajan
#Date Created:  April 5, 2023
#Date Last Modified: April 8, 2023
#Purpose: This program will store an entire student database. Grades, notes, report cards are recorded. 
#A report card may be generated and saved to a text file named 'reportcard.txt'
#Metric data will also be available in the form of a graph for analysis

import matplotlib.pyplot as plt #importing matplotlib.pyplot module 
import os #importing OS module 
 #intializing empty dictionary
student = {} #intializing empty dictionary
 #intializing empty dictionary
def greeting(): #login function
    print("Welcome to the Conestoga Student DataBase, only permited staff members may access this database!")
    flag1 = False
    while (flag1 == False):
        try: #try block for potential value error
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
        except ValueError: #exception block
            print("Please enter Yes or No")
        finally: #Final block, code will run regardless.
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
def mainmenu(): #main menu function
    selection = int(input("Pick from one of the following options:\n1. Create New Classroom \n2. Grades \n3. Class Progression Chart \n4. Export Report Card\n5.Enrollment Management\n6. Quit\n"))
    return selection
#Main Body
greeting()
final = {}
dict = {}
dict2 = {}
flag3 = False
flag4 = False
while (flag3==False):
    selection = int(input("Pick from one of the following options:\n1. Create New Classroom \n2. Grades \n3. Class Progression Chart \n4. Export Report Card\n5. Enrollment Management\n6. Quit\n"))
    match selection: #Matching input using switch case selection
        case 1 :
            print("Student creation - Student database will be subject to overwriting.")
            population = input("Enter the number of students in your classroom:\n")
            for x in range(0,int(population)): #using for loop to create students based on size of classroom obtained from user input in variable population
                student[x+1] = {} #intializing empty nested entry
                firstname = input("Enter first name:")
                lastname = input("Enter last name")
                student[x+1] = {"Firstname": firstname, "Lastname":lastname} #assigning user input to nested dictionary for each unique student
            print(student.items())   
            continue    
        case 2 :           
            gradeM = int(input("Enter the student number associated with student you would like to review:\n"))
            classSel = int(input("Enter the course you wish to modify the grade for student {} {} : \n 1. PROG1783\n 2. INFO1145\n 3. INFO1385\n".format((student[gradeM]['Firstname']),(student[gradeM]['Lastname'])))) #user input to determine which course will be modified for specific user obtained from accessing dictionary key
            if classSel == 1:
                gradeEntry = input("Enter the PROG1783 grade value:\n")
                student[gradeM]['PROG1783'] = int(gradeEntry) 

            elif classSel == 2:
                gradeEntry = input("Enter the INFO1145 grade value:\n")
                student[gradeM]['INFO1145'] = int(gradeEntry) 
            
            elif classSel == 3:
                gradeEntry = input("Enter the INFO1385 grade value:\n")
                student[gradeM]['INFO1385'] = int(gradeEntry) 
            elif classSel == 4:
                print(student.items())
                print(student)       
        case 3 :   
            gradeG = int(input("Enter the student number associated with student you would like to generate a graph for:\n"))
            left = [1,2,3] #creating bar for each course
            height = [student[gradeG]['PROG1783'],student[gradeG]['INFO1145'],student[gradeG]['INFO1385']] #hieght values obtained from values in dictionary for each course
            tick_label = ['PROG1783','INFO1145','INFO1385'] #labeling each bar
            plt.bar(left, height, tick_label = tick_label,width = 0.8, color = ['red', 'green' , 'blue']) #customizing graph for each variable
            plt.xlabel('Course') #x-axis label
            plt.ylabel('Grade %')#y-axis label
            plt.title("Progress Report: " + student[gradeG]['Firstname'] + " " + student[gradeG]['Lastname']) #Graph title
            plt.show() #calling graph to be displayed
        case 4 :
            confirmR = input("Are you sure you want to export a report card for all students?\n")
            if confirmR == 'Y':
             newFile = open("reportcard.txt", 'w')    #creating 'reportcard.txt' file for writing 
             
            newFile.write("Student List: ")
                
            newFile.write('\n')
            for x,p in (student.items()): #looping through dictionary
                newFile.write("Student # ")
                newFile.write("{}\t{}\n".format(str(x),str(p))) #writing each dictionary item to 'reportcard.txt' file
            newFile.close() #closing file as per good I/O practice
            print("The summary txt file has been succesfully written to ", os.getcwd()) #Displaying file pathway
            print("File name: ", newFile) #displaying file name

        case 5 :
            print("Enrollment management:")
            choice = int(input("1. Delete Student\n2. Add Student\n3. Exit to main menu\n:"))
            if choice == 1:
                searchD = int(input("Enter the student number associated with student you would like to delete:\n"))
                confirmD = input("Are you sure you want to delete {} {}".format(student[searchD]['Firstname'],student[searchD]['Lastname'])) #confirmation to delete, reminding user with specified user name to be deleted.
                if confirmD == 'Y':
                    del student[searchD] #utilizing dictionary key to delete entry, obtained from user input
                    mainmenu()
                elif confirmD == 'N':
                    pass
            elif choice == 2:    
                student[int(len(student))+1] = {}
                firstnameC = input("Enter first name:")
                lastnameC = input("Enter last name")
                student[int(len(student))+1] = {"Firstname": firstnameC, "Lastname":lastnameC}#writing each dictionary value
                print(student.items())
                mainmenu()
            elif choice == 3:
                mainmenu()    
        case 6 :
            exit()
            break
        case _:
            print("invalid response")

 
