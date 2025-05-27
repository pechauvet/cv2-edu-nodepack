import numpy as np
import cv2

def canny_edges(
        image: np.ndarray,
        threshold1: {
            'widget_name': 'int_float_entry',
            'widget_kwargs': {'min_value': 1, 'max_value': 255},
            'type': int,
        } = 30,
        threshold2: {
            'widget_name': 'int_float_entry',
            'widget_kwargs': {'min_value': 1, 'max_value': 255},
            'type': int,
        } = 150,
        aperture_size: 'natural_number' = 3
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    The canny edge detector.
    An edge detection function that uses a multi-stage algorithm to detect a wide range of edges in images.
    It was developed by John F. Canny in 1986 (from https://en.wikipedia.org/wiki/Canny_edge_detector).
    :param image: the grayscale image to process.
    :param threshold1: any edge with intensity gradient below threshold1 is discarded.
    :param threshold2: any edge with intensity gradient more than threshold2 are preserved.
    :param aperture_size: aperture size for the Sobel operator.
    :return: a grayscale image with significant edges.
    """
    return cv2.Canny(image, threshold1=threshold1, threshold2=threshold2,
                     apertureSize=aperture_size)

### alias the function defining the node as main_callable
main_callable = canny_edges