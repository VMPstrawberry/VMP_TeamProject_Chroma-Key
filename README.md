# VMP_TeamProject_Chroma-Key
**Strawberry Team = 심유림 / 정수겸 / 윤 찬**  
**&lt;Awesome Things you can do with Chroma-Key>**

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




