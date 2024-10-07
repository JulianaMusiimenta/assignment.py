# The volume of a sphere with radius r is(4/3)* pie*r**2.
#what is the volume  of the sphere with radius 5.
# make sure the program enters the radius from the keyboard and the answer in 2dps.

def volumOfTrangle():

  radius= int(input ('Enter the radius of the sphere: '))
  pie= int(input('Enter the pie of the sphere: '))

  volume= ((4/3)* pie * r **3)

  print(f" The volume of the sphere radius {radius} and pie {pie} is {volume:.3f}")

  volumOfTrangle()
#2) 
# create a program that calculate the area of a triangle (1/2* base * height).
# base and height should be entered using the keyboard.
# Formula A = 1/2*b*h

def areaofTriangle():

    base = int(input('\nEnter the base of the triangle: '))
    height = int(input('Enter the height of the triangle: '))

    area = (1/2) * base * height 

    print(f"The area of a triangle of base {base} and height {height} is {area:.2f}")

    areaofTriangle()
#3)
# Question one
#WITI has tasked you to automate a simple grading system.
# As a python student , write a program using to display the grades that 
# the student will be receiving based on the mark scored in a subject.
# the grades are:
# 90% -100% Grade is A
# 80% - 89% Grade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50% -59% Grade is E
# < 50% Fail.

def calculateGrades():

    print("\n...student Grade calculations...")

    #capture student mark
    mark = int(input('Enter mark scored:\t'))

    #testing student mark
    if mark>=90 and mark<=100:
        print("Grade is A")

    elif mark>=80 and mark<=89:
        print("Grade is B")

    elif mark>=70 and mark<=79:
        print("Grade is C")

    elif mark>=60 and mark<=69:
        print("Grade is D")

    elif mark>=50 and mark<=59:
        print("Grade is E")

    else:
        print("Fail")

        # call the function
        calculateGrades()

#WITU Acadamy is proposing a sacco to help student save their money. 
#design a platform thst will do the following 
#welcome to, WITU Academy sacco.
# 1. Deposit money
# 2. withdraw money 
#3. check balance 
# Ensure if the student select 1, money is deposited and minimum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdraw is 500.
# If the student selects 3, the acount balance should be displyed.


def saccoTransactions():

    accountBalance = 0
    run = 1

    while run ==1:

        print("\nWelcome to, WITU Academy sacco.")

        #menu
        print('1. Deposit money')
        print('2. withdraw money')
        print('3. check balance')


    studentChoice = int(input("Enter your selection(1,2,3): "))

    #performing the transaction basing on the student selection
    if studentChoice == 1:
        print('\n...processing a deposit transaction...')
    depositAmount = int(input("Enter amount to be deposited: "))

        #check if deposit amount is less than 1000
    if depositAmount < 1000:
        print('\nMinimum deposit is 1000')
    else:
     accountBalance += depositAmount
     print(f"Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:,}")
    if studentChoice == 2:
     print('\n...processing a withdrawing transaction...')
    withdrawAmount = int(input("Enter amount to be withdraw: "))
    if accountBalance ==0:
        print("your balance is 0")
    elif withdrawAmount < 500:
        print("Minimum withdraw amount is 500")
    elif  withdrawAmount > accountBalance:
        print(f"withdraw failed, insufficient funds")
    else:
        accountBalance -= withdrawAmount
        print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new balance is {accountBalance}')
    if studentChoice == 3:
        print(f'Your account balance is {accountBalance:,}')
    else:
     print("you entered a wrong choice !! please select 1,2 or 3\n")
     run = int(print("Enter 1 to continue or ant number to exit: "))
     if run!=1:
        print("Thanks for using our sacco")
    
    
    
    




    



            










         