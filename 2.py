import cv2
import numpy as np 
src = cv2.imread("airplane.png")
dst = cv2.imread("sky.jpg")
src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
width, height, channels = dst.shape
center = (int(width/2),int(height/2))
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
cv2.imwrite("result.jpg", output)