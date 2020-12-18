import cv2

im = cv2.imread("3D.jpg")
roi = cv2.selectROI(im)

print(roi)
print(roi[0])
print(roi[1])
print(roi[2])
print(roi[3])

im_cropped = im[int(roi[1]):int(roi[1]+roi[3]),
                int(roi[0]):int(roi[0]+roi[2])]
print(im_cropped)

edge = cv2.imshow("Cropped Image", im_cropped)
print(edge)
cv2.waitKey(0)
