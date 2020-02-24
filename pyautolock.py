"""
pyautogui based remote/face pc lock code.
by RRN.
"""
import cv2
import pyautogui  
import time
from time import sleep

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	time.sleep(10)
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

	#print("Found {0} faces!".format(len(faces)))
	#print("Checking for User Presence...")
	
	
	#First Check for face 
	if(len(faces)==0):	
		print("Detecting no User, waiting for 2 sec...")
		time.sleep(2)
		for i in range(0,5):
			# Second Check for face 
			time.sleep(1)
			if (len(faces)==0):
				pyautogui.hotkey('win', 'r')
				pyautogui.typewrite("cmd\n") 
				sleep(0.500)    
				pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n exit\n") 
				break
			else: 
				print("User Detected, resuming monitoring...")
				break
			
		break	
	
	
	# Rectangle around the faces
	'''for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
'''

	# Display the resulting frame
	'''cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		'''				
cap.release()
cv2.destroyAllWindows()

#splash plymouth.ignore-serial-consoles quiet

	