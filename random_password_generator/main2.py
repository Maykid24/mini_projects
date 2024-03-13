#Modification of the random password generator to be more efficient
import string
import random

#Making global arguments for different strings
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

#Creating functions to facilitate password generation dependent on user input
def gen_pass_all_characters(pass_length):
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    return ''.join(random.choice(all_characters) for _ in range(pass_length))

def alpha_characters(pass_length):
    alpha_characters = uppercase_letters + lowercase_letters
    return ''.join(random.choice(alpha_characters) for _ in range(pass_length))

def alpha_num_characters(pass_length):
    alpha_num_characters = uppercase_letters + lowercase_letters + digits
    return ''.join(random.choice(alpha_num_characters) for _ in range(pass_length))

def alpha_special_characters(pass_length):
    alpha_special_characters = uppercase_letters + lowercase_letters + special_characters
    return ''.join(random.choice(alpha_special_characters) for _ in range(pass_length))

def upper_special_characters(pass_length):
    upper_special_characters = uppercase_letters + special_characters
    return ''.join(random.choice(upper_special_characters) for _ in range(pass_length))

def lower_special_characters(pass_length):
    lower_special_characters = lowercase_letters + special_characters
    return ''.join(random.choice(lower_special_characters) for _ in range(pass_length))

def upper_digits(pass_length):
    upper_digits = uppercase_letters + digits
    return ''.join(random.choice(upper_digits) for _ in range(pass_length))

def lower_digits(pass_length):
    lower_digits = lowercase_letters + digits
    return ''.join(random.choice(lower_digits) for _ in range(pass_length))

#Defining a dictionary for the above functions to be able to quickly grab and utilize the functions
pass_generators = {
    1: gen_pass_all_characters,
    2: alpha_characters,
    3: alpha_num_characters,
    4: alpha_special_characters,
    5: upper_special_characters,
    6: lower_special_characters,
    7: upper_digits,
    8: lower_digits,
}

#Main function asking the user for information of what kind of password the user would like
def generate_password(pass_length):
    while True:
        try:
            #Giving the user the ability to choose from a series of items
            user_choice = int(input("What kind of password would you like?\n"
                                     "1. Any character\n"
                                     "2. Upper and Lower case A-Z\n"
                                     "3. Upper, Lower, digits\n"
                                     "4. Upper, Lower, Special\n"
                                     "5. Upper and Special\n"
                                     "6. Lower and Special\n"
                                     "7. Upper and digits\n"
                                     "8. Lower and digits\n"))
            pass_generator = pass_generators.get(user_choice)
            if pass_generator:
                return pass_generator(pass_length)
            else:
                print("Invalid choice, please choose between 1 and 8")
        except ValueError:
            print("Use numbers only please")


#Intializing the function to run the above functions
if __name__ == "__main__":
    pass_length = int(input("Enter the length of the password you would like: "))
    generated_password = generate_password(pass_length)
    print("Password is: ", generated_password)


