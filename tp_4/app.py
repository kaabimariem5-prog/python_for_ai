import cv2
image = cv2.imread("test_visages.png")
if image is not None:
 floue = cv2.GaussianBlur(image, (7, 7), 0)
 cv2.imshow("Originale", image)
 cv2.imshow("Image floue", floue)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
