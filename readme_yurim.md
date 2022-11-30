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
* By **cv2.inRange()**, you can change the pixels as below:
    * chosen pixels --> 225 (WHITE)
    * unchosen pixels --> 0 (BLACK)
* So each frame turns into a black-and-white image.
* Think or it as simple paper-cutting-and-pasting process.
* The selected part would be added on your background image.
