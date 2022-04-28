if __name__ == '__main__':
    import sys
    import os

    root_path = os.path.abspath(os.path.join(sys.path[0], '..'))
    sys.path.insert(1, root_path)

from utils import sql

def insert_landmark(con, data):
    """
        data: {
            "key" : string
        }
    """
    try:
        if data.get("key") == None:
            return { "error": True, "msg": "data insufficient to process query" } 
        
        q = "INSERT INTO landmark (key) values(?)"
        p = (data["key"],)

        res = sql.execute_query(con, q, p)
        
        return res
    except:
         return { "error": True, "msg": "error while insert data" }


if __name__ == '__main__':
    import db.setup as db

    key = input()
    con = db.get_connection()
    data = { "key": key }

    res = insert_landmark(con, data)

    print(res)