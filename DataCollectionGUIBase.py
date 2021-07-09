from tkinter import *
from tkinter import filedialog
#from moviepy.editor import *
# import cv2
import numpy as np
# from picamera.array import PiRGBArray
# import picamera
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

def pi_button():
    if pi_number.get() == "Off":
        pi_entry.delete(0, 'end')
        pi_entry.insert(0, 'Pi Number')

experimental = Label(root, text = 'Experimental', font = ('calibre', 12, 'bold'))
experimental.pack(side=TOP, anchor=NW)

pi_number = StringVar()
pi_entry = Entry(root, width = 20)
pi_entry.insert(0, 'Pi Number')
pi_chk = Checkbutton(root, text = "Pi Number", width = 15, variable = pi_number, onvalue="On", offvalue="Off", command=pi_button)
pi_chk.deselect()
pi_chk.pack(padx = 5, pady = 5, side=TOP, anchor=NW)
pi_entry.pack(padx = 5, pady = 5, side=TOP, anchor=NW)

rec_var = StringVar()
rec_chk = Checkbutton(root, text='Recording Type', width = 15, variable = rec_var, onvalue="On", offvalue="Off")
rec_chk.deselect()
rec_chk.pack(padx=5, pady=5, side=TOP, anchor=NW)
rec = StringVar()
rec.set("Select Recording Type")
rec_type = OptionMenu(root, rec, "Baseline", "Post-Operation", "Test","Select Recording Type")
rec_type.pack(side=TOP, anchor=NW)



label_file_explorer = Label(root, text = "Select the Directory to save your file:", font = ('calibre',12,'bold'), width = 100, height = 4)
button_file_explorer = Button(root, text = "Select Directory", font = ('calibre',12,'normal'), command = command_directoryExplorer)

label_filename = Label(root, text = "Enter file name:", font = ('calibre',12,'bold'))
entry_filename = Entry(root, textvariable = filename_var, font = ('calibre',12,'normal'))
button_confirm_filename = Button(root, text = "Confirm", font = ('calibre',12,'normal'), command = confirm_filename)
label_confirm_filename = Label(root, text = "", font = ('calibre',12,'normal'))

label_duration = Label(root, text = "Recording duration (in seconds):", font = ('calibre',12,'bold'))
entry_duration = Entry(root, textvariable= duration_var, font = ('calibre',12,'normal'))
button_confirm_duration = Button(root, text = "Confirm", font = ('calibre',12,'normal'), command = confirm_duration)
label_confirm_duration = Label(root, text = "", font = ('calibre',12,'normal'))


#picamera initialization
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
#         key= cv2.waitKey(1) & 0xFF
#         rawCapture.truncate(0)
        
#         if key == ord('q'): #quit
#             cv2.destroyAllWindows()
#             camera.close()
#             break

    

    
#button_open_preview = Button(root, text = "Open Preview", command= picameraPreview)



#Root Window Properties
label_file_explorer.place(x=-325, y = 350)
button_file_explorer.place(x = 100, y= 400)
label_filename.place(x=12, y=250)
entry_filename.place(x=125, y=250)
button_confirm_filename.place(x=125, y=275)
label_confirm_filename.place(x=75,y=295)

label_duration.place(x=12, y=500)
entry_duration.place(x=225, y=500)
button_confirm_duration.place(x=125, y=525)
label_confirm_duration.place(x=75,y=555)


#button_open_preview.grid(column =1, row =3)
root.title("Data Collection PiCamera GUI")
root.geometry("1200x850")

root.mainloop()