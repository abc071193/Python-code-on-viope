The last exercise in this chapter continues with the exercise from the last chapter, the calculator. 
In this exercise, expand the existing code by implementing the following new features: 
(A) Calculator does not automatically quit when the result is given, allowing user to do new calculations. 
The user has to select "6" in the menu to exit the program. 
(B) The calculator shows the selected numbers in the main menu by printing "Current numbers:" and the user-given input. 
By selecting "5" in the calculator menu, the user can change the given numbers. 
print("Calculator")
keepgoing = True
while True:
    if keepgoing:
        value_1 = input("Give the first number: ")
        value_2 = input("Give the second number: ")
        keepgoing = False
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) Change numbers\n(6) Quit")
    print("Current numbers:",value_1, value_2)
    value_3 = int(input("Please select something (1-6): "))

    if int(value_3) == 1:
        print("The result is:",int(value_1) + int(value_2))
    elif int(value_3) == 2:
        print("The result is:",int(value_1) - int(value_2))
    elif int(value_3) == 3:
        print("The result is:",int(value_1) * int(value_2))
    elif int(value_3) == 4:
        print("The result is:",int(value_1) / int(value_2))
    elif int(value_3) == 5:
        keepgoing = True
    elif int(value_3) == 6:
        print("Thank you!")
        break
    else:
        print("Selection was not correct")
