# VMP_TeamProject_Chroma-Key
**Strawberry Team = 심유림 / 정수겸 / 윤 찬**  
**&lt;3 Awesome Things you can do with Chroma-Key>**

*Let's talk about our code !*

```python
import numpy as np
import cv2


src = cv2.VideoCapture("Mask.mp4") 
background_image = cv2.imread("Sea.jpg", cv2.IMREAD_COLOR) 

src_fps = src.get(cv2.CAP_PROP_FPS) 
src_width = src.get(cv2.CAP_PROP_FRAME_WIDTH) 
src_height = src.get(cv2.CAP_PROP_FRAME_HEIGHT) 


print(" Information ".center(60, "="))
print(f"fps : {src_fps},    width : {src_width},    height : {src_height}".center(60)) 
print("="*60)
```



***1***

* Firstly, import numpy and cv2 to use these packages.

***2***

* And then, upload the source video and a new background image by using cv2.VideoCapture() and cv2.imread() respectively.

* You have to use a new background image that is the same size as the frame in the original video.

***3***

* Next, get the information of the source video

* Use A.get(cv2.CAP_PROP_FPS) to get the frame per second of the video.

* Use A.get(cv2.CAP_PROP_WIDTH) to get the width of each frame of the video.

* Use A.get(cv2.CAP_PROP_HEIGHT) to get the height of each frame of the video.

***4***

* Print now, and check the information of the source video including FPS, width, height.
### Determining the hsv color range
```python
hsv_lower = np.array([50, 35, 133]) 
hsv_upper = np.array([90, 110, 235])
```
* We have to determine the hsv color range for distinguishing backgrounds and objects and seperate objects from backgrounds.
### Making a recorder to record the result
```python
recorder = cv2.VideoWriter("naming for your video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), src_fps, (int(src_width), int(src_height))) 
```
* If you have finished setting the hsv color range, you will save the result to your file.
* First, you should name the video and save it in mp4 file format.
* In order for this algorithm to work, the background picture to be used for the chroma key operation must be the same size as the original video, so you will use the int function to resize the backgorund picture.
### Getting each frame of the video
```python
while src.isOpened():
    ret, frame = src.read()

    if frame is None:
        break
```
* If frame is ***None***, an error would occur in a following step.
* Stop the while loop in that case using if statement.
### Reset the background & Convert color
```python
    else:
        # Reset the background
        dst = cv2.resize(background_image, (int(src_width), int(src_height))) 

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```
* Make sure to reset the background each time a frame is updated.
  * If you do not do so, you will have an afterimage of the previous frame.
* Convert the color to HSV using **cv2.cvtColor()**.
  * Since we are using cv2 methods to upload the image and video,
  * They are in BGR order when they are first uploaded.
### Masking
```python
        # Convert each frame to black & white image
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
        pixel_values = mask # just renaming

        # Cutting and pasting
        dst[pixel_values == 0] = frame[pixel_values == 0]
```
* By **cv2.inRange()**, you can change the pixel values as below:
    * chosen pixels --> 225 (WHITE)
    * unchosen pixels --> 0 (BLACK)
* So each frame turns into a black-and-white image.
* Think or it as simple paper-cutting-and-pasting process.
* The selected part would be added on your background image.
### Record the frame and check the result
```python
        # Show before and after
        cv2.imshow('Before (src)', frame)
        cv2.imshow('After (dst)', dst)

        # Record the modified frame
        recorder.write(dst)

        # Repeat every 10 milliseconds
        if cv2.waitKey(10) == 27: 
            # Press [Esc] to stop during the process
            # If you do that, the record would not be perfectly completed
            # Please wait for the process itself to stop to get a full video
            break

print("Your video is ready!")
src.release()
cv2.destroyAllWindows()
```



