
import streamlit as st
import cv2
import numpy as np
import time
from modules.pose_landmark import Detector

detector = Detector()
model = detector.mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.5, model_complexity=0, smooth_landmarks = True)
l_count = 0
r_count = 0
dir = 0
pTime = 0
st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(1)

fps_reducer = 0
left_flag = None
right_flag = None
while run:
    try:
        if fps_reducer % 3 == 0:
            _, img = camera.read()
            img = cv2.resize(img, (1280, 720))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img, result = detector.mediapipe_detection(img, model)
            left_count, right_count, image = detector.extract_keypoints_bicep_curl(result, img, (left_flag, right_flag))
            l_count += left_count[0]
            r_count += right_count[0]
            left_flag = left_count[1]
            right_flag = right_count[1]
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)
            
            cv2.putText(img, f'Left Count: {l_count}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)
            cv2.putText(img, f'Right Count: {r_count}', (50, 150), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

            FRAME_WINDOW.image(img)
        fps_reducer+=1
    except:
        pass
else:
    st.write('Stopped')