import secrets
import string
import time

# Get the password length from the user.
user_input_length = int(input("Password Length? (12 or more is recommended) "))

# A while loop as a parameter for the user to choose if they wants digits in the password or not.
while True:
    user_input_digits = input("Do you want digits? [y/n] ")
    if user_input_digits in ["yes", "y"]:
        digits = string.digits
        break
    
    elif user_input_digits in ["no", "n"]:
        digits = ""
        break

    else :
        print ("Enter a valid answer yes or no. you can use (y) or (n)")

# A while loop as a parameter for the user to choose if they wants special characters in the password or not.
while True:
    user_input_special = input("Do you want special characters? [y/n] ")
    if user_input_special in ["yes", "y"]:
        special = "!@#$%^&*"
        break
    
    elif user_input_special in ["no", "n"]:
        special = ""
        break

    else :
        print ("Enter a valid answer yes or no. you can use (y) or (n)")

# a functions that generates the password.
def generate_random_password(length=user_input_length):
    characters = string.ascii_letters + digits + special
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# printing the password on screen
random_password = generate_random_password()
print(random_password)

# Za Warudo
time.sleep(60)
