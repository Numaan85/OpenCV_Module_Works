import cv2

video_cap = cv2.VideoCapture(0)

image_counter =0
while True:
    ret , video_data = video_cap.read()
    cv2.imshow("Video Camera",video_data)
    k=cv2.waitKey(1)
    if k%256 == 27:
        break

video_cap.release()