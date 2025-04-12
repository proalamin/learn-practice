import cv2

cam =cv2.VideoCapture(1)

while True:
   _, frame = cam.read()
   cv2.imshow("Camera", frame)
   cv2.waitKey(1)