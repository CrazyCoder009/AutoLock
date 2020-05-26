"""
pyautogui based remote/face pc lock code.
by RRN.
"""
import cv2
import pyautogui  
import time
from time import sleep

global cap,cv2,flag,faces
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def Check_Face():
	print("Check face Activated!")
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
			#flags = cv2.CV_HAAR_SCALE_IMAGE
	)
	print("Checking for User Presence...")
	print("Found {0} faces!".format(len(faces)))
	if(len(faces)==0):
		print("Detecting no User! Flag set to 0")
		flag=0
		print(flag)	
				
	else:
		print("flag set to 1!")
		flag=1
		print(flag)	
		
		
	return flag


def Execute_Lock():
	print("Execute Lock Activated!")
	pyautogui.hotkey('win', 'r')
	pyautogui.typewrite("cmd\n") 
	sleep(0.500)    
	pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n exit\n") 
				

while(True):
	time.sleep(5)
	Check_Face()
	flag = Check_Face()
	if flag==0:
		#Second Check before trigger
		print("No user detected, executing Locking Sequence..")
		Execute_Lock()
	else:
		print("User Detected..Flag reset to 1!")
		flag=1
		pass
		

#splash plymouth.ignore-serial-consoles quiet

	