from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler


class ImageCropper(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'ImageCropper':
            return super().handle(request)

        print('ImageCropper')
        return 'ImageCropper'
