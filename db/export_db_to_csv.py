if __name__ == '__main__':
    import sys
    import os

    root_path = os.path.abspath(os.path.join(sys.path[0], '..'))
    sys.path.insert(1, root_path)

import db.setup as db
import sqlite3
import os
import csv


def serialize_to_csv(con, table, path):
    cur = con.cursor()
    cur.execute(f"select * from {table}")
    
    with open(path, "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter="\t")
      csv_writer.writerow([i[0] for i in cur.description])
      csv_writer.writerows(cur)

if __name__ == '__main__':
    con = db.get_connection()

    tables = ["yoga_pose","yoga_pose_tag","pose_landmark_angle","landmark"]

    for t in tables:
        try:
            path = os.path.join(sys.path[1], "db", "data", "csv", f"{t}.csv")
            serialize_to_csv(con, t, path)
        except Exception as e:
            print(e)