import cv2

def face_detector():
	cap = cv2.VideoCapture(0) # 0 id is for webcame, it is used to open webcam

	clf = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

	while True:
		ret, frame = cap.read()

		if ret == False:
			continue

		faces = clf.detectMultiScale(frame, 1.3, 5) # image, scalling. neigh

		for x,y,w,h in faces:
			cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

		cv2.imshow("Frame", frame)

		key = cv2.waitKey(1) & 0xff # 64 bit --> 8 bit

		if key == ord('q'):
			cap.release()
			break

if __name__ == '__main__':
	face_detector()
	cv2.destroyAllWindows()