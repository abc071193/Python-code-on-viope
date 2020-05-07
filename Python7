The third exercise in the chapter continues with the calculator exercises done earlier. 
This time the idea is to finally take out the annoying problems with numbers, 
input validity and the stability problems caused by type conversion funvtion.
Make the following changes to the calculator: 
Every time the user gives numbers to the program, the system asks for the numbers with the prompt "Give a number: " and 
continues until a valid number is given. If the number is not correct, the system gives an error message "This input is invalid.".
import math
           

def getnum():
    while True:
        try:
            num=int(input("Give a number: "))
            return num
        except Exception:
            print("This input is invalid.")
        
def main():
    print("Calculator")
    number1=getnum()
    number2=getnum()
    number1=int(number1) #type conversion
    number2=int(number2) #type conversion
        

    while True:
            print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n\
(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
            print("Current numbers:",number1,number2)
            selection = int(input("Please select something (1-6): "))
            if selection == 1:
                print("The result is:", number1+number2)
            elif selection == 2:
                print("The result is:", number1-number2)
            elif selection == 3:
                print("The result is:", number1*number2)
            elif selection == 4:
                print("The result is:", number1/number2)
            elif selection == 5:
                print("The result is:", math.sin(number1/number2))
            elif selection == 6:
                print("The result is:", math.cos(number1/number2))
            elif selection == 7:
                number1 = getnum()
                number2 = getnum()
            elif selection == 8:
                print("Thank you!")
                break
if __name__=="__main__":
    main()
