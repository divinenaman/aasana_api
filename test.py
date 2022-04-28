import db.setup as db

con = db.get_connection()

q = "DROP Table pose_landmark_angle"
cur = con.cursor()

cur.execute(q)
con.close()