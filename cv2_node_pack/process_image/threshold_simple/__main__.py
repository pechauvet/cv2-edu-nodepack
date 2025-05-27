import numpy as np
import cv2

def threshold_simple(
        image: np.ndarray,
        threshold: 'natural_number' = 130,
        max_value: {
            'widget_name': 'int_float_entry',
            'widget_kwargs': {'min_value': 1, 'max_value': 255},
            'type': int,
        } = 255,
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    The basic thresholding method applied to grayscale image : for each pixel, if the pixel value
    is smaller than or equal to the threshold, it is set to 0, otherwise it is set to a maximum value.
    :param image: the grayscale image to threshold.
    :param threshold: the threshold value.
    :param max_value: the maximum value.
    :return: the threshold image.
    """
    if len(image.shape) > 2 :
        raise ValueError("image must be in grayscale !")

    ret, img=cv2.threshold(image, thresh=threshold, maxval=max_value, type=cv2.THRESH_BINARY)
    return img

### alias the function defining the node as main_callable
main_callable = threshold_simple