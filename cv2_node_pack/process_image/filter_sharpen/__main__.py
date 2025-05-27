import numpy as np
import cv2

def filter_sharpen(
        image: np.ndarray,
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    Sharpen an image (enhance the edges and fine details in the image).
    :param image: the image to filter.
    :return: a filtered (sharpened) image.
    """
    # Create the sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # Return the sharpened image
    return cv2.filter2D(image, -1, kernel)

### alias the function defining the node as main_callable
main_callable = filter_sharpen