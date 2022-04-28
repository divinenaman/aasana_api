import repo
import utils

def get_yoga_pose_by_id(con, data):
    res = repo.get_pose_by_id(con, data)
    return res
