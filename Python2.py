The last exercise in this chapter is the first part of the second multi-part assignment of this course, the notebook. 
In this notebook the user is able to add, read and delete notes from a separate note file "notebook.txt".


Create a program which allows the user to
(1) Read the contents of the notebook
(2) Add notes to the file or
(3) Delete all of the notes.
If the user selects 1, the entire notebook file is printed to the screen, if 2 then the program prompts "Write a new note: ", and adds the written note as the last line into the file with a trailing line break "\n". 
If the player selects 3, the file is emptied and the message "Notes deleted" will be shown. Also add the option (4) Quit, which ends the program, printing "Notebook shutting down, thank you.". 
With other selections the program prompts "Incorrect selection". When working, the program prints following:
while True:
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit")
	number = int(input("Please select one: "))
	if number == 2:
		myfile = open("notebook.txt","a")
		mytext = input("Write a new note: ")
		myfile.write(mytext)
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
