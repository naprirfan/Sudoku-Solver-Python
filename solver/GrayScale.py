# https://techtutorialsx.com/2018/06/02/python-opencv-converting-an-image-to-gray-scale/

from solver.base.AbstractChainHandler import AbstractChainHandler
from utilities.Image import Image
import cv2


class GrayScale(AbstractChainHandler):
    def handle(self, request):
        print('Grayscale image')

        data_description = request[0]
        raw_image = request[1]
        if not data_description == 'GrayScale':
            return super().handle(request)

        result = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
        # Image.show(result)

        return result