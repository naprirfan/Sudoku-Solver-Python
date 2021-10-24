from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler
from utilities.Image import Image
import cv2


class ContourFinder(AbstractChainHandler, ABC):
    def handle(self, request):
        print('ContourFinder')

        data_description = request[0]
        image = request[1]

        if not data_description == 'ContourFinder':
            return super().handle(request)

        contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return [contours, image]
