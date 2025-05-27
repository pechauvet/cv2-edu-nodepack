import numpy as np
import cv2

def filter_blur(
        image: np.ndarray,
        ksize: {
        'widget_name': 'literal_entry',
        'type': tuple,
        } =(7, 7)
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    Apply the smoothing filter (normalized one-matrix) to an image.
    :param image: the image to filter.
    :param ksize: the kernel size along x and y. Must be odd numbers.
    :return: the filtered image.
    """
    if ksize[0]%2==0 :
        raise ValueError("ksize[0] must be an odd number (1, 3, 5, 7, 9, ...) !")
    if ksize[1]%2==0 :
        raise ValueError("ksize[1] must be an odd number (1, 3, 5, 7, 9, ...) !")

    return cv2.blur(image, ksize=ksize)

### alias the function defining the node as main_callable
main_callable = filter_blur