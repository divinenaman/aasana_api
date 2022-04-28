if __name__ == '__main__':
    import sys
    import os

    root_path = os.path.abspath(os.path.join(sys.path[0], '..'))
    sys.path.insert(1, root_path)

from utils import sql

required = ["pose_id", "landmark_1", "landmark_2", "intersection_landmark", "min_value", "max_value"]

def insert_pose_landmark_angle(con, data):
    """
        data: {
            "pose_id" : int FK,
            "landmark_1": int FK,
            "landmark_2": int FK,
            "intersection_landmark": int FK,
            "min_value": int,
            "max_value" int
        }
    """
    try:
        has_data = list(filter(lambda x: data.get(x) != None, required))
        
        if len(has_data) != len(required):
            return { "error": True, "msg": "data insufficient to process query" } 
        
        q = f"INSERT INTO pose_landmark_angle ({','.join(required)}) values({','.join(['?'] * len(required))})"
        p = tuple(map(lambda x: data.get(x), required))

        res = sql.execute_query(con, q, p)
        
        return res
    except Exception as e:
         return { "error": True, "msg": e }


if __name__ == '__main__':
    import db.setup as db

    d = input().split(';')
    
    data = {}
    for i, val in enumerate(d):
        data[required[i]] = val
    con = db.get_connection()
    res = insert_pose_landmark_angle(con, data)

    print(res)