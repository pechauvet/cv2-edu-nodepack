import numpy as np
import cv2

def filter_bilateral(
        image: np.ndarray,
        diameter: 'natural_number' = 9,
        sigmaColor: 'natural_number' = 50,
        sigmaSpace: 'natural_number' = 50
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    Applies the bilateral filter to an image (see https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html).
    :param image: the image to filter.
    :param diameter: diameter of each pixel neighborhood that is used during filtering.
    :param sigmaColor: filter sigma in the color space.
    :param sigmaSpace: filter sigma in the coordinate space.
    :return: the filtered image.
    """
    return cv2.bilateralFilter(image, d=diameter, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)

### alias the function defining the node as main_callable
main_callable = filter_bilateral