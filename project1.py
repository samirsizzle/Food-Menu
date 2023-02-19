def menu(my_list): # Creates the function
    """
    This function chooses a selected item from a list
    """
    my_list = ["Pizza", "Cheeseburger", "Mac n Cheese"]
    return my_list

# Call for the function
Anotherlist = ["Pizza", "Cheeseburger", "Mac n Cheese"]
casefold_list = [food.lower() for food in Anotherlist]
print(Anotherlist)
while True:
    food = input("What will you like to eat today :") 
    if food.lower() == 'p': # If we input capital "P" or lowercase "p",(lower.()) it will stop the stop the function (break)
        break
    elif food in Anotherlist:
       print("Okay! One "  + food)
    elif food in casefold_list:
        print("Okay! One " + food)
    else: 
        print("Sorry, we do not have that on the menu") 
