# cv2-edu-nodepack
An educational OpenCV node pack for Nodezator (https://nodezator.com/)

### Objective
This node pack was created to serve as a basic tool for discovering image processing. It is intended for introductory activities and workshops for high school and undergraduate students (not necessarily in science and technology). 
The number of nodes is deliberately limited, focusing on a few fundamental elements of image processing: grayscale conversion, filters, morphological transformations, edge detection. They are enough to practice some activities like counting elements such as cells, debris, fibers in a not too complex photo.

### Why Nodezator ?
Nodezator was chosen as the development base due to the simplicity of the interface for students (a simplified menu, a single editing window) and the ease of implementing nodes for the developer. Finally, the ability to generate Python code in the form of a program allows more advanced programming students to rework it outside of the workshop.

### Installation
To use this node pack, it is mandatory to install:
- nodezator : a multipurpose visual node editor for Python conceived by Kennedy Richard Silva Guerra (see https://nodezator.com/).
- numpy : the package for scientific computing (images and frames in opencv-python are numpy arrays).
- opencv-python : allows to use OpenCV from python.

This node pack must be used through the nodezator application.

### Node pack structure
The node pack is structured in four groups of nodes :
- inout_nodes : nodes to open and save images
- view_nodes : nodes to show images and values
- process_image : color conversion, filters, thresholding, erosion and dilation, ...
- feature_detection : trace edges, find and count contours, highlight objects...

> #### Structure details :
> - inout_nodes :
>    - open_image
>    - save_image 
> - view_nodes : 
>    - view_image
>    - view_value 
> - process_image : 
>    - color_conversion
>    - filter_bilateral
>    - filter_blur
>    - filter_gaussian_blur
>    - filter_median
>    - filter_sharpen
>    - morpho_transform
>    - threshold_adaptive
>    - threshold_otsu
>    - threshold_simple
> - feature_detection :
>    - canny_edges
>    - find_contours
>    - find_contours2
>    - highlight_objects
>    - hough_circles
>    - hough_lines

You can download the following pdf documents for a complete description of the nodes:
- [Nodes Description-Eng.pdf](https://github.com/user-attachments/files/20452240/Nodes.Description-Eng.pdf) (english)
- [Description Noeuds-Fr.pdf](https://github.com/user-attachments/files/20452272/Description.Noeuds-Fr.pdf) (french) 

### Examples

#### Open, convert colors and display
A graph that allows you to open an image, simultaneously convert it to grayscale and invert the RGB channels, and display the result of each conversion.
![cv2_color_conversion](https://github.com/user-attachments/assets/9b037a2d-0da0-4896-885e-ce4110630827)

#### Dilate and erode
A graph that allows you to test the morpho_transform node, a first one in dilate mode and the second one in erode mode, and which displays the result for each of the two nodes. 
![cv2_dilate_erode](https://github.com/user-attachments/assets/90c235fa-74cb-431e-bdb2-1231984efa89)

#### Find and count contours
A more complex example... This graph allows you to find contours of blood celles and to count them. It illustrates the use of these nodes :
- color_conversion : the input image is converted to grayscale;
- filter_gaussian_blur : a gaussian blur filter is applied to the grayscale image;
- canny_edges : preserves the edges of objects and erases the rest;
- morpho_transform : in mode erode, to close all the contours;
- find_contours2 : detect the contours, put them in a list, and trace the contours in green on the original (RGB) image.
Finally the image with contours traces is diplayed, as well as the number of contours (the number of detected cells).
![cv2_count_objects](https://github.com/user-attachments/assets/cefb00cd-0eee-4c8b-84b6-faa4bb355338)

