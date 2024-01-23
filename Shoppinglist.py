
# empty list where information that user inputs will be stored
list = []
# variable message left blank so that the program has something to check before while loop
message = ""
# flag variable, named active, set to True
# while loop shall run as long as active is True
active = True
# following print statements communicate to the user what program does
print("During this test, you will be asked to add and remove items from a shopping list")
print("If you wish to add items, simply enter 'Add'; to remove an item, enter 'Remove'")
print("If you wish to exit the shopping list, simply type in 'Exit' to do so")
# the code shall be executed continuously while active remains True
while active:
    # message allows the user to interact with program, thus manipulating shopping list
    message = input("Would you like to add items, remove items or exit the application?: ").title()
    # if user enters 'Add', the following code will be executed
    # a combination of if and elif statements allows code to differentiate what user wants to do
    # for this if statement, items will be added to the shopping list
    if message == 'Add':
        # these two print statements again communicate what the user must do
        # note that they are outside of while loop, and so will not be printed continuously
        print("Please add the items you wish to buy. ")
        print("If you wish to stop adding items, please enter 'Quit' to do so. ")
        # variable 'abort' set to 'Quit'. To be used in combination with flag to halt program
        abort = 'Quit'
        # add left blank so code can check something before while loop occurs
        add = ""
        # flag variable, named 'running', set to True. As flag is true, while loop performs
        running = True
        # Here is the code that will be executed as long as running is True
        while running:
            # add variable with input allows user to add what they want
            # data entered by user will be saved to the variable
            add = input("Add an item: ").title()
            # an if statement is used when the user wants to quit the program
            # if the user has entered 'Quit' (saved to variable abort) the following executes
            if add == abort:
                # the flag, named running, is set to False. This discontinues the loop
                running = False
                # a print statement informs user what has been bought
                print("You have the following items in your list thus far: ")
                # a for loop with the enumerate function goes through list to show bought items
                for count, lis in enumerate(list):
                    # f statement used to show the count and the items in the list
                    # once the for loop has finished, user is sent back to message variable
                    print(f'{count}. {lis}')
            # if add doesn't == quit, the following is executed
            else:
                # print statement displays item added to list, so that user knows what's bought
                print(f"Adding {add} to your list. ")
                # every time the user adds an item, it is appended to list with .append(add)
                # note that the use of the else statement means that 'Quit' won't be added to list
                # .append(add) only adds items that are in else statement, and 'Quit' is not
                # the use of this if-else statement prevents a logical error: 'Quit' is not added as item
                list.append(add)
    # an elif statement is used to cover next possible scenario: that the user enters 'Remove'
    # once the user enters 'Remove', the following code is executed
    elif message == 'Remove':
        # the for loop below informs the user about what is currently in the shopping list
        # please note that this is outside of while loop and will not be printed continuously
        print("You currently have the following items in your list: ")
        for count, lis in enumerate(list):
            print(f"{count}. {lis}")
        # the two print statements inform the user about how they remove items and how to quit
        print("Please enter the items that are currently in your list to remove them. ")
        print("If you wish to stop removing items, please enter 'Quit' ")
        # a termination of the code is, again, set as 'Quit' and saved to 'abort' variable
        abort = 'Quit'
        # variable remove set as blank so that program has something to check before while loop
        remove = ""
        # flag set to True
        running = True
        # the following code is executed as long as the flag remains as being True
        while running:
            # how the code functions below is similar to above
            # the only difference being is that in the else statement, .remove() deletes items from list
            remove = input('Select an item to remove: ').title()
            if remove == abort:
                running = False
                print("You have the following items in your list thus far: ")
                for count, lis in enumerate(list):
                    print(f'{count}. {lis}')
            else:
                # the print statement tells the user what is being removed
                print(f'Removing {remove} from your list. ')
                # the .remove() command is used to delete an item from the list
                list.remove(remove)
    # the third possibility is stated here: that the user wishes to quit the program by entering 'Exit'
    elif message == "Exit":
        # the flag designed to keep the while loop running whilst shopping list forms is now set to False
        # by setting the flag to false, the while loop is terminated
        active = False
        # the for loop below loops through the entire list, showing the user what they bought
        # the enumerate() function allows user to see the number of items they bought
        print(f'You have ordered the following items: ')
        for count, lis in enumerate(list):
            print(f'{count}. {lis}')
        # final print statement displays a goodbye message to user
        print("Thank you for shopping with us! ")
    # if the user doesn't input either 'Add', 'Remove' or 'Exit', invalid input is printed
    else:
        print("Invalid Input! ")
