import numpy as np
import cv2
from pathlib import Path

current_file_path = Path(__file__)

dummy_image_path = \
  current_file_path.parent / 'full_saturation_spectrum.png'
image_str_path = str(dummy_image_path)

def isgray(img):
    if len(img.shape) < 3: return True
    if img.shape[2]  == 1: return True
    b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]
    if (b==g).all() and (b==r).all(): return True
    return False

def open_image(
      filepath : {
        'widget_name': 'image_preview',
        'type' : str
      } = image_str_path,
    ) -> [
      {'name' : 'image',  'type': np.ndarray},
      {'name' : 'width',  'type': int},
      {'name' : 'height', 'type': int},
      {'name' : 'size',   'type': tuple},
      {'name' : 'mode',   'type': str},
    ]:
    """
    Read an image and load it in memory in opencv format - i.e. as a numpy multidimensional array (type ndarray).
    :param filepath: the image file path.
    :return: the numpy multidimensional array encoding the image.
    """
    image = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    dim = image.shape
    height = dim[0]
    width = dim[1]
    if isgray(image) :
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_format='Gray'
    else :
        img_format = 'RGBA' if image.shape[2] == 4 else 'RGB'

    return {
        'image': image,
        'width': width,
        'height': height,
        'size': dim,
        'mode': img_format,
    }

### function aliasing
main_callable = open_image