import math
import cv2
import numpy as np
import mediapipe as mp

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose

# Initializing mediapipe drawing class, useful for annotation.
mp_drawing = mp.solutions.drawing_utils 

def get_landmark(pose_model, img):
    results = pose_model.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    landmarks_dict = {}
    height, width, _ = img.shape

    if results.pose_landmarks:
        for i in range(len(results.pose_landmarks.landmark)):
            landmark = results.pose_landmarks.landmark[i]    
            landmarks_dict[mp_pose.PoseLandmark(i).name] = ((int(landmark.x * width), int(landmark.y * height),(landmark.z * width))) 

    return results.pose_landmarks, landmarks_dict

def draw_landmark(landmarks, img):
    img_copy = img.copy()
    
    if landmarks:
        mp_drawing.draw_landmarks(image=img_copy, landmark_list=landmarks, connections=mp_pose.POSE_CONNECTIONS)

    return img_copy

def calculate_angle(landmark1, landmark2, landmark3):
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2
    x3, y3, _ = landmark3

    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    
    if angle < 0:
        angle += 360
    
    return angle

