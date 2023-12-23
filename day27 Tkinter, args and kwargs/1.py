from tkinter import *

window = Tk()

window.title("My First Gui Programme")
window.minsize(width=600, height=600)

# label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
# or
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()



window.mainloop()
