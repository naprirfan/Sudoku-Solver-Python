from solver.base.AbstractChainHandler import AbstractChainHandler


class GaussianBlur(AbstractChainHandler):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'GaussianBlur':
            return super().handle(request)

        print('gaussian blur processing raw image')
        return 'gaussian blur processing raw image'
