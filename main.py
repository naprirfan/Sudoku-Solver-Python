from solver.GaussianBlur import GaussianBlur
from solver.Thresholding import Thresholding
from solver.ImageDilation import ImageDilation
from solver.ContourFinder import ContourFinder
from solver.CornerFinder import CornerFinder
from solver.ImageCropper import ImageCropper
from solver.CellExtractor import CellExtractor
from solver.DigitInterpreter import DigitInterpreter
from solver.SudokuSolver import SudokuSolver
from solver.base.AbstractChainHandler import AbstractChainHandler


class ClientExecutor:
    def __init__(self, raw_image_path: str):
        self.gaussianBlur = GaussianBlur()
        self.thresholding = Thresholding()
        self.imageDilation = ImageDilation()
        self.contourFinder = ContourFinder()
        self.cornerFinder = CornerFinder()
        self.imageCropper = ImageCropper()
        self.cellExtractor = CellExtractor()
        self.digitInterpreter = DigitInterpreter()
        self.sudokuSolver = SudokuSolver()

        print(raw_image_path)
        self.gaussianBlur.set_next(self.thresholding).set_next(self.imageDilation).set_next(self.contourFinder).set_next(
            self.cornerFinder).set_next(self.imageCropper).set_next(self.cellExtractor).set_next(
            self.digitInterpreter).set_next(self.sudokuSolver)

    def execute_handler(self, handler: AbstractChainHandler, parameter):
        return handler.handle(parameter)

    def solve_sudoku_puzzle(self):
        blurredImage = self.execute_handler(self.gaussianBlur, ['GaussianBlur', 0])
        imageWithThreshold = self.execute_handler(self.thresholding, ['Thresholding', blurredImage])
        dilatedImage = self.execute_handler(self.imageDilation, ['ImageDilation', imageWithThreshold])
        contouredImage = self.execute_handler(self.contourFinder, ['ContourFinder', dilatedImage])
        corneredImage = self.execute_handler(self.cornerFinder, ['CornerFinder', contouredImage])
        croppedImage = self.execute_handler(self.imageCropper, ['ImageCropper', corneredImage])
        extractedCell = self.execute_handler(self.cellExtractor, ['CellExtractor', croppedImage])
        recognizedDigits = self.execute_handler(self.digitInterpreter, ['CellExtractor', extractedCell])
        solvedSudoku = self.execute_handler(self.sudokuSolver, ['SudokuSolver', recognizedDigits])

        return solvedSudoku


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = ClientExecutor('some_image_path')
    client.solve_sudoku_puzzle()
