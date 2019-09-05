#coding=utf-8
import cv2 as cv
import numpy as np
def add_demo(m1, m2):
  dit = cv.add(m1, m2)
  cv.imshow('3',dit)
  
def sub_demo(m1, m2):
  dd = cv.subtract(m1,m2)
  cv.imshow('4',dd)
def bit_not(m1):
  dd = cv.bitwise_not(m1)
  cv.imshow('5',dd)

if __name__ == "__main__":
  pic1 = cv.imread('./images/WindowsLogo.jpg')
  pic2 = cv.imread('./images/LinuxLogo.jpg')
  # cv.imshow('1', pic1)
  # cv.imshow('2',pic2)
  # print(pic1.shape)
  # print(pic2.shape)

  add_demo(pic1, pic2)
  sub_demo(pic2, pic1)
  bit_not(pic1)
  cv.waitKey(0)
