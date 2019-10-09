import sys

print("What is the secret passphrase 4?")
userInput = input() # User input to provide the secret passphrase 

x = userInput.split(" ")  # Split into array the passphrase 

sevens = ["7", "7", "7", "7", "7", "7", "7", "7"] # Iterate through character list 

if(x[0] == '9'): #Make sure the passphrase starts with nine
	for x in sevens:
		if(x[7:] == sevens):
			print("Trigger 4 diffused!\n")
		else: 
			print("Wrong passphrase!")
else: 
 	print("Wrong passphrase!")
