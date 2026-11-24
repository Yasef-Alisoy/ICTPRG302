#This program is a password manager with menu options to store and view credentials.

import string as s
# This function displays the menu options to the user
def display_menu():
    print("\nMenu:")
    print("1. Save credentials")
    print("2. View credentials")
    print("3. Exit")

def encrypted_text(value, shift = 3):
    #char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<,"
    char_set = s.ascii_letters + s.digits + s.punctuation
    encrypted_text = ""
    #loop each char and shift value to 3 spots to the right. 

    for character in value:

        #find current location 
        original_index = char_set.find(character)

        if original_index != -1:
            #shift 3 pos to the right
            shifted_index = (original_index + shift) % len(char_set)
            encrypted_text += char_set[shifted_index]
        else:
            encrypted_text += character

    return encrypted_text


def decrypted_text(value, shift = -3):
    #char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<,"
    char_set = s.ascii_letters + s.digits + s.punctuation
    decrypted_text = ""
    #loop each char and shift value to 3 spots to the right. 

    for character in value:

        #find current location 
        original_index = char_set.find(character)

        if original_index != -1:
            #shift 3 pos to the right
            shifted_index = (original_index + shift) % len(char_set)
            decrypted_text += char_set[shifted_index]
        else:
            decrypted_text += character

    return decrypted_text

# This function reads and displays records from the file
def display_records():
    try:
        with open("records.txt", "r") as file:
            # Print column headers
            print("\n{:<20} {:<30} {:<50}".format("URL/resource", "User_name", "Password"))
            print("-" * 80)
            #loop througt each line in the file
            for line in file:
                data = line.strip().split(",") #Split line into parts using comma
                #Display the name and first detail field
                dec_url = decrypted_text(data[0])
                dec_username = decrypted_text(data[1])
                dec_password = decrypted_text(data[2])
                print("{:<20} {:<30} {:<50}".format(dec_url, dec_username, dec_password))
    except FileNotFoundError:
        # This runs if the file doesn't exist yet
        print("\nThe file 'records.txt' does not exist. No records to display.")



# This function adds a new record to the file
def add_record():
    # Prompt the user for input
    url = input("\nEnter URL/resource: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Only add the record if all three fields are filled in
    if url and username and password:
        with open("records.txt", "a") as file:    # Open the file in append mode
            enc_url = encrypted_text(url)
            enc_username = encrypted_text(username)
            enc_password = encrypted_text(password)
            file.write(f"{enc_url},{enc_username},{enc_password}\n")  # write data to the file
        print("\nRecord added successfully!")
    else:
        print("\nInvalid input. All fields are required.")


# Main program loop that runs until the user chooses to exit
while True:
    display_menu()  # Show the menu
    choice = input("Enter your choice: ")
    # Run the appropriate function based on user input
    if choice == "1":
        add_record()
    elif choice == "2":
        display_records()
    elif choice == "3":
        print("\nExiting the program. Goodbye!")
        break  # Exit the loop and end the program
    else:
        print("\nInvalid choice. Please try again.")




