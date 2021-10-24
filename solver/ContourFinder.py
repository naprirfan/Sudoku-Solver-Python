from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler


class ContourFinder(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'ContourFinder':
            return super().handle(request)

        print('ContourFinder')
        return 'ContourFinder'
