# https://en.wikipedia.org/wiki/Thresholding_(image_processing)
# https://learnopencv.com/opencv-threshold-python-cpp/

from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler
from utilities.Image import Image
import cv2


class Thresholding(AbstractChainHandler, ABC):
    def handle(self, request):
        print('now thresholding')

        data_description = request[0]
        image = request[1]
        if not data_description == 'Thresholding':
            return super().handle(request)

        th, img = cv2.threshold(image, 127, 200, cv2.THRESH_BINARY_INV)
        Image.show(img)

        return img
