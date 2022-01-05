import cv2

# import the image
image = cv2.imread('back-to-the-future.jpg')

# converting the original image to grayscale and invert it
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image

# Gaussian effect to the inverted image, inverted it and sketch it
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256)

# Sketch the image
cv2.imshow("Original image", image)
cv2.imshow("Pencil sketch image", pencil_sketch)
cv2.waitKey(0)
