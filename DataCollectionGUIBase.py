from tkinter import *
from tkinter import filedialog
from moviepy.editor import *
import cv2
import numpy as np

root = Tk() #name of our tkinter window
filedirectory = ""

def command_directoryExplorer():
    filename = filedialog.askdirectory(initialdir = "/",
    title = "Select a Directory")
    label_file_explorer.configure(text= "File Directory: " + filename)

label_file_explorer = Label(root, text = "Select the Directory to save your file:", width = 100, height = 4)
button_file_explorer = Button(root, text = "Open File", command = command_directoryExplorer)


#Root Window Properties
label_file_explorer.grid(column =1, row =1)
button_file_explorer.grid(column =1, row=2)
root.title("Data Collection PiCamera GUI")
root.geometry("1000x750")

root.mainloop()