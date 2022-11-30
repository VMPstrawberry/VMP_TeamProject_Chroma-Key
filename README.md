# VMP_TeamProject_Chroma-Key
**Strawberry Team = 심유림 / 정수겸 / 윤 찬**  
**&lt;Awesome Things you can do with Chroma-Key>**

Let's talk about our code !

![code1](https://user-images.githubusercontent.com/119425924/204765876-38f0a76a-06ba-43bb-9100-20346f8a639e.png)

***1-2***

* Firstly, import numpy and cv2 to use these packages.

***5-6***

* And then, Upload the source video and a new background image by using cv2.VideoCapture() and cv2.imread() respectively.

* You have to use a new background image that is the same size as the frame in the original video.

***8-10***

* Next, get the information of the source video

* Use A.get(cv2.CAP_PROP_FPS) to get the frame per second of the video.

* Use A.get(cv2.CAP_PROP_WIDTH) to get the width of each frame of the video.

* Use A.get(cv2.CAP_PROP_HEIGHT) to get the height of each frame of the video.

***13-15***

* Print now, and check the information of the source video including FPS, width, height.




