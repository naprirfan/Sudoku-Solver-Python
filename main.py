from solver.GaussianBlur import GaussianBlur
from solver.Thresholding import Thresholding
from solver.ImageDilation import ImageDilation
from solver.ContourFinder import ContourFinder
from solver.CornerFinder import CornerFinder
from solver.base.AbstractChainHandler import AbstractChainHandler

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def client_code(handler: AbstractChainHandler):
    result = handler.handle("hey!")
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gaussianBlur = GaussianBlur()
    thresholding = Thresholding()
    imageDilation = ImageDilation()
    contourFinder = ContourFinder()
    cornerFinder = CornerFinder()

    gaussianBlur.set_next(thresholding).set_next(imageDilation).set_next(contourFinder).set_next(cornerFinder)

    client_code(gaussianBlur)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
