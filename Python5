This exercise expands on the calculator, which was made in chapter 4, exercise 4. 
In this exercise, add sin() and cos() -calculations from the library module math to the calculator. 
Add these actions as selections 5 and 6, simultaneously moving the "change numbers" feature to 7 and "Quit" to 8. 
When the user calls either of the new features, the first number is the divident and second the divider like this: sin(number_1/number2).
import math
print("Calculator")
keepgoing = True
while True:
    if keepgoing:
        value_1 = input("Give the first number: ")
        value_2 = input("Give the second number: ")
        keepgoing = False
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7) Change numbers\n(8) Quit")
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
        print("The result is:",math.sin(int(value_1)/int(value_2)))
    elif int(value_3) == 6:
        print("The result is:",math.cos(int(value_1)/int(value_2)))
    elif int(value_3) == 7:
        keepgoing = True
    elif int(value_3) == 8:
        print("Thank you!")
        break
    else:
        print("Selection was not correct")
