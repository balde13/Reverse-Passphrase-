import sys, os 

print("Whats is the second secret passphrase")
userInput = input() #Get user input of passphrase

if (len(userInput) !=9): #IF the lenght of the passphrase is not nine return false and close
	print("Wrong passphrase")
	sys.exit(0)

path = os.getcwd()  # Get the current working directory
fileName = os.listdir(path) #find the bomb2019 in the current directory

if "bomb2019" in fileName: #Get only the bomb2019 file from list
	fileName = "bomb2019"

	if (fileName == userInput): #Return print statement of success or else false and exit
		print("Trigger 2 diffused!")
	else: 
		print("Wrong passphrase")
		sys.exit(0)
