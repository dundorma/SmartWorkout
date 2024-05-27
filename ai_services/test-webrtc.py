import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np
import time
from modules.get_ice_config import get_ice_servers
from modules.pose_landmark import Detector



dir = 0
pTime = 0
st.title("webrtc Live Feed")


class LogObj:
    def __init__(self):
        self.l_count = 0
        self.r_count = 0
        self.left_flag = None
        self.right_flag = None
        self.detector = Detector()
        self.model = self.detector.mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.5, model_complexity=0, smooth_landmarks = False)
        self.log = ''



bicep = st.checkbox("Bicep Curl")
log_obj = LogObj()


def video_frame_callback(frame):
    global log_obj
    img = frame.to_ndarray(format="bgr24")

    if bicep:
        img, log_obj = detection(img, log_obj)
    print(log_obj.l_count, log_obj.r_count)
    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", 
                video_frame_callback=video_frame_callback,
                media_stream_constraints={"video": True, "audio": False},
                rtc_configuration={"iceServers": get_ice_servers()},
                )



def detection(image, log_obj):
    img = cv2.resize(image, (1280, 720))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img, result = log_obj.detector.mediapipe_detection(img, log_obj.model)
    left_count, right_count, image = log_obj.detector.extract_keypoints_bicep_curl(result, img, (log_obj.left_flag, log_obj.right_flag))
    log_obj.l_count += left_count[0]
    log_obj.r_count += right_count[0]
    log_obj.left_flag = left_count[1]
    log_obj.right_flag = right_count[1]
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
    #             (255, 0, 0), 5)
    
    cv2.putText(img, f'Left Count: {log_obj.l_count}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
    cv2.putText(img, f'Right Count: {log_obj.r_count}', (50, 150), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img, log_obj
