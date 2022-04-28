import repo
import utils

def get_yoga_pose(con):
    res = repo.get_pose(con)
    return res
