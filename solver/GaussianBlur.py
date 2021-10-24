# https://en.wikipedia.org/wiki/Gaussian_blur
# https://www.tutorialkart.com/opencv/python/opencv-python-gaussian-image-smoothing/

from solver.base.AbstractChainHandler import AbstractChainHandler
from utilities.Image import Image
import cv2


class GaussianBlur(AbstractChainHandler):
    def handle(self, request):
        print('gaussian blur processing raw image')

        data_description = request[0]
        raw_image = request[1]
        if not data_description == 'GaussianBlur':
            return super().handle(request)

        img = cv2.GaussianBlur(raw_image, (3, 3), cv2.BORDER_DEFAULT)
        # Image.show(img)

        return img