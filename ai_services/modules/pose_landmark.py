from modules.calculate import calc_angle, calculate_angle
import mediapipe as mp
import numpy as np
import cv2


class Detector:
    def __init__(self):
        self.mp_holistic = mp.solutions.holistic
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose

    def mediapipe_detection(self, image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False                 
        results = model.process(image)                
        image.flags.writeable = True                  
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, results

    
    def extract_keypoints(self, results, mode):
        pass


    def extract_keypoints_bicep_curl(self, results, image = None, flag=None):
        landmarks = results.pose_landmarks.landmark
        left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        left_elbow = landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value]
        left_wrist = landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value]
        right_shoulder = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        right_elbow = landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        right_wrist = landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value]

        # Calculate angle
        left_angle = calc_angle(left_shoulder, left_elbow, left_wrist)      #  Get angle 
        right_angle = calc_angle(right_shoulder, right_elbow, right_wrist)

        if image is not None:
            cv2.putText(image,\
                    str(left_angle), \
                        tuple(np.multiply([left_elbow.x, left_elbow.y], [640,480]).astype(int)),\
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2,cv2.LINE_AA)
            cv2.putText(image,\
                    str(right_angle), \
                        tuple(np.multiply([right_elbow.x, right_elbow.y], [640,480]).astype(int)),\
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2,cv2.LINE_AA)
        left_count = 0
        right_count = 0
        
        if flag is not None:
            left_flag = flag[0]
            right_flag = flag[1]
        else:
            left_flag = None
            right_flag = None
            
        if left_angle > 160:
            left_flag = 'down'
        if left_angle < 50 and left_flag=='down':
            left_count = 1
            left_flag = 'up'

        if right_angle > 160:
            right_flag = 'down'
        if right_angle < 50 and right_flag=='down':
            right_count = 1
            right_flag = 'up'
        
        if image is not None:
            return (left_count, left_flag), (right_count, right_flag), image
        else:
            return (left_count, left_flag), (right_count, right_flag)
    

    def extract_keypoints_pushup(self, results):
        landmarks = results.pose_landmarks.landmark
        
        shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        shoulder_r = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        elbow = landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value]
        elbow_r = landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        wrist = landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value]
        wrist_r = landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value]


        left_arm_angle = calculate_angle(shoulder, elbow, wrist)
        right_arm_angle = calculate_angle(shoulder_r, elbow_r, wrist_r)





        if left_arm_angle > 160 or right_arm_angle > 160:
            up_pos = 'Up'
            display_pos = 'Up'

        if (left_arm_angle < 110 or right_arm_angle < 110) and up_pos == 'Up':
            down_pos = 'Down'
            display_pos = 'Down'    

        if (left_arm_angle > 160 or right_arm_angle > 160) and down_pos == 'Down':

            pushup_pos = "up"
            display_pos = "up"
            push_up_counter += 1

            up_pos = None
            down_pos = None
            pushup_pos = None 

        
        cv2.putText(image, 'Push Up Counter: ' + str(push_up_counter), (image_width-320, 240), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)
        