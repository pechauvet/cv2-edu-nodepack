import pygame
import numpy as np

ORIGIN = pygame.math.Vector2()

def cvImageToSurface(cv_image):
    """
    Convert an opencv image (ndarrray) in a pygame image (Surface).
    :param cv_image: the opencv image.
    :return: a pygame Surface image.
    """
    if cv_image.dtype.name == 'uint16':
        cv_image = (cv_image / 256).astype('uint8')
    size = cv_image.shape[1::-1]
    if len(cv_image.shape) == 2:
        cv_image = np.repeat(cv_image.reshape(size[1], size[0], 1), 3, axis = 2)
        img_format = 'RGB'
    else:
        img_format = 'RGBA' if cv_image.shape[2] == 4 else 'RGB'
        cv_image[:, :, [0, 2]] = cv_image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv_image.flatten(), size, img_format)
    return surface.convert_alpha() if img_format == 'RGBA' else surface.convert()

def view_image(
    image: np.ndarray,
    max_preview_size: 'natural_number' = 600
) -> [
    {'name': 'full_surface', 'type': pygame.Surface, 'viz': 'loop'},
    {'name': 'preview_surface', 'type': pygame.Surface, 'viz': 'side'},
]:
    """
    Create a view on the input image.
    :param image: the image to view in the nodezator window.
    :param max_preview_size: the maximum preview diagonal size.
    :return: Two pygame images of type Surface : one for the image,
    the other for a reduced size preview.
    """
    if max_preview_size < 0:
        raise ValueError("'max_preview_size' must be >= 0")

    full_surface =  cvImageToSurface(image)

    if not max_preview_size:
        preview_surface = full_surface

        return {
            'full_surface': full_surface,
            'preview_surface': preview_surface,
        }

    bottomright = full_surface.get_size()
    diagonal_length = ORIGIN.distance_to(bottomright)
    if diagonal_length > max_preview_size:
        size_proportion = max_preview_size / diagonal_length
        new_size = ORIGIN.lerp(bottomright, size_proportion)
        preview_surface = pygame.transform.smoothscale(full_surface, new_size)
    else:
        preview_surface = full_surface

    return {
        'full_surface': full_surface,
        'preview_surface': preview_surface,
    }

### alias the function defining the node as main_callable
main_callable = view_image