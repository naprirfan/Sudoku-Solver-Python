from abc import ABC
from solver.base.AbstractChainHandler import AbstractChainHandler
from typing import Any


class Thresholding(AbstractChainHandler, ABC):
    def handle(self, request: Any):
        if not isinstance(request, str):
            return super().handle(request)

        return 'now thresholding'
