import cv2


class Image:
    @staticmethod
    def show(image):
        cv2.imshow('displaymywindows', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
