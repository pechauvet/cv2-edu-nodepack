import numpy as np
import cv2

def threshold_otsu(
        image: np.ndarray,
        max_value: {
            'widget_name': 'int_float_entry',
            'widget_kwargs': {'min_value': 1, 'max_value': 255},
            'type': int,
        } = 255,
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    The basic thresholding method applied to grayscale image with threshold automatically
    computed by the Otsu method.
    :param image: the grayscale image to threshold.
    :param max_value: the maximum value.
    :return: the threshold image.
    """
    if len(image.shape) > 2 :
        raise ValueError("image must be in grayscale !")

    ret, img=cv2.threshold(image, thresh=0, maxval=max_value, type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img

### alias the function defining the node as main_callable
main_callable = threshold_otsu