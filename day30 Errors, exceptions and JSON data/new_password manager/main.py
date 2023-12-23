from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    # name= ["ram", "syam", "chintu" ] ~raja = "#".join(name)~ print(raja)~  output = ram#syam#chintu
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    search_text = website_text.get().lower()
    try:
        with open("data.json") as check_file:
            data_read = json.load(check_file)
            print(data_read)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")
    else:

        if search_text in data_read:
            email = data_read[search_text]["email"]
            password = data_read[search_text]["password"]
            messagebox.showinfo(title=search_text, message=f"email: {email}\n password: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"No {search_text} Value saved Earlier")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    pass_saved = password_text.get()
    website_saved = website_text.get()
    email_saved = email_text.get()
    new_data = {
        website_saved: {
            "email": email_saved,
            "password": pass_saved
        }
    }

    if len(pass_saved) == 0 or len(email_saved) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure u haven't left any box empty")
    else:


        try:
            with open("data.json", "r") as data_file:
                # Reading the data file
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}  # Initialize an empty dictionary if the file doesn't exist

        # Updating old data with new data
        data.update(new_data)

        # Writing the updated data to the file
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)





        website_text.delete(0, END)
        email_text.delete(0, END)
        password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
pass_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_text = Entry(width=21)
website_text.insert(END, "")
website_text.focus()
website_text.grid(row=1, column=1)

email_text = Entry(width=37)
email_text.insert(END, "shivam@larchat.com")
email_text.grid(row=2, column=1, columnspan=3)

password_text = Entry(width=21)
password_text.insert(END, "")
password_text.grid(row=3, column=1)

button_gp = Button(text="Generate Password", command=generate_password)
button_gp.grid(row=3, column=2)

button_add = Button(text="Add", width=36, height=1, command=save)
button_add.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
