import os
import cv2 
from matplotlib import pyplot as plt

source = './imgs'
dest = './masks'

for file in ['coins.jpg', 'bookpage.jpg']:
	path = os.path.join(source, file)
	img = cv2.imread(path) 
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#Histogram
	filename, ext = os.path.splitext(file)
	destPath = os.path.join(dest, filename + '.png')
	hist = cv2.calcHist([img],[0],None,[256],[0,256])
	plt.figure()
	plt.title("Histogram of {}".format(file))
	plt.plot(hist)
	plt.savefig(destPath)

	#Thresholding
	threshold_val = 120

	ret, thresh = cv2.threshold(img, threshold_val, 255, cv2.THRESH_BINARY)

	destPath = os.path.join(dest, "mask_{}".format(file))
	cv2.imwrite(destPath, thresh)

	log_OR = cv2.bitwise_or(img, thresh)
	destPath = os.path.join(dest, "logOR_{}".format(file))
	cv2.imwrite(destPath, log_OR)

print('---DONE---')
