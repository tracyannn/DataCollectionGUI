#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:52:58 2021

@author: rahulpatel
"""
#%%
#load in relevant packages:
from picamera.array import PiRGBArray
from picamera import PiCamera
from picamera import PiVideoFrame
from time import sleep
from subprocess import call 
import os
import datetime
import time
import cv2
import csv
import time
#%%
#collect relevant time and date data +pi info
t = time.localtime()
experiment_start_time = str(time.strftime("%H:%M:%S", t))
Date= str(datetime.date.today().strftime("%Y%m%d"))
print ('The date and time are: ' + Date + " " + "and" + " " + experiment_start_time + ".") 
pi_number = str(2) #edit this per pi

#%%
#check if usb directory for today's data exists

ParentDir= ('/mnt/USB'+pi_number+'/Videos/')  
#('/media/pi/USB'+pi_number+'/Videos/') #250 GB flashdrive
TodaysDir= (ParentDir+Date+'/')
try:
    os.makedirs(TodaysDir)
except FileExistsError as error:
    pass
os.chdir(TodaysDir)
#%%
t = time.localtime()
experiment_start_time = str(time.strftime("%H:%M:%S", t))
Date= str(datetime.date.today().strftime("%Y%m%d"))
print ('The date and time are: ' + Date + " " + "and" + " " + experiment_start_time + ".") 
#pi_number = str(4) #causing problems
#%%
Recording_type = input('Baseline(B) or Post-Operation (P) or Test (T)? : ')
Recording_type = Recording_type.upper()
if Recording_type not in ['B', 'P', 'T']:
    exit
elif Recording_type == 'P':
    PO_type = input('Sham (S) or laparotomy (L)?: ')
    PO_type = PO_type.upper()
    Surgeon = str(input('Surgeron initials or name:'))
    SurgeryStartTime = str(input('Enter Surgery Start Time (HH:MM): '))
    SurgeryEndTime = str(input('Enter Surgery End Time (HH:MM): '))
    AnimalWeight = str(input('Enter Animal Weight (g): '))
    LORR = str(input('Enter LORR (s): '))
    d = (60*30)
    if PO_type == 'S':
        Recording_type = str('SHAM')
    if PO_type == 'L':
        Recording_type = str('LAPA')
elif Recording_type == 'B':
    Recording_type = str('BASE')
    Surgeon = str('')
    SurgeryStartTime = str('')
    SurgeryEndTime = str('')
    AnimalWeight = str('')
    LORR = str('')
    d = (60*30)
elif Recording_type == 'T':
    Test_Name = str(input('Test file name:'))
    Replicate= str('Rep' +input('Rep #: '))
    Recording_type = str('TEST')
    FileName = str(Date + '_' + Test_Name + '_'+ Recording_type + '_' + Replicate)
    d = (60*5)

#%%    
if Recording_type == 'SHAM' or Recording_type == 'BASE' or Recording_type == 'LAPA':
#if Recording_type == 'SHAM' or 'BASE' or 'LAPA':
    Strain = str(input('Strain: ')) 
    AnimalID = str(input('AnimalID: '))
    FileName = (Strain + '_'+ Recording_type + '_' + AnimalID + '_' + Date) 
#Date= datetime.date.today().strftime("%Y%m%d") #think about removing
elif Recording_type not in {'SHAM', 'BASE', 'LAPA'}:
    Strain = str('')
    AnimalID = str('')
    Surgeon = str('')
    SurgeryStartTime = str('')
    SurgeryEndTime = str('')
    AnimalWeight = str('')
    LORR = str('')
#FileName = (Date + '_' + Drug + '_'+ Recording_type + '_' + Dose + '_'+ Replicate) 
print('Your File Name is:', FileName)
name_check= input("Is this correct? (y/n): ")
name_check = name_check.upper()
if name_check != ("Y"):
    exit()
#%% Initiate the camera module with pre-defined settings.
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30
camera.brightness = 44
#42
#camera.awb_mode = "fluorescent"
camera.sharpness = 25
#camera.rotation= 180
camera_fps = str(camera.framerate)
camera_res = str(camera.resolution) 
camera_brightness= str(camera.brightness)
camera_sharpness = str(camera.sharpness)
#camera.framerate = input() #variable fps

#%% Preview with PiRGBarray/opencv
rawCapture = PiRGBArray(camera, size=(1920, 1080))
print ('Press q to quit preview.')
time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    image= frame.array  #grabbing frame
    cv2.imshow("Preview Camera 1", image) #display image
    key= cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    
    if key == ord('q'): #quit
        cv2.destroyAllWindows()
        camera.close()
        break

#%%
#from picamera.encoders import PiVideoFrame     
preview_quality = input('Preview is okay? (y/n): ')
preview_answer = preview_quality.upper() 
if preview_answer == 'Y':
    camera.close()
    camera = PiCamera()
    camera._get_framerate
    camera.resolution = (1920, 1080)
    camera.framerate = 30
    camera.brightness = 44
    #camera.awb_mode = "fluorescent"
    camera.sharpness = 25
    #camera.rotation= 180
    #PiVideoFrame()
    #camera.annotate_frame_num = True
    #camera.annotate_text = datetime.datetime.now().strftime("%H-%M-%S-%f")
    sleep(2) #allow camera to iniitlaize
    print ("Camera has started recording.")
    camera.start_recording(f'{FileName}.h264') #f-string naming integration 
    t = time.localtime()
    recording_start_time = (time.strftime("%H:%M:%S", t))
    camera.wait_recording(d) #modify duration of recording, input time in seconds
    camera.stop_recording()
    print("Recording Finished.")
    camera.close()
    t = time.localtime()
    recording_end_time = (time.strftime("%H:%M:%S", t))
    print ("Camera 1 is ready to record.")
    user_notes = str(input('Enter recording notes: '))
    t = time.localtime()
    experiment_end_time = (time.strftime("%H:%M:%S", t))
    with open(f'{FileName}.csv', 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["File_Name", "Date", "Experiment_Start_Time", 'Experiment_End_Time','Recording_type', 'Recording_start_time', 'Recording_end_time', 'Strain', 'AnimalID', 'Surgeon','SurgeryStartTime','SurgeryEndTime','AnimalWeight(g)','LORR', 'User_notes','Pi_number', 'Camera_fps', 'Camera_res', 'Camera_Brightness', 'Camera_Sharpness' ])
        writer.writerow([f'{FileName}',f'{Date}', f'{experiment_start_time}', f'{experiment_end_time}',f'{Recording_type}', f'{recording_start_time}', f'{recording_end_time}', f'{Strain}', f'{AnimalID}', f'{Surgeon}',f'{SurgeryStartTime}',f'{SurgeryEndTime}',f'{AnimalWeight}',f'{LORR}', f'{user_notes}',f'{pi_number}', f'{camera_fps}', f'{camera_res}', f'{camera_brightness}', f'{camera_sharpness}'])
else:
    camera.close()
    exit()

# make daily directory in j drive if not already there.
JParentDir= ('/home/pi/cifs/Rahul/PainFace/Data/PainGenetics/')
             #/Optimization/JDriveAccess/')
JTodaysDir= (JParentDir+Date+'/')

Jlist= os.listdir(JParentDir)

if Date in Jlist:
    pass
else: 
    MakeDir= ('sudo mkdir '+ JTodaysDir)
    call([MakeDir], shell=True)


#Transfer to JDrive
#ToJStart= ("Start file transfer: "+ time.strftime("%H:%M:%S", time.local))
CopyVideo= ('sudo cp ' + FileName + '.h264 '+ JTodaysDir)
call([CopyVideo], shell=True)
#ToJFin= ("File transfer Complete: "+ time.strftime("%H:%M:%S", time.local))
CopyCSV= ('sudo cp ' + FileName + '.csv ' + JTodaysDir)
call([CopyCSV], shell=True)
print ('The H264 and CSV have been copied to the JDrive (' +JTodaysDir+ ').')
#ExpFin = (time.strftime("%H:%M:%S", time.localtime()))
