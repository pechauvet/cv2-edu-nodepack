import numpy as np
import cv2

COLOR_TRANSFORM_MAP = {
  'Gray'         : cv2.COLOR_BGR2GRAY,
  'BGR'          : cv2.COLOR_BGR2RGB,
}

def color_conversion(
        image: np.ndarray,
        transform_name: {
            'widget_name': 'option_menu',
            'widget_kwargs': {
                'options': tuple(COLOR_TRANSFORM_MAP),
            },
            'type': str,
        } = 'Gray',
) -> [
      {'name': 'image', 'type': np.ndarray},
    ]:
    """
    Convert an image in grayscale or in reversed channels (RGB to BGR).
    :param image: the image to transform.
    :param transform_name: grayscale or RGB to BGR transformation.
    :return: the transformed image.
    """
    transform=COLOR_TRANSFORM_MAP[transform_name]
    if len(image.shape)<3 :
        return image
    else :
        return cv2.cvtColor(image, transform)

### alias the function defining the node as main_callable
main_callable = color_conversion