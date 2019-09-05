import numpy as np
import cv2 as cv

def create_pic():
  img = np.ones([100,100,3],np.uint8)
  # img.fill(12222.388)
  # print(img)
  img = img * 200
  print(img)
  cv.imshow('img',img)
  cv.waitKey(0)

create_pic()