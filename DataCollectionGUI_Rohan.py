from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
# import RPi.GPIO as GPIO
# import cv2
import numpy as np
# import picamera
import time
import csv
import tkinter.font as font

root = Tk() #name of our tkinter window
filedirectory = ""
font_bold = ('calibre',11,'bold')
font_normal = ('calibre',11,'normal')
# camera = picamera.PiCamera()
# camera.rotation = 180
rec_duration = 0
pi_flag=False

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

duration_var =  DoubleVar()
def confirm_duration():
    duration = duration_var.get()
    rec_duration = duration * 60
    label_confirm_duration.configure(text = "Confirmed duration: " + str(rec_duration) + " seconds")

def pi_button():
    if pinumvar.get() == "Off":
        entry_pinum.configure(state='disabled')
        label_confirmed_pinum.configure(text = "")
    else:
        entry_pinum.configure(state="normal")
        entry_pinum.insert(0, '')


# label_experimental = Label(root, text = 'Experimental')
# experimental.pack(side=TOP, anchor=NW)


#pi number widget
pinumvar = StringVar()
raspinum = IntVar()
entry_pinum = Entry(root, width = 20, font = font_normal, textvariable = raspinum, state='disabled')
checkbox_pinum = Checkbutton(root, text = "Pi Number", width = 15, font = font_bold, variable = pinumvar, onvalue="On", offvalue="Off", command=pi_button)
checkbox_pinum.deselect()
entry_pinum.place(x=20,y=85)
checkbox_pinum.place(x=20,y=50)

label_confirmed_pinum = Label(root, text = "")
label_confirmed_pinum.place(x=20, y=110)
def confirm_pinum():
    if(pinumvar.get() == "On"):
        pi_flag = True
        label_confirmed_pinum.configure(text = "Confirmed Pi Number: " + str(raspinum.get()))


button_confirm_pinum = Button(root, text = "Confirm", font = font_normal, command = confirm_pinum)
button_confirm_pinum.place(x=190, y =85)

notes_label = Label(root, text="Notes (optional):", font=font_bold)
notes_label.place(x=300, y=50)   
notes_text = Text(root, width=25, height=5, font=font_normal)
notes_text.place(x=300,y=85)

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
        postop.place(x=160, y=180)
        POtype = types.get()
        if POtype == "Sham":
            recordingtype = 'SHAM'
        elif POtype == "Laparotomy":
            recordingtype = 'LAPA'
        animalid = Label(root, text="Animal ID:")
        dynamic_widgets.append(animalid)
        animalid.place(x=20, y=235)
        animalid_entry = Entry(root, width=10)
        dynamic_widgets.append(animalid_entry)
        animalid_entry.place(x=85, y=235)
        strain = Label(root, text="Strain:")
        dynamic_widgets.append(strain)
        strain.place(x=20, y=260)
        strain_entry = Entry(root, width=10)
        dynamic_widgets.append(strain_entry)
        strain_entry.place(x=65, y=260)
        surgeon = Label(root, text="Surgeon:")
        dynamic_widgets.append(surgeon)
        surgeon.place(x=20, y=210)
        surgeon_entry = Entry(root, width = 10)
        dynamic_widgets.append(surgeon_entry)
        surgeon_entry.place(x=85, y=210)
        surgery_start = Label(root, text="Start Time (HH:MM):")
        dynamic_widgets.append(surgery_start)
        surgery_start.place(x=190, y=210)
        start_entry = Entry(root, width=10)
        dynamic_widgets.append(start_entry)
        start_entry.place(x=320, y=210)
        surgery_end = Label(root, text = "End Time (HH:MM):")
        dynamic_widgets.append(surgery_end)
        surgery_end.place(x=190, y=235)
        end_entry = Entry(root, width=10)
        dynamic_widgets.append(end_entry)
        end_entry.place(x=320, y=235)
        animal_weight = Label(root, text="Weight (g):")
        dynamic_widgets.append(animal_weight)
        animal_weight.place(x=165, y=260)
        weight_entry = Entry(root, width=5)
        dynamic_widgets.append(weight_entry)
        weight_entry.place(x=240, y=260)
        lorr = Label(root, text="LORR (s):")
        dynamic_widgets.append(lorr)
        lorr.place(x=295, y=260)
        lorr_entry = Entry(root, width=5)
        dynamic_widgets.append(lorr_entry)
        lorr_entry.place(x=360, y=260)

    elif choice == "Baseline":
        for i in dynamic_widgets:
            i.destroy()
        recordingtype = 'BASE'
        animalid = Label(root, text="Animal ID:")
        dynamic_widgets.append(animalid)
        animalid.place(x=20, y=210)
        animalid_entry = Entry(root, width=20)
        dynamic_widgets.append(animalid_entry)
        animalid_entry.place(x=120, y=210)
        strain = Label(root, text="Strain:")
        dynamic_widgets.append(strain)
        strain.place(x=20, y=240)
        strain_entry = Entry(root, width=20)
        dynamic_widgets.append(strain_entry)
        strain_entry.place(x=120, y=240)
    
    elif choice == "Test":
        for i in dynamic_widgets:
            i.destroy()
        replicate = Label(root, text="Rep #:")
        dynamic_widgets.append(replicate)
        replicate.place(x=20, y=210)
        replicate_entry = Entry(root, width = 20)
        dynamic_widgets.append(replicate_entry)
        replicate_entry.place(x=120, y=210)
        recordingtype = 'TEST'
    else:
        for i in dynamic_widgets:
            i.destroy()

#recording type widget
rec_var = StringVar()
checkbox_recType = Checkbutton(root, text='Recording Type', width = 15, font = font_bold, variable = rec_var, onvalue="On", offvalue="Off", command=rec_chk)
checkbox_recType.deselect()
# checkbox_recType.pack(padx=5, pady=5, side=TOP, anchor=NW)
checkbox_recType.place(x=20, y=150)

rec = StringVar()
rec.set("Select Recording Type")
dropdown_recType = OptionMenu(root, rec, "Baseline", "Post-Operation", "Test", command=rectype)
dropdown_recType.place(x=20, y=180)
# dropdown_recType.pack(side=TOP, anchor=NW)

# resolution widget
res_var = StringVar()
confirmed_res = "(640, 480)"
def confirm_resolution():
    label_confirmed_res = Label(root, text = "Confirmed Resolution: " + res_var.get()).place(x=500, y=655)
    confirmed_res = res_var.get()
    strRes = res_var.get()
    res1 = int(strRes[1:strRes.find(',')])
    res2 = int(strRes[strRes.find(',')+2:len(strRes)-1])
    update_framerate_options()
    # camera.resolution = (res1,res2)

label_resolution = Label(root, text = 'Select Camera Resolution: ', font = font_bold)
label_resolution.pack()
res_options = ["(640, 480)", "(1296, 972)", "(1296, 730)", "(1920, 1080)", "(2592, 1944)"]
res_var.set(res_options[0])
dropdown_resolution = OptionMenu(root, res_var, *res_options)
dropdown_resolution.pack()

button_confirm_resolution = Button(root, text = "Confirm", font = font_normal, command = confirm_resolution)
label_confirm_resolution = Label(root, text = "", font = font_normal)

# frame rate widget
frame_var = StringVar(root)
def confirm_framerate():
    label_confirmed_framerate = Label(root, text = "Confirmed Frame Rate: " + frame_var.get() + " fps").place(x=775, y=655)
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

# directory selector widget
label_file_explorer = Label(root, text = "Select the Directory to save your file:", font = font_normal, width = 100, height = 4)
button_file_explorer = Button(root, text = "Select Directory", font = font_normal, command = command_directoryExplorer)

# file name widget
label_filename = Label(root, text = "Enter file name:", font = font_bold)
entry_filename = Entry(root, textvariable = filename_var, font = font_normal)
button_confirm_filename = Button(root, text = "Confirm", font = font_normal, command = confirm_filename)
label_confirm_filename = Label(root, text = "", font = font_normal)

# recording duration widget
label_duration = Label(root, text = "Recording duration (in minutes):", font = font_bold)
entry_duration = Entry(root, textvariable= duration_var, font = font_normal)
button_confirm_duration = Button(root, text = "Confirm", font = font_normal, command = confirm_duration)
label_confirm_duration = Label(root, text = "", font = font_normal)

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

button_open_preview = Button(root, text = "Open Preview", font = font_normal, command = CameraON)
button_open_preview.place(x=600,y=50)

button_close_preview = Button(root, text = "Close Preview", font = font_normal, command = CameraOFF)
button_close_preview.place(x=600, y = 100)

button_start_recording = Button(root, text = "Start Recording", font = font_bold, bg = "skyblue1", command = CameraRECORD)
button_start_recording.place(x = 590, y = 175)
label_recording_status = Label(root, text = '', font = font_normal)
label_recording_status.place(x = 520, y = 210)


#progress bar

label_progress = Label(root, text = "Recording Progress:", font = font_bold).place(x = 450, y = 470)
progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 400, mode= 'determinate')
progress.place(x=450, y = 500)

label_progressbar_status = Label(root, text = "0% Complete", font = font_normal)
label_progressbar_status.place(x=600, y = 530)

def bar():
    rec_duration = duration_var.get() *60
    for second in range(int(rec_duration+1)):
        progresspct = second/rec_duration *100
        progress['value'] = progresspct
        ppct = int(progresspct)
        label_progressbar_status.configure(text = str(ppct) + "% Complete")
        root.update_idletasks()
        time.sleep(1)



# sharpness slider
slider_sharpness = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10, length=300)
slider_sharpness.place(x= 450, y=270)

label_sharpness_number = Label(root, text = "Sharpness: ", font = font_bold)
label_sharpness_number.place(x= 450, y = 250)

def confirm_sharpness():
    label_confirm_sharpness = Label(root, text="Confirmed sharpness: " + str(slider_sharpness.get()))
    sharpness = slider_sharpness.get()
    label_confirm_sharpness.place(x=450, y= 325)

button_confirm_sharpness = Button(root, text='Confirm', command=confirm_sharpness).place(x=760, y=285)

#brightness slider
slider_brightness = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10, length=300)
slider_brightness.place(x= 450, y=380)

label_brightness_number = Label(root, text = "Brightness: ", font = font_bold)
label_brightness_number.place(x= 450, y = 360)

def confirm_brightness():
    label_confirm_brightness = Label(root, text="Confirmed brightness: " + str(slider_brightness.get()))
    brightness = slider_brightness.get()
    label_confirm_brightness.place(x=450, y= 435)

button_confirm_brightness = Button(root, text='Confirm', command=confirm_brightness).place(x=760, y=395)

 
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

def create_csv():
    '''
    will have to check if the variables are confirmed.
    for the recording type fields, all labels and entry boxes are stored in the global list 'dynamic_widgets'.
    possible to access label text and entry text?

    '''
    fname = filename_var.get()
    pinumber = pinumvar.get()
    notesentry = notes_text.get()
    brightness = slider_brightness.get()
    sharpness = slider_sharpness.get()
    resolution = res_var.get()
    framerate_var = frame_var.get()



    #check if filename_var is non-empty and is confirmed
    with open(filename_var.get() + '.csv',) as f:
        w = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

        #i created a boolean flag variable that is true when the pi button is confirmed. not sure if there is a better way to do this
        if pinumvar.get() == "On" and pi_flag == True:
             w.writerow(['PiNumber', raspinum.get()])
        


    
csv_button_font = font.Font(family='Helvetica', size=20, weight='bold')
csv_button = Button(root,height=4, width=13, text="Create CSV", font=csv_button_font, padx=-5, pady=-5, command=create_csv)
csv_button.place(x=635, y=670)
csv_label_font = font.Font(family = 'Helvetica', size=10, weight='bold')
csv_label = Label(root, text="Make sure all necessary fields are entered before creating csv.", font=csv_label_font)
csv_label.place(x=575, y=775)



root.title("Data Collection PiCamera GUI")
root.geometry("1000x800")
root.resizable(width = False, height = False)

root.mainloop()