import cv2

image = cv2.imread("test_visages.png")

if image is None:
    print("erreur : test_visages.png introuvable")
else:
    cv2.imshow("Mon image",image)
    cv2.waitkey(0)
    cv2.destroyAllwindows()