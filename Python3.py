The last exercise in this chapter extends the previous exercise, but it is also possible to make it completely independently. 
Modify the function tester so that, besides testing if the length of the given string is more than ten characters, it also tests if there is the character "X" (capital X) in the given string. 
If the string is longer than 10 characters and it has X in it, the tester subfunction returns a value True to the main function, otherwise False.
def tester(givenstring):
    if len(givenstring) < 10:
        print("Too short")
    
    else:
        if givenstring.find('X') == -1:
            print(givenstring)
            return False
        elif givenstring.find('X') != -1:
            print(givenstring)
            print("X spotted!")
            return True
    
def main():
    while True:
        givenstring = input("Write something (quit ends): ")
        if givenstring == "quit":
            break
        else:
            tester(givenstring)

if __name__ == "__main__":
    main()
