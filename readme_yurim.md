***
```python
while src.isOpened():
    # Get each frame from the video
    ret, frame = src.read()

    if frame is None:
        break
```
* If frame is ***None***, an error would occur in a following step.
* Stop the while loop in that case using if statement.
---
```python
    else:
        # Reset the background
        dst = cv2.resize(background_image, (int(src_width), int(src_height))) 

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Convert each frame to black & white image
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
        pixel_values = mask # just renaming

        # Cutting and pasting
        dst[pixel_values == 0] = frame[pixel_values == 0]
```
* Make sure to reset the background each time a frame is updated.
  * If you do not do so, you will have an afterimage of the previous frame.
* Convert the color to HSV using cv2.cvtColor().
  * Since we are using cv2.imread() to upload the image and video,
  * They are in BGR order when they are first uploaded.
