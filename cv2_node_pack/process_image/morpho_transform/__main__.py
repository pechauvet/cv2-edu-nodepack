import numpy as np
import cv2

MORPHO_MAP = {
  'dilate'         : cv2.dilate,
  'erode'          : cv2.erode,
}

def morpho_transform(
        image: np.ndarray,
        ksize: {
            'widget_name': 'literal_entry',
            'type': tuple,
        } = (3, 3),
        iterations: 'natural_number' = 1,
        morpho_name: {
            'widget_name': 'option_menu',
            'widget_kwargs': {
                'options': tuple(MORPHO_MAP),
            },
            'type': str,
        } = 'dilate',

) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    Morphological transformations of an image : dilate or erode
    (see https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html).
    :param image: the grayscale image to process.
    :param ksize: the kernel size along x and y. Must be odd numbers.
    :param iterations: the number of iterations to apply.
    :param morpho_name: the name of the transformation : 'dilate' or 'erode'.
    :return: the transformed image.
    """
    if ksize[0]%2==0 :
        raise ValueError("ksize[0] must be an odd number (1, 3, 5, 7, 9, ...) !")
    if ksize[1]%2==0 :
        raise ValueError("ksize[1] must be an odd number (1, 3, 5, 7, 9, ...) !")
    kernel = np.ones(ksize, np.uint8)
    transform = MORPHO_MAP[morpho_name]
    return transform(image, kernel=kernel, iterations=iterations)

### alias the function defining the node as main_callable
main_callable = morpho_transform