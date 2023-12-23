from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols

    shuffle(password_list)
    # name= ["ram", "syam", "chintu" ] ~raja = "#".join(name)~ print(raja)~  output = ram#syam#chintu
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    password_text.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pass_saved = password_text.get()
    website_saved = website_text.get()
    email_saved = email_text.get()
    if len(pass_saved) == 0 or len(email_saved) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure u haven't left any box empty")
    else:
        is_ok = messagebox.askokcancel(title=website_saved, message="These are the details entered:\n" f"Email:{email_saved} \n Password: {pass_saved}")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{pass_saved} |  {website_saved}  |  {email_saved}\n")

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
password_label.grid(row=3 , column=0)

website_text = Entry(width=35)
website_text.insert(END, "")
website_text.focus()
website_text.grid(row=1, column=1,columnspan=2)


email_text = Entry(width=35)
email_text.insert(END, "shivam@larchat.com")
email_text.grid(row=2, column=1, columnspan=2)


password_text = Entry(width=21)
password_text.insert(END, "")
password_text.grid(row=3, column=1)

button_gp = Button(text="Generate Password",highlightthickness=0, command=generate_password)
button_gp.grid(row=3, column=2)


button_add = Button(text="Add", width=36, height=1,command=save)
button_add.grid(row=4, column=1, columnspan=2)




















































window.mainloop()