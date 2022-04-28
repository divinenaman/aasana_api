from io import BytesIO
import numpy as np
from PIL import Image

def image_str_to_nparray(img_string):
    tempBuff = BytesIO(img_string)
    image = Image.open(tempBuff)
    pixels = np.asarray(image)
    return pixels