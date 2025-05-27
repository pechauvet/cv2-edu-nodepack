import numpy as np
import cv2

def draw_rect(img : np.ndarray, contour : np.ndarray, color : tuple):
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

def draw_circle(img : np.ndarray, contour : np.ndarray, color : tuple):
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(img, center, radius, color, 2)

def draw_convex_hull(img : np.ndarray, contour : np.ndarray, color : tuple):
    hull = cv2.convexHull(contour)
    cv2.drawContours(img, [hull], 0, color, 2)

DRAW_MAP = {
    'rectangle'   : draw_rect,
    'circle'      : draw_circle,
    'convex hull' : draw_convex_hull
}

def highlight_objects(
        image_original: np.ndarray,
        contours: list[np.ndarray],
        min_area: 'natural_number' = 10,
        draw_name: {
            'widget_name': 'option_menu',
            'widget_kwargs': {
                'options': tuple(DRAW_MAP),
            },
            'type': str,
        } = 'rectangle',
        color: {
            'widget_name': 'color_button',
            'type': tuple,
        } = (255, 0, 0),

) -> [
    {'name' : 'image', 'type': np.ndarray},
    {'name' : 'number',  'type': int},
    ]:
    """
    Draw a shape around previously detected contours, if their surface is greater than a given threshold.
    :param image_original: the original image.
    :param contours: the detected contours.
    :param min_area: the minimal area (threshold to count a contour).
    :param draw_name: the type of shape (rectangle, circle or convex hull).
    :param color: the color of the shape to draw.
    :return: the image with shapes around objects, and the number of objects.
    """
    im_ret = image_original.copy()
    draw = DRAW_MAP[draw_name]
    col=color[::-1]
    nb=0
    for contour in contours :
        if cv2.contourArea(contour) > min_area :
            draw(im_ret, contour, col)
            nb+=1

    return {
        'image': im_ret,
        'number': nb
    }

### alias the function defining the node as main_callable
main_callable = highlight_objects