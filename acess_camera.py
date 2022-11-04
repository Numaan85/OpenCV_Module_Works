import cv2  #openCV library use to access camera

video_cap = cv2.VideoCapture(0) #it is a function help to access camera 

while True: #it use for infinite loop
    ret , video_data = video_cap.read()
    cv2.imshow("Video Camera",video_data)
    k=cv2.waitKey(1)
    if k%256 == 27: #it break when you press esc key
        break

video_cap.release()
