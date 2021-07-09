from tkinter import *
from tkinter import filedialog
import RPi.GPIO as GPIO
import cv2
import numpy as np
import picamera
import time

root = Tk() #name of our tkinter window
filedirectory = ""

def command_directoryExplorer():
    filedir = filedialog.askdirectory(initialdir = "/",
    title = "Select a Directory")
    label_file_explorer.configure(text= "File Directory: " + filedir)

filename_var = StringVar()
def confirm_filename():
    filename = filename_var.get()
    if (filename.find(".mp4") < 0):
        filename += ".mp4"
    filename_var.set(filename)
    label_confirm_filename.configure(text = "Confirmed filename: " + filename)

duration_var = IntVar()
def confirm_duration():
    duration = duration_var.get()
    label_confirm_duration.configure(text = "Confirmed duration: " + str(duration) + " seconds")



label_file_explorer = Label(root, text = "Select the Directory to save your file:", font = ('calibre',12,'normal'), width = 100, height = 4)
button_file_explorer = Button(root, text = "Select Directory", font = ('calibre',12,'normal'), command = command_directoryExplorer)

label_filename = Label(root, text = "Enter file name:", font = ('calibre',12,'bold'))
entry_filename = Entry(root, textvariable = filename_var, font = ('calibre',12,'normal'))
button_confirm_filename = Button(root, text = "Confirm", font = ('calibre',12,'normal'), command = confirm_filename)
label_confirm_filename = Label(root, text = "", font = ('calibre',12,'normal'))

label_duration = Label(root, text = "Recording duration (in seconds):", font = ('calibre',12,'bold'))
entry_duration = Entry(root, textvariable= duration_var, font = ('calibre',12,'normal'))
button_confirm_duration = Button(root, text = "Confirm", font = ('calibre',12,'normal'), command = confirm_duration)
label_confirm_duration = Label(root, text = "", font = ('calibre',12,'normal'))

label_resolution = Label(root, text = "What resolution would you like to set the video to:", font = ('calibre',12,'bold'))
# optionMenu_resolution = OptionMenu(root)

#picamera initialization
camera = picamera.PiCamera()

def CameraON():
    camera.preview_fullscreen = False
    camera.preview_window = (90, 100, 320, 240)
    camera.resolution = (640, 480)
    camera.start_preview()

def CameraOFF():
    camera.stop_preview()




# camera = picamera.PiCamera()
# camera.resolution = (1920, 1080)  # will be adjusted to user preferences
# camera.framerate = 30  # will be adjusted to user preferences
# camera.brightness = 44  # will be adjusted to user preferences

# def picameraPreview():
#     rawCapture = PiRGBArray(camera, size=(1920, 1080))
#     print ('Press q to quit preview.')
#     time.sleep(0.1)
#     for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
#         # image= frame.array  #grabbing frame
#         cv2.imshow("Preview Camera 1", image) #display image
#         rawCapture.truncate(0)
        
#         if key == ord('q'): #quit
#             cv2.destroyAllWindows()
#             camera.close()
#             break

#button_open_preview = Button(root, text = "Open Preview", command= picameraPreview)

#Root Window Properties
label_file_explorer.place(x=-250, y = 400)
button_file_explorer.place(x = 100, y= 450)
label_filename.place(x=20, y=200)
entry_filename.place(x=150, y=200)
button_confirm_filename.place(x=125, y=225)
label_confirm_filename.place(x=75,y=255)

label_duration.place(x=20, y=600)
entry_duration.place(x=280, y=600)
button_confirm_duration.place(x=125, y=625)
label_confirm_duration.place(x=75,y=655)


#button_open_preview.grid(column =1, row =3)
root.title("Data Collection PiCamera GUI")
root.geometry("1200x850")
root.resizable(width = False, height = False)

root.mainloop()