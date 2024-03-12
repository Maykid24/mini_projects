import string
import random

def generate_password(password_length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

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

            #Being able to determine which group the user has selected in order to return a password according to what the user would like
            if user_choice == 1:
                all_characters = lowercase_letters + uppercase_letters + digits + special_characters
                password = ''.join(random.choice(all_characters) for _ in range(password_length))
                return password
            elif user_choice == 2:
                alpha_characters = uppercase_letters + lowercase_letters
                password = ''.join(random.choice(alpha_characters) for _ in range(password_length))
                return password
            elif user_choice == 3:
                alpha_num_characters = uppercase_letters + lowercase_letters + digits
                password = ''.join(random.choice(alpha_num_characters) for _ in range(password_length))
                return password
            elif user_choice == 4:
                alpha_special_characters = uppercase_letters + lowercase_letters + special_characters
                password = ''.join(random.choice(alpha_special_characters) for _ in range(password_length))
                return password
            elif user_choice == 5:
                upper_special_characters = uppercase_letters + special_characters
                password = ''.join(random.choice(upper_special_characters) for _ in range(password_length))
                return password
            elif user_choice == 6:
                lower_special_characters = lowercase_letters + special_characters
                password = ''.join(random.choice(lower_special_characters) for _ in range(password_length))
                return password
            elif user_choice == 7:
                upper_digits = uppercase_letters + digits
                password = ''.join(random.choice(upper_digits) for _ in range(password_length))
                return password
            elif user_choice == 8:
                lower_digits = lowercase_letters + digits
                password = ''.join(random.choice(lower_digits) for _ in range(password_length))
                return password
            else:
                print("Invalid choice. Please choose a number between 1 and 8.")
        except ValueError:
            print("Use numbers only for selection")

#Initiating the python script to run the correct input and functions associated with the script
if __name__ == "__main__":
    password_length = int(input("Enter the length of the password you want to generate: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
