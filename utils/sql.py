def execute_query(con, query, data):
    try:
        cur = con.cursor()
        res = cur.execute(query, data)
        con.commit()
        return { "error": False, "msg": "query executed successfully" }
    except Exception as e:
        return { "error": True, "msg": e }

def query_table(con, query, data = None):
    try:
        cur = con.cursor()
        
        if data != None:
            res = cur.execute(query, data)
        else:
            res = cur.execute(query)
        
        rows = res.fetchall()
        con.commit()
        
        return { "error": False, "msg": rows }
    except Exception as e:
        return { "error": True, "msg": e }