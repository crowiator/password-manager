from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # These lists are used to in password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generating items in lists for password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(8, 10))]

    # Combine all list together
    password_list = password_letters + password_symbol + password_numbers

    # Shuffle password
    shuffle(password_list)

    # Create string from list
    password = "".join(password_list)

    # Insert new password to input
    password_input.insert(0, password)

    # Save new password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


# Function for saving password to file
def save_password_to_file():

    # Variables from inputs
    webpage = website_input.get().title()
    username = username_input.get()
    password = password_input.get()

    # Dictionary
    new_data = {
        webpage : {
            "email": username,
            "password": password
        }
    }

    # Check if inputs are not empty
    if len(webpage) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Wrong input", message="Please don't leave any fields empty!")
    else:
        try:
            # Save data in json format
            with open("passwords.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
            # If file does not exist, crate and write into new file
        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            # Updating old data
            data.update(new_data)

            with open("passwords.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear all entries
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD------------------------------- #
def find_password():
    webpage_key = website_input.get().title()
    try:
        with open("passwords.json", "r") as data_file:
        # Reading old data
            data = json.load(data_file)
            page = data[webpage_key]

    except FileNotFoundError:
        messagebox.showerror("Key Error", "No Data File Found")

    except KeyError:
        messagebox.showerror("Key Error", "No webpages found")

    else:
        email_item = page["email"]
        password_item = page["password"]
        messagebox.showinfo(f"{page}", f"Email: {email_item}\n Password: {password_item}")




# ---------------------------- UI SETUP ------------------------------- #


#  Window
window = Tk()
# window.minsize(width=200, height=200)
window.title("Password manager")
window.config(padx=50, pady=50)

# Canvas for picture
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_picture)
canvas.grid(row=0, column=1)

# Website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky='W')

# Email/Username label
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky='W')

# Password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky='W')

# Website input
website_input = Entry(width=21)
website_input.grid(row=1, column=1, sticky='W')
website_input.focus()

# Email/Username input
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky='W')
username_input.insert(0, "jack@gmail.com")
# Password input
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky='W')

# Generate Password Button
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky='NS')

# Search Button
search_button = Button(text="Search", width=14,  command=find_password)
search_button.grid(row=1, column=2, sticky='NS')

# Add Button
add_button = Button(width=36, text="Add", command=save_password_to_file)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
