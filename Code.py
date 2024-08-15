import tkinter
from tkinter import ttk
from tkinter import*
import random
#01/07/2024/ 23/07/2024 
window = tkinter.Tk()
window.title("Julies Party Store")

frame = tkinter.Frame(window)
frame.pack()

#print
def enter_data():
    customer_name = customer_name_entry.get()
    item_hired= item_hired_combobox.get()
    receipt= receipt1
    print (customer_name, item_hired, receipt)


# Saving user information #01/07/2024
user_info_frame =tkinter.LabelFrame(frame, text="Hired")
user_info_frame.grid(row = 0, column = 0, padx = 3, pady = 3)

#Customer name #5/07/2024
customer_name_label = tkinter.Label(user_info_frame, text = "Customer Name")
customer_name_label.grid(row = 0, column = 0, padx = 20, pady = 20) 
item_hired_label = tkinter.Label(user_info_frame,text = "Item Hired")

#combobox used for item hired #5/07/2024
item_hired_combobox = ttk.Combobox(user_info_frame,values=["Balloons","Cups","Ribbons", "Party Hats","Table cloths"])
item_hired_label.grid(row = 2, column = 0)
item_hired_combobox.grid(row = 2, column = 2, padx = 5, pady = 5)

item_hired_label.bind('<<ComboboxSelected>>')


                                   
customer_name_entry = tkinter.Entry(user_info_frame)
customer_name_entry.grid(row = 0, column = 2)


#23/07/2024
receipt = tkinter.Label(user_info_frame, text = "Receipt")
receipt.grid(row = 3, column = 0, padx= 5, pady = 5,sticky = E)
#24/07/2024
receipt1 = random.randint(1000, 1099)

#2/08/2024
#Quit
def main():
    Button(user_info_frame, text = "Quit", command = quit).grid(column = 6, row= 6, sticky = W)
    window.mainloop()
    
# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=1, column=0, sticky="news", padx=20, pady=10)


#5/07/2024
main()
