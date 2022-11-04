import cv2

video_cap = cv2.VideoCapture(0) 

image_count =0
while True:
    ret , video_data = video_cap.read()
    cv2.imshow("Video Camera",video_data)
    wait=cv2.waitKey(1)
    if wait%256 == 27: #it break when you press esc key
        break
    elif wait%256 ==32: #it capture photo when you press space key
        img_name ="opencv_frame_{}.png".format(image_count)
        cv2.imwrite(img_name,video_data) #imwrite funtion use to store image
        print("Screenshot is taken")
        image_count+=1


video_cap.release()