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
global flag=1
def Check_Face():
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		global faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30)
			#flags = cv2.CV_HAAR_SCALE_IMAGE
		)
		
		print("Found {0} faces!".format(len(faces)))
		print("Checking for User Presence...")
		if (len(faces)==0):
			print("Detecting no User! Flag set to 0")
			flag=0
			return flag

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

def Execute_Lock():
			if (len(faces)==0):
				pyautogui.hotkey('win', 'r')
				pyautogui.typewrite("cmd\n") 
				sleep(0.500)    
				pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n exit\n") 
				break
			else: 
				print("Execute lock detected User, resuming monitoring...")
				break

while(True):
	Check_Face()
	time.sleep(10)
	if flag==0:
		#Second Check before trigger
		print("Execute Lock Detecting no User, waiting for 5 sec...")
		time.sleep(5)
		if flag==0:
		Execute_Lock()
		else:
			flag=1
		break
	break

#splash plymouth.ignore-serial-consoles quiet

	