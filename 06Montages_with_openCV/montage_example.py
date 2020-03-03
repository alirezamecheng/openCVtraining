# tutotila from: https://www.pyimagesearch.com/2017/05/29/montages-with-opencv/
# USAGE
# python montage_example.py --images nordstrom_sample
# python montage_example.py --images nordstrom_sample --sample 33

# import the necessary packages
from imutils import build_montages
from imutils import paths
import argparse
import random
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-s", "--sample", type=int, default=21,
	help="# of images to sample")
args = vars(ap.parse_args())

# grab the paths to the images, then randomly select a sample of
# them
imagePaths = list(paths.list_images(args["images"])) # To obtain a listing of all image paths inside the --images  directory, we make a call to the list_images  function
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]

# initialize the list of images
images = []

# loop over the list of image paths
for imagePath in imagePaths:
	# load the image and update the list of images
	image = cv2.imread(imagePath)
	images.append(image)

# construct the montages for the images
montages = build_montages(images, (128, 196), (7, 3)) # Note: Empty space in the montage will be filled with black pixels.

# loop over the montages and display each of them
for montage in montages:
	cv2.imshow("Montage", montage)
	cv2.waitKey(0)