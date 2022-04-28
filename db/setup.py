import sqlite3
from sqlite3 import Error
from db.create_query import query_dict
import numpy as np
import io
import os

compressor = 'zlib'  # zlib, bz2

def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    # zlib uses similar disk size that Matlab v5 .mat files
    # bz2 compress 4 times zlib, but storing process is 20 times slower.
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())  # zlib, bz2

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    out = io.BytesIO(out.read())
    return np.load(out)

sqlite3.register_adapter(np.ndarray, adapt_array)
sqlite3.register_converter("array", convert_array)

def create_connection(path=os.path.join(os.getcwd(),"db","data","test.db")):
    connection = None
    print(path)
    try:
        connection = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    create_tables(connection)
    return connection

def get_connection(path=os.path.join(os.getcwd(),"db","data","test.db")):
    connection = None
    print(path)
    try:
        connection = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def create_tables(con):
    cur = con.cursor()
    cur.execute(query_dict["create_pose_table"])
    cur.execute(query_dict["create_landmark_table"])
    cur.execute(query_dict["create_pose_landmark_angle_table"])
    cur.execute(query_dict["create_pose_tag_table"])
    con.commit()

def test(con):
    cur = con.cursor()
    cur.execute("insert into yoga_pose (name, desc) values (?,?)",("shavaasan", "Relaxation Pose"))
    con.commit()

    a = cur.execute("SELECT * from yoga_pose")
    print(a.fetchall())

    con.close()

def test_arr(con):
    cur = con.cursor()
    q = "SELECT name,type from yoga_pose"
    res = cur.execute(q)
    x = []
    y = []
    for name,t in res.fetchall():
        y.append(name)
        x.append(t)

    print(x, y)
    con.close()