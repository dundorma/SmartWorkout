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


    def extract_keypoints_bicep_curl(self, results):
        landmarks = results.pose_landmarks.landmark
        left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_elbow = landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW]
        left_wrist = landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST]
        right_shoulder = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER]
        right_elbow = landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW]
        right_wrist = landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST]

        # Calculate angle
        left_angle = calc_angle(left_shoulder, left_elbow, left_wrist)      #  Get angle 
        right_angle = calc_angle(right_shoulder, right_elbow, right_wrist)

        # Visualize angle
        cv2.putText(image,\
                str(left_angle), \
                    tuple(np.multiply([left_elbow.x, left_elbow.y], [640,480]).astype(int)),\
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2,cv2.LINE_AA)
        cv2.putText(image,\
                str(right_angle), \
                    tuple(np.multiply([right_elbow.x, right_elbow.y], [640,480]).astype(int)),\
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2,cv2.LINE_AA)
    
        # Counter 
        if left_angle > 160:
            left_flag = 'down'
        if left_angle < 50 and left_flag=='down':
            left_count += 1
            left_flag = 'up'

        if right_angle > 160:
            right_flag = 'down'
        if right_angle < 50 and right_flag=='down':
            right_count += 1
            right_flag = 'up'
    

    def extract_keypoints_pushup(self, results):
        landmarks = results.pose_landmarks.landmark
        
        shoulder = [landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        shoulder_r = [landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        elbow = [landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].x,  landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        elbow_r = [landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,  landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        wrist = [landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].y]
        wrist_r = [landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

        nose = [landmarks[self.mp_pose.PoseLandmark.NOSE.value].x,landmarks[self.mp_pose.PoseLandmark.NOSE.value].y]


        left_hip = [landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].y]
        right_hip = [landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].y]
        left_knee = [landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value].y]
        right_knee = [landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
        left_ankle = [landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
        right_ankle = [landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

        midpoint_shoulder_x = (int(shoulder[0] * image_width )+ int(shoulder_r[0] * image_width))/2

        midpoint_shoulder_y = (int(shoulder[1] * image_height )+ int(shoulder_r[1] * image_height))/2

        midpoint_hip_x = (int(left_hip[0] * image_width )+ int(right_hip[0] * image_width))/2
        midpoint_hip_y = (int(left_hip[1] * image_height)+ int(right_hip[1] * image_height))/2



        based_mid_x = int((midpoint_shoulder_x + midpoint_hip_x)/2)
        based_mid_y = int((midpoint_shoulder_y + midpoint_hip_y)/2)

        neck_point_x = (int(nose[0] * image_width )+ int(midpoint_shoulder_x))/2
        neck_point_y = (int(nose[1] * image_height) + int(midpoint_shoulder_y))/2


        left_arm_angle = int(calculate_angle(shoulder, elbow, wrist))
        right_arm_angle = int(calculate_angle(shoulder_r, elbow_r, wrist_r))
        left_leg_angle = int(calculate_angle(left_hip, left_knee, left_ankle))

        right_leg_angle = int(calculate_angle(right_hip, right_knee, right_ankle))


        
        left_arm_length = np.linalg.norm(np.array(shoulder) - np.array(elbow))

        # ppm = 10.8

        # left_arm_motion = left_arm_angle* left_arm_length

        # left_arm_motion = left_arm_motion/ppm

        #newpoint_left = [left_hip[0] +5,right_hip[0] +5]

        mid_point_x = (int(left_hip[0] * image_width )+ int(right_hip[0] * image_width))/2
        mid_point_y = (int(left_hip[1] * image_height)+ int(right_hip[1] * image_height))/2

        #cv2.circle(image,(int(mid_point_x) ,int(mid_point_y +30 )),15,(0,255,255),-1)



        if left_arm_angle > 160:
            up_pos = 'Up'
            display_pos = 'Up'

        if left_arm_angle < 110 and up_pos == 'Up':
            down_pos = 'Down'
            display_pos = 'Down'    

        if left_arm_angle > 160 and down_pos == 'Down':

            pushup_pos = "up"
            display_pos = "up"
            push_up_counter += 1

            up_pos = None
            down_pos = None
            pushup_pos = None 

        
        #visulaize the angle
        cv2.line(image,(int(shoulder[0]* image_width),int(shoulder[1]* image_height)),(int(neck_point_x),int(neck_point_y)),(line_color),3)

        cv2.line(image,(int(shoulder_r[0]* image_width),int(shoulder_r[1]* image_height)),(int(neck_point_x),int(neck_point_y)),(line_color),3)

        cv2.line(image,(int(shoulder[0]* image_width),int(shoulder[1]* image_height)),(int(elbow[0]* image_width),int(elbow[1]* image_height)),(line_color),3)
        cv2.line(image,(int(shoulder_r[0]* image_width),int(shoulder_r[1]* image_height)),(int(elbow_r[0]* image_width),int(elbow_r[1]* image_height)),(line_color),3)

        
            

            #neck to mid point
        cv2.line(image,(int(neck_point_x),int(neck_point_y)),(int(based_mid_x),int(based_mid_y)),(line_color),3,cv2.LINE_4)

            #mid to hips
        cv2.line(image,(int(based_mid_x),int(based_mid_y)),(int(left_hip[0] * image_width ),(int(left_hip[1] * image_height))),(line_color),3,cv2.LINE_8)

        cv2.line(image,(int(based_mid_x),int(based_mid_y)),(int(right_hip[0] * image_width ),(int(right_hip[1] * image_height))),(line_color),3,cv2.LINE_8)


            ##neck point


        cv2.circle(image,(int(neck_point_x),int(neck_point_y)),4,(line_color),5)

            #create new circles at that place
        cv2.circle(image,(int(shoulder[0]* image_width),int(shoulder[1]* image_height)),4,(line_color),3)
        cv2.circle(image,(int(shoulder_r[0]* image_width),int(shoulder_r[1]* image_height)),4,(line_color),3)
            #mid point
        cv2.circle(image,(int(based_mid_x),int(based_mid_y)),4,(line_color),5)



        cv2.rectangle(image,(image_width,0),(image_width-330,250),(0,0,0),-1)
        cv2.putText(image,'Angles',(image_width-300,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
        cv2.putText(image, 'Left Elbow Angle: ' + str(left_arm_angle), (image_width-290, 70), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, 'Right Elbow Angle: ' + str(right_arm_angle), (image_width-290, 110), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, 'Left Knee Angle: ' + str(left_leg_angle), (image_width-290, 150), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image, 'Right Knee Angle: ' + str(right_leg_angle), (image_width-290, 190), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.putText(image, 'Push Up Counter: ' + str(push_up_counter), (image_width-320, 240), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)
        