import sys

passPhrase = "I l0v3 C0mput3r $ci3nc3." # Here the passphrase is explictly defined 

print("Please help! What is the first passphrase?")
userInput = input() # We ask for user input so they can provide the passphrase

# Here if the user input is equal to the passphrase we return a pass print statement else return false and exit 
if(userInput == passPhrase):
	print("Trigger 1 diffused.")
else: 
	print("Wrong Passphrase.")
	sys.exit(1)

