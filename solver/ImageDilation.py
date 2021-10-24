from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler


class ImageDilation(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'ImageDilation':
            return super().handle(request)

        print('imageDilation')
        return 'imageDilation'
