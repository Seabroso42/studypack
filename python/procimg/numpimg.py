import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

abyssalVoid = np.zeros((512,512,3),np.uint8)
plt.imshow(abyssalVoid)
print(abyssalVoid.shape)
abyssalVoid[:200, :200] = [255,0,160]
img3 = cv.cvtColor(abyssalVoid, cv.COLOR_BGR2RGB)
plt.imshow(img3)