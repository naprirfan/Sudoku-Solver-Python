from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler


class SudokuSolver(AbstractChainHandler, ABC):
    def handle(self, request):
        data_description = request[0]
        if not data_description == 'SudokuSolver':
            return super().handle(request)

        print('SudokuSolver')
        return 'SudokuSolver'
