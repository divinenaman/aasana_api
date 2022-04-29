import repo
import utils
import re
import utils.image as image_utils
import base64
import model

def compare_pose(con, pose_model, data):
    try:
        
        img = data.img

        img = re.sub(r'data:image/.*;base64,', '', img)
        im_bytes = base64.b64decode(img)

        img = image_utils.image_str_to_nparray(im_bytes)

        landmark_obj, landmark_dict = model.get_landmark(pose_model, img)
        
        if not landmark_obj:
            return { "error": False, "msg": "No Joints Found" }

        img_with_landmark = model.draw_landmark(landmark_obj, img)        

        d = { "pose_id": data.pose_id }
        res = repo.get_pose_landmark_angle(con, d)

        if res["error"]:
            print(res["msg"])
            return { "error": True, "msg": "something went wrong" }

        required_landmark_angle = res["msg"]

        res = repo.get_landmark(con)
        if res["error"]:
            print(res["msg"])
            return { "error": True, "msg": "something went wrong" }
        
        landmark_keys = res["msg"]
        landmark = {}

        for idx, key in landmark_keys:   
            landmark[idx] = key

        angles = []
        
        for idx, pose_id, l1, l2, lmid, min_val, max_val  in required_landmark_angle:
            b = landmark_dict[landmark[l1].upper()]
            a = landmark_dict[landmark[lmid].upper()]
            c = landmark_dict[landmark[l2].upper()]

            angle = model.calculate_angle(b,a,c)
            is_angle_correct = False

            if angle >= min_val and angle <= max_val:
                is_angle_correct = True

            d = { "angle": angle, "is_angle_correct": is_angle_correct, "angle_between": landmark[l1].upper() + "," + landmark[lmid].upper() + "," + landmark[l2].upper()  }
            
            angles.append(d)
    
        return { "error": False, "msg": angles }
    
    except Exception as e: 
        print(str(e))
        return { "error": True, "msg": e }  