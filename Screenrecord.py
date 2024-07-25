import pyautogui
import cv2
import numpy as np
import os
import datetime
import time
import dlib

# Function to detect faces and crop the frame to show only the face
def detect_faces(img):
    faces = face_detector(img, 1)
    face_count = len(faces)
    face_img_resized = None  # Initialize outside loop
    for face in faces:
        x = face.left() - 20  # Decrease x by 20 pixels to include more area on the left side
        y = face.top() - 20  # Decrease y by 20 pixels to include more area on the top side
        w = face.right() - x + 40  # Increase w by 40 pixels to include more area on the right side
        h = face.bottom() - y + 40  # Increase h by 40 pixels to include more area on the bottom side
        # Ensure x, y, w, h are within the image bounds
        x = max(0, x)
        y = max(0, y)
        w = min(w, img.shape[1] - x)
        h = min(h, img.shape[0] - y)
        # Crop the frame to show only the face
        face_img = img[y:y+h, x:x+w]
        # Resize the cropped face to a fixed size for better visualization
        face_img_resized = cv2.resize(face_img, (200, 200))
        # Draw rectangle around the face on the original frame
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return img, face_img_resized, face_count

# Initialize dlib's face detector
face_detector = dlib.get_frontal_face_detector()

# Specify folder for saving the screen recorded video
video_save_dir = "D://Facemesh//Videosdetect//Recordings"

# Specify folder for saving the frames
frames_save_dir = "D://Facemesh//Videosdetect//Frames"

# Ensure folders exist
os.makedirs(video_save_dir, exist_ok=True)
os.makedirs(frames_save_dir, exist_ok=True)

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of output video file
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
video_filename = os.path.join(video_save_dir, f"Recording_{timestamp}.avi")

# Specify frames rate
fps = 60.0

# Creating a VideoWriter object
out = cv2.VideoWriter(video_filename, codec, fps, resolution)

# Create an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

# Capture and save the screen recording
print("Recording screen... Press 'q' to stop or recording will stop after 3 minutes.")
start_time = time.time()
while (time.time() - start_time) < 180:  # 3 minutes limit
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert color from BGR(Blue, Green, Red) to RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform face detection on the frame
    frame_with_faces, face_img_resized, face_count = detect_faces(frame)

    # Write frame to the output video file
    out.write(frame_with_faces)

    # Optional: Display the recording screen with faces detected
    cv2.imshow('Live', frame_with_faces)

    # Save frame as an image file if faces are detected
    if face_count > 0:
        # Save frame to the output video file
        out.write(frame_with_faces)

        # Save cropped face as an image file
        cv2.imwrite(os.path.join(frames_save_dir, f'frame_{timestamp}_{int(time.time())}.jpg'), face_img_resized)

    # Stop recording when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoWriter object
out.release()

# Destroy all windows
cv2.destroyAllWindows()

print("Screen recording saved successfully.")
