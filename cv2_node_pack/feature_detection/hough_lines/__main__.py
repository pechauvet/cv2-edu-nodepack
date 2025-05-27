import numpy as np
import cv2

def hough_lines(
        image: np.ndarray,
        threshold: 'natural_number'=100,
        minLineLength: float=5.0,
        maxLineGap: float=10.0,
) -> [
    {'name' : 'image', 'type': np.ndarray},
    {'name' : 'number',  'type': int},
    {'name' : 'lines', 'type': list},
    ]:
    """
    Finds line segments in a binary image using the probabilistic Hough transform.
    :param image: The grayscale input image.
    :param threshold: Min number of votes for valid line
    :param minLineLength: Minimum line length. Line segments shorter than that are rejected.
    :param maxLineGap: Maximum allowed gap between points on the same line to link them.
    :return: An image with the lines drawn on the input image, the number of detected lines
    and the list of lines [(x1, y1), (x2, y2)].
    """
    lines = cv2.HoughLinesP(
        image,  # Input gray image with edges
        1,  # Distance resolution in pixels
        np.pi / 180,  # Angle resolution in radians
        threshold=threshold,
        minLineLength=minLineLength,
        maxLineGap=maxLineGap
    )

    detected_lines = []
    im_ret = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if lines is not None:
        # Iterate over points
        for points in lines:
            # Extracted points nested in the list
            x1, y1, x2, y2 = points[0]
            # Draw the lines
            cv2.line(im_ret, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Maintain a simples lookup list for points
            detected_lines.append([(x1, y1), (x2, y2)])

    return {
        'image': im_ret,
        'number': len(detected_lines),
        'lines': detected_lines
    }

### alias the function defining the node as main_callable
main_callable = hough_lines
