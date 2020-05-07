The last exercise in this chapter adds a small feature to the other continuous exercise project, the notebook. 
In this exercise, add a feature which includes the date and time of the written note to the program. 
The program works as earlier, but saves data in the form "[note]:::[date and time]" meaning that 
there is a three-colon separator between the note and timestamp.
import time
while True:
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit")
	number = int(input("Please select one: "))
	if number == 2:
		myfile = open("notebook.txt","a")
		mytext = input("Write a new note: ")
		mytext = mytext+":::"
		mytext += time.strftime("%X %x")
		myfile.write(mytext+"\n")
		myfile.close()
	elif number == 1:
		myfile = open("notebook.txt","r")
		filetext = myfile.read()
		print(filetext)
		myfile.close()
	elif number == 3:
		myfile = open("notebook.txt","r+")
		myfile.seek(0)
		myfile.truncate()
		print("Notes deleted.")
		myfile.close()
	elif number == 4:
		print("Notebook shutting down, thank you.")
		break
	else:
		print("Incorrect selection")
