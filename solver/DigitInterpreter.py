from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler


class DigitInterpreter(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'DigitInterpreter':
            return super().handle(request)

        print('DigitInterpreter')
        return 'DigitInterpreter'
