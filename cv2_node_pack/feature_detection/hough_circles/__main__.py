import numpy as np
import cv2

def hough_circles(
        image: np.ndarray,
        resolution:float=1.0,
        minDistCenters: 'natural_number'=20,
        param1: 'natural_number'=50,
        param2: 'natural_number'=30,
        minRadius: 'natural_number'=1,
        maxRadius: 'natural_number'=40
) -> [
    {'name' : 'image', 'type': np.ndarray},
    {'name' : 'number',  'type': int},
    {'name' : 'circles', 'type': list},
    ]:
    """
    Finds circles in a grayscale image using the Hough transform.
    :param image: the grayscale input image.
    :param resolution: Inverse ratio of the accumulator resolution to the image resolution. For example, if resolution=1 , the accumulator has the same resolution as the input image. If resolution=2 , the accumulator has half as big width and height.
    :param minDistCenters: Minimum distance between the centers of the detected circles.
    :param param1: The higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller).
    :param param2: The accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.
    :param minRadius: Minimum circle radius.
    :param maxRadius: Maximum circle radius.
    :return: An image with the circles drawn on the input image, the number of detected circles
    and the list of circles [(x,y), r].
    """
    circles = cv2.HoughCircles(image,
                                        cv2.HOUGH_GRADIENT, dp=resolution, minDist=minDistCenters, param1=param1,
                                        param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    im_ret = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    # Draw circles that are detected
    detected_circles = []
    if circles is not None:
        # Convert the circle parameters to integers
        circles = np.uint16(np.around(circles))
        # Draw circles
        for pt in circles[0, :]:
            x, y, r = pt[0], pt[1], pt[2]
            # Draw the circumference of the circle
            cv2.circle(im_ret, (x, y), r, (0, 255, 0), 2)
            # Draw the center
            cv2.circle(im_ret, (x, y), 1, (0, 0, 255), 3)
            # Append circle to detected ones
            detected_circles.append([(x,y),r])

    return {
        'image': im_ret,
        'number': len(detected_circles),
        'circles': detected_circles
    }

### alias the function defining the node as main_callable
main_callable = hough_circles