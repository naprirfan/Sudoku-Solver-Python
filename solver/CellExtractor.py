from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler


class CellExtractor(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'CellExtractor':
            return super().handle(request)

        print('CellExtractor')
        return 'CellExtractor'
