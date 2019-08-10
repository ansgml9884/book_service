import pyzbar.pyzbar as pyzbar
import cv2
def barcode():
	cap = cv2.VideoCapture(cv2.CAP_DSHOW)
	ret,img= cap.read()
	i = 0
	barcode_data= None
	while(True):
		ret, img = cap.read()
		if not ret:
			continue
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		decoded = pyzbar.decode(gray)
		cv2.imshow('img',img)
		if ((cv2.waitKey(1) & 0xFF == ord('q')) or decoded!=[]) :
			for d in decoded:
				barcode_data = d.data.decode("utf-8")
				print(barcode_data)
				cap.release()
				cv2.destroyAllWindows()
				return barcode_data