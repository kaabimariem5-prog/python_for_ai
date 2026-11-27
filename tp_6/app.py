import cv2

detecteur = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
image = cv2.imread("test_visages.png")

if image is None:
    print("Image introuvable")
elif detecteur.empty():
    print("Fichier XML du détecteur introuvable")
else:
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    visages = detecteur.detectMultiScale(
        gris, scaleFactor=1.1, minNeighbors=5
    )

    for (x, y, w, h) in visages:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    print("Nombre de visages :", len(visages))
    cv2.imshow("Detection de visages", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()