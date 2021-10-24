from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler


class Thresholding(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'Thresholding':
            return super().handle(request)

        print('now thresholding')
        return 'now thresholding'
