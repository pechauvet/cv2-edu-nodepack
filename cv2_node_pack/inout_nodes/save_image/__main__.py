import cv2
import numpy as np

def rescale_image(image, percent:int=75) -> np.ndarray:
    """
    Get an image resized as a percentage of the original image's width and height.
    :param image: the input image in opencv format (ndarray).
    :param percent: the percentage of rescale.
    :return: the rescaled image.
    """
    width = int(image.shape[1] * percent / 100)
    height = int(image.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

def save_image(
    image  : np.ndarray,
    path   : 'image_path' = '.',
    percent_resize: {
        'widget_name': 'int_float_entry',
        'widget_kwargs': {'min_value': 20, 'max_value': 100},
        'type': int,
    } = 100,
):
    """
    Save an image in a file.
    :param image: the image (in opencv format - ndarray) to save.
    :param path: the path of the file.
    :param percent_resize: a resize percentage, between 20% and 100% (no resize).
    """
    if percent_resize!=100 :
        image = rescale_image(image, percent_resize)
    cv2.imwrite(path, image)

main_callable = save_image