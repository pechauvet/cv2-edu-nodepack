import numpy as np
import cv2

THRESHOLD_METHOD_MAP = {
  'Simple Mean'             : cv2.ADAPTIVE_THRESH_MEAN_C,
  'Gaussian-weighted Mean'  : cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
}

def threshold_adaptive(
        image: np.ndarray,
        max_value: {
            'widget_name': 'int_float_entry',
            'widget_kwargs': {'min_value': 1, 'max_value': 255},
            'type': int,
        } = 255,
        threshold_method: {
            'widget_name': 'option_menu',
            'widget_kwargs': {
                'options': tuple(THRESHOLD_METHOD_MAP),
            },
            'type': str,
        } = 'Gaussian-weighted Mean',
        ksize: 'natural_number' = 9,
        constant: {
            'widget_name': 'int_float_entry',
            'widget_kwargs': {'min_value': 0, 'max_value': 255},
            'type': int,
        } = 2,
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    Adaptive thresholding method (see https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html).
    :param image: the grayscale image to threshold.
    :param max_value: the max gray value to apply.
    :param threshold_method: the thresholding method.
    :param ksize: the kernel size.
    :param constant: the C constant.
    :return: the grayscale image, resulting from threshold operation.
    """
    if ksize%2==0 :
        raise ValueError("ksize must be an odd number (1, 3, 5, 7, 9, ...) !")
    if len(image.shape) > 2 :
        raise ValueError("image must be in grayscale !")

    img=cv2.adaptiveThreshold(image, maxValue=max_value,
                              adaptiveMethod=THRESHOLD_METHOD_MAP[threshold_method],
                              thresholdType=cv2.THRESH_BINARY_INV,
                              blockSize=ksize,
                              C=constant)
    return img

### alias the function defining the node as main_callable
main_callable = threshold_adaptive