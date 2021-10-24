from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler
from utilities.Image import Image
import cv2
import numpy


class ImageDilation(AbstractChainHandler, ABC):
    def handle(self, request):
        print('imageDilation')

        data_description = request[0]
        image = request[1]
        if not data_description == 'ImageDilation':
            return super().handle(request)

        kernel = numpy.ones((5, 5), numpy.uint8)
        result = cv2.dilate(image, kernel, iterations=1)
        Image.show(result)

        return result
