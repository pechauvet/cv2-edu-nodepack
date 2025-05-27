import numpy as np
import cv2

def filter_gaussian_blur(
        image: np.ndarray,
        ksize: {
        'widget_name': 'literal_entry',
        'type': tuple,
        } =(7, 7),
        sigmaX: float=0.0
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    Apply the gaussian filter (normalized) to an image.
    :param image: the image to filter.
    :param ksize: the kernel size along x and y. Must be odd numbers.
    :param sigmaX: the standard deviation in X and Y direction.
    :return: A filtered image.
    """
    if ksize[0]%2==0 :
        raise ValueError("ksize[0] must be an odd number (1, 3, 5, 7, 9, ...) !")
    if ksize[1]%2==0 :
        raise ValueError("ksize[1] must be an odd number (1, 3, 5, 7, 9, ...) !")
    return cv2.GaussianBlur(image, ksize=ksize, sigmaX=sigmaX)

### alias the function defining the node as main_callable
main_callable = filter_gaussian_blur