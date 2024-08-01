#Author: Mandita Ram
#Title: Version 02 of Julies Party Store
#Date:05/07/2024
#01/07/2024
import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title("Data Entry ")

frame = tkinter.Frame(window)
frame.pack()

# Saving user information #1/07/2024
user_info_frame =tkinter.LabelFrame(frame, text="User information")
user_info_frame.grid(row = 0, column = 0, padx = 3, pady = 3)

#Customer name #5/07/2024
customer_name_label = tkinter.Label(user_info_frame, text = "Customer Name")
customer_name_label.grid(row = 0, column = 0, padx = 20, pady = 20) 
item_hired_label = tkinter.Label(user_info_frame,text = "Item Hired")

#combobox used for item hired #5/07/2024
item_hired_combobox = ttk.Combobox(user_info_frame,values=["Balloons","Cups","Ribbons", "Party Hats","Table cloths"])
item_hired_label.grid(row = 2, column = 0)
item_hired_combobox.grid(row = 2, column = 2, padx = 5, pady = 5)
                                   
customer_name_entry = tkinter.Entry(user_info_frame)
customer_name_entry.grid(row = 0, column = 2)



window.mainloop()
