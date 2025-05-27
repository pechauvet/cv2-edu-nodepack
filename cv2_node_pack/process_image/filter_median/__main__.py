import numpy as np
import cv2

def filter_median(
        image: np.ndarray,
        ksize: {
            'widget_name': 'int_float_entry',
            'widget_kwargs': {'min_value': 1},
            'type': int,
        } = 3,
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    Apply the median filter to an image.
    :param image: the image to filter.
    :param ksize: the kernel size along x and y. Must be odd numbers.
    :return: a filtered image.
    """
    if ksize%2==0 :
        raise ValueError("ksize must be an odd number (1, 3, 5, 7, 9, ...) !")
    return cv2.medianBlur(image, ksize=ksize)

### alias the function defining the node as main_callable
main_callable = filter_median