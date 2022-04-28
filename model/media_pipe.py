import mediapipe as mp

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose

def get_media_pipe_model():
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
    return pose