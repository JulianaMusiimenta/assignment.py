#write a programme that takes two numbers input and displays there sum,differen,product and quotient
# number_one= int(input('enter the first number: '))
# number_two= int(input('enter the second number: '))
# sum= number_one + number_two
# print(f"The sum of {number_one} and {number_two} is : {sum}")
# difference= number_one - number_two
# print(f"The difference of {number_one} and {number_two} is : {difference}")
# product= number_one * number_two
# print(f"The product of {number_one} and {number_two} is : {product}")
# quotient= number_one / number_two
# print(f"The quotient of {number_one} and {number_two} is : {quotient}")
# modulus= number_one % number_two
# print(f"The modulus of {number_one}  and {number_two} is : {modulus}")
# floor_division = number_one // number_two
# print(f"The floor_division of {number_one} and {number_two} is {floor_division}")
#write a programme that compare two intergers and prints whether the first number is greator,less than or equal to the second  number
#2)comparision operators(use of if loop) 
#a)greater than(>)(9>2)=true
#b)less than (<)(9<2)=false
#c)equual to (==)(9==2)=false
#d)not equal to(!=)(9!=2)=true
#if loops(commenting the comparision whether its true or false)
# if number_one > number_two :
#     print(f" {number_one} is greator than {number_two}")
# elif number_one < number_two :
#     print(f" {number_one} is less than {number_two}")
# else:
#     print(f"They are equal")
 #write a program that checks if a given number is btn 10 and 20 where by 20 inclusive using logical operation
# number = int(input("enter the number: "))
# if 10 < number <= 20 :
#     print (f"{number} is between 10 and 20")
#     print(f"{number}is not between 10 and 20")
#write  a programme that print squires of all intergers from 1-10 using a loop 
# for i in range (1,11):
#      print(i**2)
#write a simple programme that asks the user for their ae if the age is greater or equal to 18, print adult and qualified else less than 18, print not qualifies
# name = input("enter your name:")
# age = input("enter your age:")
# print(f"hi, {name}! you are an adult. you are qualified")
# print(f"hi, {name}! you are not an adult. you are not qualified")
# we have the following stdents details and marks. enter these details from the keyboard
#student name= Ritah
#student number = SEP23/BCS/14
# programming = 78
#data science =89
 #computer application =55
 #calculate the average marks and print the answer in 3dp
student_name = int(input("enter students name: "))
student_number = int(input("enter students number: "))
programming = int(input("Enter programming mark: "))
data_science = int(input("Enter data science mark: "))
computer_application = int(input("Enter computer application mark :"))
total = (programming + data_science + computer_application)
number_of_course_unit =3
average=(total/number_of_course_unit)
print(f"average mark : {average: .3f}")
 #write a programme tha converts celicius temp to forenheight the programme should ask the user to enter the temp in degree celicious and then display the temp converted to foreinheight
celicius=float(input("enter the temperature in forenheight"))
forenheight=(celicius * 9/5) +32
print(f"{celicius} degrees celicius is equal to {forenheight: .2f}")
 #a car's miles per gallaton can be calculated with the following formula
 #a) write the programme that ask the user for the number of miles driven and gallons used and displays the volume . it should calculate the car's miles-per-gallons used and displays the results.
 #MPG=milesdriven/gallon of gas used
miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons of gas used: "))
mpg =miles_driven
print(f"the car's miles per gallon(mpg) is :{mpg:.2f}")