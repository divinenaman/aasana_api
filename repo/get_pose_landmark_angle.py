if __name__ == '__main__':
    import sys
    import os

    root_path = os.path.abspath(os.path.join(sys.path[0], '..'))
    sys.path.insert(1, root_path)

from utils import sql

required = ["pose_id"]

def get_pose_landmark_angle(con, data):
    """
        data: {
            "pose_id" : int FK
        }
    """
    try:
        has_data = list(filter(lambda x: data.get(x) != None, required))
        
        if len(has_data) != len(required):
            return { "error": True, "msg": "data insufficient to process query" } 
        
        q = f"SELECT * FROM pose_landmark_angle WHERE pose_id = ?"
        p = tuple(map(lambda x: data.get(x), required))

        res = sql.query_table(con, q, p)
        
        return res
    except Exception as e:
         return { "error": True, "msg": e }


if __name__ == '__main__':
    import db.setup as db

    d = int(input())
    data = { "pose_id": d }
    
    con = db.get_connection()
    res = get_pose_landmark_angle(con, data)

    print(res)