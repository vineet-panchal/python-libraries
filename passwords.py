import secrets
import string
# importing libraries

def generatePassword(length): 
    """Generate a random password of length using the ASCII character set"""
    password = "" # password initialized
    isStrong = False # is password strong

    while not isStrong: # is password strong?
        password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length)) # keep generating until it's strong enough
        
        if (any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in string.punctuation for char in password)): # does it follow the criteria of a strong password?
            return password

if __name__ == '__main__': # main method
    length = int(input("Enter the length of the password you want to generate:  "))
    print("\nYour generated password is: ", generatePassword(length), "\n")
