import sys

print("What is the secret passphrase 4?")
userInput = input() # User input to provide the secret passphrase 

x = userInput.split(" ")  # Split into array the passphrase 

passphrase = ["2", "7", "9", "9", "8", "7"] # Iterate through list of characters

if(x[0] == '9'): # Check first if value character is st to '9'
	for x in passphrase:
		if(x[7:] == passphrase):
			print("Trigger 4 diffused!\n")
		else: 
			print("Wrong passphrase!")
else: 
 	print("Wrong passphrase!")
