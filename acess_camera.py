import cv2

video_cap = cv2.VideoCapture(0)

image_counter =0
while True:
    ret , video_data = video_cap.read()
    cv2.imshow("Video Camera",video_data)
    k=cv2.waitKey(1)
    if k%256 == 27:
        break
    elif k%256 ==32:
        img_name ="opencv_frame_{}.png".format(image_counter)
        cv2.imwrite(img_name,video_data)
        print("Screenshot is taken")
        image_counter+=1


video_cap.release()