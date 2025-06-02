import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt

def readImage(path):
  root = os.getcwd()
  imgPath= os.path.join(root, path)
  img = cv.imread(imgPath)
  cv.imshow('img', img)
  print(img.shape)
  cv.waitKey(0)

def readVideo(path):
  root = os.getcwd()
  vidPath = os.path.join(root, path)

def videoWebcam():
  cap = cv.VideoCapture(0)

  if not cap.isOpened():
    exit()

  while True:
    ret, frame = cap.read()
    if ret:
      cv.imshow('Webcam', frame)

    if cv.waitKey(1) == ord('q'):
      break

def videoFromFile(path):
  root = os.getcwd()
  vidPath = os.path.join(root, f'sample\\{path}')
  cap = cv.VideoCapture(vidPath)

  while cap.isOpened():
    ret, frame = cap.read()
    cv.imshow('video', frame)
    delay = int(1000/60)

    if cv.waitKey(delay) == ord('q'):
      break



def writeImage(image, name):
  root = os.getcwd()
  img = image
  outPath= os.path.join(root, f'python/procimg/saved/{name}')
  cv.imwrite(outPath, img)

if __name__ == '__main__':
  root = os.getcwd()
  print(cv.__version__)
  #readImage(os.path.join(root, 'python/procimg/sample/snake_lamp.png'))
  test = cv.imread(os.path.join(root, 'python/procimg/sample/LogoLaser.png'))
  #writeImage(test, "output.jpg")
  videoPath = ""

  videoFromFile(videoPath)