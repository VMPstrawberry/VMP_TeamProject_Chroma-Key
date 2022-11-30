import numpy as np
import cv2

# Upload source video and background image
src = cv2.VideoCapture("Mask.mp4") # <-- This will be your source video
background_image = cv2.imread("Sea.jpg", cv2.IMREAD_COLOR)  # <-- This will be the background image by your own choice

# Get the information of the src video
src_fps = src.get(cv2.CAP_PROP_FPS) # frame per second
src_width = src.get(cv2.CAP_PROP_FRAME_WIDTH) 
src_height = src.get(cv2.CAP_PROP_FRAME_HEIGHT) 

# You can check the information here
print(" Information ".center(60, "="))
print(f"fps : {src_fps},    width : {src_width},    height : {src_height}".center(60)) 
print("="*60)

# Determine the hsv color range
hsv_lower = np.array([50, 35, 133]) 
hsv_upper = np.array([65, 110, 235])

# Make a recorder to record the result
recorder = cv2.VideoWriter("Videos/result.mp4", 
                                cv2.VideoWriter_fourcc(*'mp4v'), 
                                src_fps, (int(src_width), int(src_height))) 

print("Making your video...")
print("Please wait for a second.")
while src.isOpened():
    # Get each frame from the video
    ret, frame = src.read()

    if frame is None:
        break
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

        # Show before and after
        cv2.imshow('before (src)', frame)
        cv2.imshow('after (dst)', dst)

        # Record the modified frame
        recorder.write(dst)

        # Repeat every 10 milliseconds
        if cv2.waitKey(10) == 27: 
            # Press [Esc] to stop during the process
            # If you do that, the record would not be perfectly completed
            # Please wait for the process itself to stop to get a full video
            break

print("You're video is ready!")
src.release()
cv2.destroyAllWindows()