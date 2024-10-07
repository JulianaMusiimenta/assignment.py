# control flow structure determine the order in which a program can be excuted basing on loops or conditions
#types
#1) conditional statements are statements that execute basing on a particula condition

# create a program that asks a user for the foood type  bought from the market
#the program should print you bought chicken if the user enters chicken
#you bought liver if the user enters liver
# else the program should print fish

food_type =input("Enter food type bought: ").lower()

if food_type == 'chicken':
    print(f"you bought chicken from the market")

if food_type == 'liver':
    print(f"you bought liver from the market")

elif food_type== 'fish':
    print(f"you bought fish from the market")
    
else:
    print(f"you bought fish from the market")
 

