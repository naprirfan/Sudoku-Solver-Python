from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler
from utilities.Image import Image
import cv2
import numpy as np


class ImageCropper(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        data = request[1]
        corners = data[0]
        image = data[1]

        # Image.show(image)

        if not data_description == 'ImageCropper':
            return super().handle(request)

        ordered_corners = self.order_corner_points(corners)
        width, height, dimensions = self.get_dimension(ordered_corners)
        print(width)
        print(height)
        print(dimensions)
        ordered_corners = np.array(ordered_corners, dtype="float32")
        grid = cv2.getPerspectiveTransform(ordered_corners, dimensions)
        result = cv2.warpPerspective(image, grid, (width, height))
        Image.show(result)

        return result

    def order_corner_points(self, corners):
        # Corners[0],... stores in format [[x y]]
        # Separate corners into individual points
        # Index 0 - top-right
        #       1 - top-left
        #       2 - bottom-left
        #       3 - bottom-right
        corners = [(corner[0][0], corner[0][1]) for corner in corners]
        top_r, top_l, bottom_l, bottom_r = corners[0], corners[1], corners[2], corners[3]
        return top_l, top_r, bottom_r, bottom_l

    def get_dimension(self, ordered_corners):
        top_l, top_r, bottom_r, bottom_l = ordered_corners

        # Determine width of new image which is the max distance between
        # (bottom right and bottom left) or (top right and top left) x-coordinates
        width_A = np.sqrt(((bottom_r[0] - bottom_l[0]) ** 2) + ((bottom_r[1] - bottom_l[1]) ** 2))
        width_B = np.sqrt(((top_r[0] - top_l[0]) ** 2) + ((top_r[1] - top_l[1]) ** 2))
        width = max(int(width_A), int(width_B))

        # Determine height of new image which is the max distance between
        # (top right and bottom right) or (top left and bottom left) y-coordinates
        height_A = np.sqrt(((top_r[0] - bottom_r[0]) ** 2) + ((top_r[1] - bottom_r[1]) ** 2))
        height_B = np.sqrt(((top_l[0] - bottom_l[0]) ** 2) + ((top_l[1] - bottom_l[1]) ** 2))
        height = max(int(height_A), int(height_B))

        # Construct new points to obtain top-down view of image in
        # top_r, top_l, bottom_l, bottom_r order
        dimension = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1],
                               [0, height - 1]], dtype="float32")

        return width, height, dimension
