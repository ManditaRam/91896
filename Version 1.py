#Author: Mandita Ram
#Title: Version 01 of Julies Party Store
#Date:01/07/2024
import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title("Data Entry ")

frame = tkinter.Frame(window)
frame.pack()

# Saving user information 
user_info_frame =tkinter.LabelFrame(frame, text="User information")
user_info_frame.grid(row = 0, column = 0, padx = 3, pady = 3)
