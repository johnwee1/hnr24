import cv2
import os

# The deskew method is NOT working.


class Deskew:
    @staticmethod
    def getSkewAngle(cvImage) -> float:
        # Prep image, copy, convert to gray scale, blur, and threshold
        newImage = cvImage.copy()
        gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (9, 9), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # Apply dilate to merge text into meaningful lines/paragraphs.
        # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
        # But use smaller kernel on Y axis to separate between different blocks of text
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 5))
        dilate = cv2.dilate(thresh, kernel, iterations=4)

        # Find all contours
        contours, hierarchy = cv2.findContours(
            dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        # Find largest contour and surround in min area box
        largestContour = contours[0]
        minAreaRect = cv2.minAreaRect(largestContour)

        # Determine the angle. Convert it to the value that was originally used to obtain skewed image
        angle = minAreaRect[-1]
        print(f"angle = {angle}")
        if angle < -45:
            angle = 90 + angle
        return -1.0 * angle

    @staticmethod
    def rotateImage(cvImage, angle: float):
        newImage = cvImage.copy()
        (h, w) = newImage.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        newImage = cv2.warpAffine(
            newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
        )
        return newImage

    @staticmethod
    def deskew(cvImage):
        angle = Deskew.getSkewAngle(cvImage)
        return Deskew.rotateImage(cvImage, -1.0 * angle)


# img_name = "images/grace.jpg"
# img_path = os.path.join(os.path.dirname(__file__), img_name)
# image = cv2.imread(img_path)
# rotated_img = Deskew.rotateImage(image, 25)


# unrotate_img = Deskew.deskew(rotated_img)
# cv2.imshow("r", unrotate_img)
# cv2.waitKey(0)
