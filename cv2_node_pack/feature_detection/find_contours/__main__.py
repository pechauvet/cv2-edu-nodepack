import numpy as np
import cv2

def find_contours(
        image: np.ndarray,
) -> [
    {'name' : 'image', 'type': np.ndarray},
    {'name' : 'number',  'type': int},
    {'name' : 'contours', 'type': list[np.ndarray]},
    ]:
    """
    Find and count contours form a grayscale image, and draw these contours.
    :param image: the grayscale image to process.
    :return: an image with the contours drawn on the input original image,
    the number of detected contours and tne contours themselves.
    """
    if len(image.shape) > 2 :
        raise ValueError("image must be in grayscale !")

    contours, hierarchy = cv2.findContours(image.copy(),
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print(f"Number of contours : {len(contours)}!")
    im_ret = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(im_ret, contours, -1, (0, 255, 0), 3)

    return {
        'image': im_ret,
        'number': len(contours),
        'contours': contours
    }

### alias the function defining the node as main_callable
main_callable = find_contours