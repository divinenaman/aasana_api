if __name__ == '__main__':
    import sys
    import os

    root_path = os.path.abspath(os.path.join(sys.path[0], '..'))
    sys.path.insert(1, root_path)

from utils import sql

def get_pose(con):
    """
        data: {
            "name" : string,
            "description" : string
        }
    """
    try:
        q = "SELECT * FROM yoga_pose"
        res = sql.query_table(con, q)
        
        return res
    except:
         return { "error": True, "msg": res }


if __name__ == '__main__':
    import db.setup as db

    con = db.get_connection()
    res = get_pose(con)

    print(res)