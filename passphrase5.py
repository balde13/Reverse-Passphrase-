import sys

passPhrase = "1879D43" # The password is explicitly define

print("Please help! What is the first passphrase?")
userInput = input() # We ask for user input so they can provide the passphrase

# Here if the user input is equal to the passphrase we return a pass print statement else return false and exit 
if(userInput == passPhrase):
	print("Trigger 5")
else: 
	print("Wrong Passphrase.")
	sys.exit(1)

