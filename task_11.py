import cv2
import numpy as np

image_path = 'изображение.png'
image = cv2.imread(image_path)
output_image = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(largest_contour)
    if M["m00"] != 0:
        center_x = int(M["m10"] / M["m00"])
        center_y = int(M["m01"] / M["m00"])
        print(f"Центр самого большого объекта: ({center_x}, {center_y})")

        cv2.circle(output_image, (center_x, center_y), 5, (0, 0, 255), -1)

    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imwrite('output.png', output_image)
    cv2.imshow('Largest Object', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Объекты не найдены.")