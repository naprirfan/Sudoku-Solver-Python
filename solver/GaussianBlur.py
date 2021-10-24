from solver.base.AbstractChainHandler import AbstractChainHandler
from typing import Any


class GaussianBlur(AbstractChainHandler):
    def handle(self, request: Any):
        if not isinstance(request, str):
            return super().handle(request)

        return 'gaussian blur processing'
