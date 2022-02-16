from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------------- Search ------------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)



    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message=f"There is no json file created or available")

    else:
        if website in data:
            found_email = data[website]["email"]
            found_password = data[website]["password"]
            messagebox.showinfo(title="Email Found", message=f"Email Found: \n Email:{found_email} \n "
                                                             f"Password: {found_password}")
        else:
            messagebox.showinfo(tiltle="Email Not Found", message="Email Not Found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# window

window = Tk()
window.minsize(450, 350)
window.title("My Pass")
window.config(padx= 20, pady=20)


# canvas

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(row=0,column=1)

# labels

website_label= Label(text="Website:")
email_label = Label(text="Email/UserName:")
password_label = Label(text="Password:")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)



# entries

website_entry = Entry(width=31)
email_entry = Entry(width=50)
password_entry = Entry(width=31)
website_entry.focus()
email_entry.insert(0, "ps6129@srmist.edu.in")
website_entry.grid(row=1, column=1, columnspan=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, columnspan=1)

#buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="add", width=45, command=save)
generate_password_button.grid(row=3, column=2, columnspan=1)
add_button.grid(row=4, column=1, columnspan=2)

search_button =Button(text="Search", command=search, width=15)
search_button.grid(row= 1, column=2)






window.mainloop()
