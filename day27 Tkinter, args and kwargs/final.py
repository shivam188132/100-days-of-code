from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)


# window.minsize(height=500, width=500)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)
calculate_button = Button(text="calculator", command=miles_to_km)
calculate_button.grid(column=2, row=2)

window.mainloop()
