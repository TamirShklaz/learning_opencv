import cv2
import numpy as np
import matplotlib.pyplot as plt

#Grayscale is much easier to work with
img = cv2.imread("assets/beer.png", cv2.IMREAD_GRAYSCALE)
