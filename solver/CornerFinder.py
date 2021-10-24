from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler
import cv2


class CornerFinder(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        data = request[1]
        contours = data[0]
        image = data[1]

        if not data_description == 'CornerFinder':
            return super().handle(request)

        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.0015 * peri, True)
            if len(approx) == 4:
                return [approx, image]

        raise Exception('Sudoku board not found')

