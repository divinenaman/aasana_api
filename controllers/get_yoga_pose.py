import repo
import utils

def get_yoga_pose(con):
    res = repo.get_pose(con)
    
    data = []
    if not res['error']:
        for idx, name, desc in res['msg']:
            data.append({ "id": idx, "name": name, "desc": desc })
        res['msg'] = data

    return res
