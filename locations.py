from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
# import RPi.GPIO as GPIO
#import cv2
import numpy as np
# import picamera
import time

root = Tk() #name of our tkinter window
filedirectory = ""
font_bold = ('calibre',11,'bold')
font_normal = ('calibre',11,'normal')
label_font = ('calibre', 14, 'bold')
# camera = picamera.PiCamera()
# camera.rotation = 180
rec_duration = 0

#location and name of video label
label_location = Label(root, text = 'Location and Name of Video:', font = label_font)
label_location.place(x = 5, y = 15)


#filename command
filename_var = StringVar()
def confirm_filename():
    filename = filename_var.get()
    # if (filename.find(".mp4") < 0):
    #     filename += ".mp4"
    filename_var.set(filename)
    label_confirm_filename.configure(text = "Confirmed filename: " + filename)

# file name widget
label_filename = Label(root, text = "Enter file name:", font = font_bold)
entry_filename = Entry(root, textvariable = filename_var, font = font_normal)
button_confirm_filename = Button(root, text = "Confirm", font = font_normal, command = confirm_filename)
label_confirm_filename = Label(root, text = "", font = font_normal)

#directory selector command
def command_directoryExplorer():
    filedir = filedialog.askdirectory(initialdir = "/",
    title = "Select a Directory")
    label_file_explorer.configure(text= "File Directory: " + filedir)

# directory selector widget
label_file_explorer = Label(root, text = "Select the Directory to save your file:", font = font_bold, width = 100, height = 4)
button_file_explorer = Button(root, text = "Select Directory", font = font_normal, command = command_directoryExplorer)


#experimental variables label
label_experimental = Label(root, text = 'Experimental Variables:', font = label_font)
label_experimental.place(x=5, y = 220)


#pi number function
def pi_button():
    if pinumvar.get() == "Off":
        entry_pinum.configure(state='disabled')
        label_confirmed_pinum.configure(text = "")
    else:
        entry_pinum.configure(state="normal")
        entry_pinum.insert(0, '')


#pi number widget
pinumvar = StringVar()
raspinum = IntVar()
entry_pinum = Entry(root, width = 15, font = font_normal, textvariable = raspinum, state='disabled')
checkbox_pinum = Checkbutton(root, text = "Pi Number", width = 15, font = font_bold, variable = pinumvar, onvalue="On", offvalue="Off", command=pi_button)
checkbox_pinum.deselect()
entry_pinum.place(x=55,y=350)
checkbox_pinum.place(x=20,y=330)

label_confirmed_pinum = Label(root, text = "")
label_confirmed_pinum.place(x=50, y=375)
def confirm_pinum():
    if(pinumvar.get() == "On"):
        label_confirmed_pinum.configure(text = "Confirmed Pi Number: " + str(raspinum.get()), font = font_normal)

button_confirm_pinum = Button(root, text = "Confirm", font = font_normal, command = confirm_pinum)
button_confirm_pinum.place(x=200, y =350)


#recording duraction command
duration_var =  DoubleVar()
def confirm_duration():
    duration = duration_var.get()
    rec_duration = duration * 60
    label_confirm_duration.configure(text = "Confirmed duration: " + str(rec_duration) + " seconds")

# recording duration widget
label_duration = Label(root, text = "Recording duration (in minutes):", font = font_bold)
entry_duration = Entry(root, width = 10, textvariable= duration_var, font = font_normal)
button_confirm_duration = Button(root, text = "Confirm", font = font_normal, command = confirm_duration)
label_confirm_duration = Label(root, text = "", font = font_normal)


#Recording Type Function
'''Recording Type'''
rectype_list = []
dynamic_widgets = []
        
def rec_chk():
    if rec_var.get() == "Off":
        for i in dynamic_widgets:
            i.destroy()        

def rectype(self):
    choice = rec.get()
    # print(choice)
    if choice == "Post-Operation":
        for i in dynamic_widgets:
            i.destroy()
        # polabel = Label(root, text="PO Type:")
        # dynamic_widgets.append(polabel)
        # polabel.place(x=100, y=180)
        types = StringVar()
        types.set("Select PO Type")
        postop = OptionMenu(root, types, "Sham","Laparotomy")
        dynamic_widgets.append(postop)
        postop.place(x=160, y=430)
        POtype = types.get()
        if POtype == "Sham":
            recordingtype = 'SHAM'
        elif POtype == "Laparotomy":
            recordingtype = 'LAPA'
        animalid = Label(root, text="Animal ID:")
        dynamic_widgets.append(animalid)
        animalid.place(x=20, y=485)
        animalid_entry = Entry(root, width=10)
        dynamic_widgets.append(animalid_entry)
        animalid_entry.place(x=85, y=485)
        strain = Label(root, text="Strain:")
        dynamic_widgets.append(strain)
        strain.place(x=20, y=515)
        strain_entry = Entry(root, width=10)
        dynamic_widgets.append(strain_entry)
        strain_entry.place(x=85, y=515)
        surgeon = Label(root, text="Surgeon:")
        dynamic_widgets.append(surgeon)
        surgeon.place(x=20, y=455)
        surgeon_entry = Entry(root, width = 10)
        dynamic_widgets.append(surgeon_entry)
        surgeon_entry.place(x=85, y=455)
        surgery_start = Label(root, text="Start Time (HH:MM):")
        dynamic_widgets.append(surgery_start)
        surgery_start.place(x=190, y=455)
        start_entry = Entry(root, width=10)
        dynamic_widgets.append(start_entry)
        start_entry.place(x=320, y=455)
        surgery_end = Label(root, text = "End Time (HH:MM):")
        dynamic_widgets.append(surgery_end)
        surgery_end.place(x=190, y=485)
        end_entry = Entry(root, width=10)
        dynamic_widgets.append(end_entry)
        end_entry.place(x=320, y=485)
        animal_weight = Label(root, text="Weight (g):")
        dynamic_widgets.append(animal_weight)
        animal_weight.place(x=190, y=515)
        weight_entry = Entry(root, width=5)
        dynamic_widgets.append(weight_entry)
        weight_entry.place(x=320, y=515)
        lorr = Label(root, text="LORR (s):")
        dynamic_widgets.append(lorr)
        lorr.place(x=20, y=545)
        lorr_entry = Entry(root, width=5)
        dynamic_widgets.append(lorr_entry)
        lorr_entry.place(x=85, y=545)

    elif choice == "Baseline":
        for i in dynamic_widgets:
            i.destroy()
        recordingtype = 'BASE'
        animalid = Label(root, text="Animal ID:")
        dynamic_widgets.append(animalid)
        animalid.place(x=20, y=455)
        animalid_entry = Entry(root, width=20)
        dynamic_widgets.append(animalid_entry)
        animalid_entry.place(x=120, y=455)
        strain = Label(root, text="Strain:")
        dynamic_widgets.append(strain)
        strain.place(x=20, y=480)
        strain_entry = Entry(root, width=20)
        dynamic_widgets.append(strain_entry)
        strain_entry.place(x=120, y=480)
    
    elif choice == "Test":
        for i in dynamic_widgets:
            i.destroy()
        replicate = Label(root, text="Rep #:")
        dynamic_widgets.append(replicate)
        replicate.place(x=20, y=455)
        replicate_entry = Entry(root, width = 20)
        dynamic_widgets.append(replicate_entry)
        replicate_entry.place(x=90, y=455)
        recordingtype = 'TEST'
    else:
        for i in dynamic_widgets:
            i.destroy()

#recording type widget
rec_var = StringVar()
checkbox_recType = Checkbutton(root, text='Recording Type', width = 15, font = font_bold, variable = rec_var, onvalue="On", offvalue="Off", command=rec_chk)
checkbox_recType.deselect()
# checkbox_recType.pack(padx=5, pady=5, side=TOP, anchor=NW)
checkbox_recType.place(x=20, y=410)

rec = StringVar()
rec.set("Select Recording Type")
dropdown_recType = OptionMenu(root, rec, "Baseline", "Post-Operation", "Test","Select Recording Type", command=rectype)
dropdown_recType.place(x=30, y=430)


#camera settings labels
label_camera = Label(root, text = 'Camera Settings:', font = label_font)
label_camera.place(x=450, y=15)

# resolution function
res_var = StringVar()
confirmed_res = "(640, 480)"
def confirm_resolution():
    label_confirmed_res = Label(root, text = "Confirmed Resolution: " + res_var.get()).place(x=500, y=65)
    confirmed_res = res_var.get()
    strRes = res_var.get()
    res1 = int(strRes[1:strRes.find(',')])
    res2 = int(strRes[strRes.find(',')+2:len(strRes)-1])
    update_framerate_options()
    # camera.resolution = (res1,res2)

#resolution widget
label_resolution = Label(root, text = 'Select Camera Resolution: ', font = font_bold)
label_resolution.pack()
res_options = ["(640, 480)", "(1296, 972)", "(1296, 730)", "(1920, 1080)", "(2592, 1944)"]
res_var.set(res_options[0])
dropdown_resolution = OptionMenu(root, res_var, *res_options)
dropdown_resolution.pack()

button_confirm_resolution = Button(root, text = "Confirm", font = font_normal, command = confirm_resolution)
label_confirm_resolution = Label(root, text = "", font = font_normal)

# frame rate function and widget
frame_var = StringVar(root)
def confirm_framerate():
    label_confirmed_framerate = Label(root, text = "Confirmed Frame Rate: " + frame_var.get() + " fps").place(x=490, y=125)
    # camera.framerate = int(frame_var.get())

def update_framerate_options():
    import tkinter as tk
    frame_var.set('')
    confirmed_res = res_var.get()
    frOptions1 = ("42", "45", "50", "55", "60", "65", "70", "75", "80", "85", "90")
    frOptions2 = ("10", "20", "30", "40", "42")
    frOptions3 = ("10", "20", "30", "40", "42", "49")
    frOptions4 = ("10", "15", "20", "25", "30")
    frOptions5 = ("1", "5", "10", "15")

    if(confirmed_res == "(640, 480)"):
        framerate_options = frOptions1
    elif(confirmed_res == "(1296, 972)"):
        framerate_options = frOptions2
    elif(confirmed_res == "(1296, 730)"):
        framerate_options = frOptions3
    elif(confirmed_res == "(1920, 1080)"):
        framerate_options = frOptions4
    elif(confirmed_res == "(2592, 1944)"):
        framerate_options = frOptions5
    else:
        framerate_options = frOptions4
    
    dropdown_framerate['menu'].delete(0, 'end')
    print(framerate_options)
    for option in framerate_options:
        dropdown_framerate['menu'].add_command(label = option, command = tk._setit(frame_var, option))

label_framerate = Label(root, text = 'Select Camera Frame Rate: ', font = font_bold)
label_framerate.pack()

framerate_options = ("10", "20", "30", "40", "60")
dropdown_framerate = OptionMenu(root, frame_var, *framerate_options)


button_confirm_framerate = Button(root, text = "Confirm", font = font_normal, command = confirm_framerate)
button_confirm_framerate.pack()
label_confirm_framerate = Label(root, text = "", font = font_normal)
label_confirm_framerate.pack()


# sharpness slider widget and function
slider_sharpness = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10, length=300)
slider_sharpness.place(x= 460, y=180)

label_sharpness_number = Label(root, text = "Sharpness: ", font = font_bold)
label_sharpness_number.place(x= 460, y = 155)

def confirm_sharpness():
    label_confirm_sharpness = Label(root, text="Confirmed sharpness: " + str(slider_sharpness.get()))
    sharpness = slider_sharpness.get()
    label_confirm_sharpness.place(x=460, y= 240)

button_confirm_sharpness = Button(root, text='Confirm', command=confirm_sharpness).place(x=770, y=200)


#brightness slider widget and function
slider_brightness = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10, length=300)
slider_brightness.place(x= 460, y=290)

label_brightness_number = Label(root, text = "Brightness: ", font = font_bold)
label_brightness_number.place(x= 460, y = 265)

def confirm_brightness():
    label_confirm_brightness = Label(root, text="Confirmed brightness: " + str(slider_brightness.get()))
    brightness = slider_brightness.get()
    label_confirm_brightness.place(x=460, y= 350)

button_confirm_brightness = Button(root, text='Confirm', command=confirm_brightness).place(x=770, y=310)



#video preview label
label_video_preview = Label(root, text = 'Video Preview:', font = label_font)
label_video_preview.place(x =450, y =400)


# picamera initialization
def CameraON():
    # camera.preview_fullscreen = False
    # camera.preview_window = (90, 100, 320, 240)
    # camera.resolution = (640, 480)
    # camera.start_preview()
    print("hello")

def CameraOFF():
    # camera.stop_preview()
    print("hi")

def CameraRECORD():
    rec_duration = duration_var.get() *60
    if(filename_var.get() == ""):
        label_recording_status.configure(text = "Enter filename before starting recording!")
    elif(rec_duration == 0):
        label_recording_status.configure(text = "Enter recording duration before starting recording!")
    else:
        label_recording_status.configure(text = "Recording has begun!")
        label_recording_status.place(x = 580, y= 210)
        button_start_recording.configure(bg = "red")
        print(rec_duration)
        print(filename_var.get())
        filename = filename_var.get()
        t = time.localtime()
        recording_start_time = (time.strftime("%H:%M:%S", t))
        #camera.start_recording(f'{filename}.h264')
        bar()
        #camera.wait_recording(rec_duration)
        #camera.stop_recording()
        label_recording_status.configure(text = "Recording is complete!")
        button_start_recording.configure(bg = "skyblue1")
        #camera.close()
        t = time.localtime()
        recording_end_time = (time.strftime("%H:%M:%S", t))

#open preview button
button_open_preview = Button(root, text = "Open Preview", font = font_normal, command = CameraON)
button_open_preview.place(x=460,y=435)

#close preview button
button_close_preview = Button(root, text = "Close Preview", font = font_normal, command = CameraOFF)
button_close_preview.place(x=460, y = 465)

#start recording button
button_start_recording = Button(root, text = "Start Recording", font = font_bold, bg = "skyblue1", command = CameraRECORD)
button_start_recording.place(x = 590, y = 450)
label_recording_status = Label(root, text = '', font = font_normal)
label_recording_status.place(x = 695, y = 450)


#progress bar

label_progress = Label(root, text = "Recording Progress:", font = font_bold).place(x = 250, y = 600)
progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 400, mode= 'determinate')
progress.place(x=120, y = 630)

label_progressbar_status = Label(root, text = "0% Complete", font = font_normal)
label_progressbar_status.place(x=270, y = 660)

def bar():
    rec_duration = duration_var.get() *60
    for second in range(int(rec_duration+1)):
        progresspct = second/rec_duration *100
        progress['value'] = progresspct
        ppct = int(progresspct)
        label_progressbar_status.configure(text = str(ppct) + "% Complete")
        root.update_idletasks()
        time.sleep(1)
 
# Place Widgets

#filename place
label_filename.place(x=20, y=50)
entry_filename.place(x=120, y=50)
button_confirm_filename.place(x=50, y=75)
label_confirm_filename.place(x=100,y=75)

#directory place
label_file_explorer.place(x=-280, y = 100)
button_file_explorer.place(x = 50, y= 150)

#duration place
label_duration.place(x=20, y=265)
entry_duration.place(x=225, y=265)
button_confirm_duration.place(x=40, y=290)
label_confirm_duration.place(x=90,y=290)

#resolution place
label_resolution.place(x= 460, y= 40)
dropdown_resolution.place(x=610, y= 40)
button_confirm_resolution.place(x=720, y=40)

#framerate place
label_framerate.place(x= 460, y= 100)
dropdown_framerate.place(x=625, y= 100)
button_confirm_framerate.place(x=680, y=100)



root.title("Data Collection PiCamera GUI")
root.geometry("1000x800")
root.resizable(width = False, height = False)

root.mainloop()
