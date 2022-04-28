if __name__ == '__main__':
    import sys
    import os

    root_path = os.path.abspath(os.path.join(sys.path[0], '..'))
    sys.path.insert(1, root_path)

from utils import sql

def insert_pose(con, data):
    """
        data: {
            "name" : string,
            "description" : string
        }
    """
    try:
        if data.get("name") == None or data.get("desc") == None:
            return { "error": True, "msg": "data insufficient to process query" } 
        
        q = "INSERT INTO yoga_pose (name, desc) values(?,?)"
        p = (data["name"], data["desc"])

        res = sql.execute_query(con, q, p)
        
        return res
    except:
         return { "error": True, "msg": "error while insert data" }


if __name__ == '__main__':
    import db.setup as db

    name = input()
    desc = input()
    con = db.get_connection()
    data = { "name": name, "desc": desc }

    res = insert_pose(con, data)

    print(res)