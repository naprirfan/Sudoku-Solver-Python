from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler


class CornerFinder(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'CornerFinder':
            return super().handle(request)

        print('findCorner')
        return 'findCorner'
