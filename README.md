# DeepFake-Detection
Real time deepfake detection
The Proposed DeepFake Detection System will detect the accuracy of authenticity the real time image.
The model is implemented using Recurrent Neural Network. We have used ’real and deepfake images’
dataset. We have created created a Labeled CSV with imagepath and their respective labels (0 - real,
1-fake) .In this we have extracted the HOG features (Histogram of Oriented Gradients ) of the images
specified in the CSV. We have used specifically Haar Cascade Classifier for face detection using OpenCV.
The System will initially record video and extract frames from it and then use it as input to the RNN
Model to predict the status of the frame. And hence the video will be classified as fake or real. The labeled
CSV is used to extract HOG feature and converted into an array which is later fed to RNN for prediction.

Architectural Overview

![image](https://github.com/user-attachments/assets/f241878c-f934-4008-b578-c6ec28c6a0bd)

