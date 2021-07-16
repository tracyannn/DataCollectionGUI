from tkinter import *
from tkinter import filedialog
# import RPi.GPIO as GPIO
import cv2
import numpy as np
# import picamera
import time

root = Tk() #name of our tkinter window
filedirectory = ""
font_bold = ('calibre',12,'bold')
font_normal = ('calibre',12,'normal')
# camera = picamera.PiCamera()

def command_directoryExplorer():
    filedir = filedialog.askdirectory(initialdir = "/",
    title = "Select a Directory")
    label_file_explorer.configure(text= "File Directory: " + filedir)

filename_var = StringVar()
def confirm_filename():
    filename = filename_var.get()
    # if (filename.find(".mp4") < 0):
    #     filename += ".mp4"
    filename_var.set(filename)
    label_confirm_filename.configure(text = "Confirmed filename: " + filename)

duration_var = IntVar()
def confirm_duration():
    duration = duration_var.get()
    label_confirm_duration.configure(text = "Confirmed duration: " + str(duration) + " seconds")

def pi_button():
    if pi_number.get() == "Off":
        entry_pinum.delete(0, 'end')
        entry_pinum.insert(0, 'Pi Number')

label_experimental = Label(root, text = 'Experimental')
# experimental.pack(side=TOP, anchor=NW)


#pi number widget
pi_number = StringVar()
entry_pinum = Entry(root, width = 20, font = font_normal)
entry_pinum.insert(0, 'Pi Number')
checkbox_pinum = Checkbutton(root, text = "Pi Number", width = 15, font = font_bold, variable = pi_number, onvalue="On", offvalue="Off", command=pi_button)
checkbox_pinum.deselect()
entry_pinum.place(x=20,y=100)
checkbox_pinum.place(x=0,y=50)

#recording type widget
rec_var = StringVar()
checkbox_recType = Checkbutton(root, text='Recording Type', width = 15, font = font_bold, variable = rec_var, onvalue="On", offvalue="Off")
checkbox_recType.deselect()
# checkbox_recType.pack(padx=5, pady=5, side=TOP, anchor=NW)
checkbox_recType.place(x=20, y=150)

rec = StringVar()
rec.set("Select Recording Type")
dropdown_recType = OptionMenu(root, rec, "Baseline", "Post-Operation", "Test","Select Recording Type")
dropdown_recType.place(x=20, y=180)
# dropdown_recType.pack(side=TOP, anchor=NW)

# resolution widget
res_var = StringVar()
def confirm_resolution():
    label_confirmed_res = Label(root, text = "Confirmed Resolution: " + res_var.get()).place(x=500, y=655)
    strRes = res_var.get()
    res1 = int(strRes[1:strRes.find(',')])
    res2 = int(strRes[strRes.find(',')+2:len(strRes)-1])
    camera.resolution = (res1,res2)

label_resolution = Label(root, text = 'Select Camera Resolution: ', font = font_bold)
label_resolution.pack()
res_options = ["(1920, 1080)", "(1280, 960)", "(1280, 720)", "(3840, 2160)"]
res_var.set(res_options[0])
dropdown_resolution = OptionMenu(root, res_var, *res_options)
dropdown_resolution.pack()

button_confirm_resolution = Button(root, text = "Confirm", font = font_normal, command = confirm_resolution)
label_confirm_resolution = Label(root, text = "", font = font_normal)

# frame rate widget
frame_var = StringVar()
def confirm_framerate():
    label_confirmed_framerate = Label(root, text = "Confirmed Frame Rate: " + frame_var.get() + " fps").place(x=775, y=655)
    camera.framerate = int(frame_var.get())

label_framerate = Label(root, text = 'Select Camera Frame Rate: ', font = font_bold)
label_framerate.pack()
framerate_options = ["24", "25", "30", "60", "120"]
frame_var.set(framerate_options[2])
dropdown_framerate = OptionMenu(root, frame_var, *framerate_options)
dropdown_framerate.pack()

button_confirm_framerate = Button(root, text = "Confirm", font = font_normal, command = confirm_framerate)
button_confirm_framerate.pack()
label_confirm_framerate = Label(root, text = "", font = font_normal)
label_confirm_framerate.pack()

# directory selector widget
label_file_explorer = Label(root, text = "Select the Directory to save your file:", font = font_normal, width = 100, height = 4)
button_file_explorer = Button(root, text = "Select Directory", font = font_normal, command = command_directoryExplorer)

# file name widget
label_filename = Label(root, text = "Enter file name:", font = font_bold)
entry_filename = Entry(root, textvariable = filename_var, font = font_normal)
button_confirm_filename = Button(root, text = "Confirm", font = font_normal, command = confirm_filename)
label_confirm_filename = Label(root, text = "", font = font_normal)

# recording duration widget
label_duration = Label(root, text = "Recording duration (in seconds):", font = font_bold)
entry_duration = Entry(root, textvariable= duration_var, font = font_normal)
button_confirm_duration = Button(root, text = "Confirm", font = font_normal, command = confirm_duration)
label_confirm_duration = Label(root, text = "", font = font_normal)

# picamera initialization

# def CameraON():
#     camera.preview_fullscreen = False
#     camera.preview_window = (90, 100, 320, 240)
#     camera.resolution = (640, 480)
#     camera.start_preview()

# def CameraOFF():
#     camera.stop_preview()


frame_video_preview = Frame(root, width = 730, height = 525, bg = "white")
frame_video_preview.place(x = 400, y = 25)

button_open_preview = Button(root, text = "Open Preview", font = font_normal)
button_open_preview.place(x=450,y=50)

button_close_preview = Button(root, text = "Close Preview", font = font_normal)
button_close_preview.place(x=450, y = 100)



# Place Widgets
label_file_explorer.place(x=-250, y = 400)
button_file_explorer.place(x = 100, y= 450)

label_filename.place(x=20, y=300)
entry_filename.place(x=150, y=300)
button_confirm_filename.place(x=125, y=325)
label_confirm_filename.place(x=75,y=355)

label_duration.place(x=20, y=600)
entry_duration.place(x=280, y=600)
button_confirm_duration.place(x=125, y=625)
label_confirm_duration.place(x=75,y=655)

label_resolution.place(x= 500, y= 600)
dropdown_resolution.place(x=500, y= 625)
button_confirm_resolution.place(x=610, y=625)

label_framerate.place(x= 775, y= 600)
dropdown_framerate.place(x=775, y= 625)
button_confirm_framerate.place(x=835, y=625)

root.title("Data Collection PiCamera GUI")
root.geometry("1200x850")
root.resizable(width = False, height = False)

root.mainloop()