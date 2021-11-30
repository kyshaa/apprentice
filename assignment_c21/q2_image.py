import cv2 as cv 

img = cv.imread(r'\Users\User\Desktop\Things\Perantis\assignment\assignment_c21/astronaut.jpg')
cv.imshow("Display Picture", img)

cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()