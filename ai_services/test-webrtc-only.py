import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np
import time
from modules.pose_landmark import Detector



dir = 0
pTime = 0
st.title("webrtc Live Feed")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example", 
                video_frame_callback=video_frame_callback,
                media_stream_constraints={"video": True, "audio": False},
                rtc_configuration={
                    "urls": [
                    "stun:stun.l.google.com:19302"]
                    }
                )

