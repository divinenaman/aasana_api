if __name__ == '__main__':
    import sys
    import os

    root_path = os.path.abspath(os.path.join(sys.path[0], '..'))
    sys.path.insert(1, root_path)

from utils import sql

def get_landmark(con):
    try:
        q = f"SELECT id, key FROM landmark"
        res = sql.query_table(con, q)
        
        return res
    except Exception as e:
         return { "error": True, "msg": e }


if __name__ == '__main__':
    import db.setup as db
    
    con = db.get_connection()
    res = get_landmark(con)

    print(res)