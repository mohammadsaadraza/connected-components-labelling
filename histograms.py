
import cv2 
from matplotlib import pyplot as plt 
import os

source = './imgs'
dest = './histograms'

for file in os.listdir(source):
	path = os.path.join(source, file)
	img = cv2.imread(path,0) 

	# find frequency of pixels in range 0-255 
	hist = cv2.calcHist([img],[0],None,[256],[0,256]) 

	# saving the plotting graph of an image
	filename, ext = os.path.splitext(file)
	destPath = os.path.join(dest, filename + '.png')

	plt.figure()
	plt.title("Histogram of {}".format(file))
	plt.plot(hist)
	plt.savefig(destPath)

print('---DONE---') 
