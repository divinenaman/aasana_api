from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import model
import db.setup as db
import controllers
import utils.image as image_utils
import re
import base64
import repo

app = FastAPI()
con = db.create_connection()
pose_model = model.get_media_pipe_model()

@app.get("/pose")
def pose():
    res = controllers.get_yoga_pose(con)   
    return res

class pose_compare_body(BaseModel):
    img: str
    pose_id: int

@app.post("/pose/compare")
def pose_compare(data: pose_compare_body):
    res = controllers.compare_pose(con, pose_model, data)
    return res