from functions import *

dest_dir = 'results/'
source_dir = 'prokudin-gorskii/'
suffix = '.jpg'

#the search radious
radius = 7

#code for 3.c 
#fast align

#high resolution pictures
img_names = ['seoul_tableau.jpg', 'vancouver_tableau.jpg']

for img_name in img_names:

	# Load the high resolution Image 
	orig_img = sk.img_as_float(skio.imread(img_name))

	# Split Image by Colors
	blueImage, greenImage, redImage = map(crop, split(orig_img))

	# Align Colors
	# Pyramid Alignment

	# the effect of using ncc or ssd are proved the same based on the result getting from the simple pirctures
	# So here we only use ncc to get the result, but with diffenrent base line

	# print("Baseline: B")	
	print("displacment of Green")
	greenDisplacement = fast_align_ncc(blueImage, greenImage, radius)
	alignedGreenImg = align(greenImage, greenDisplacement)
	print("displacment of Red")
	redDisplacement = fast_align_ncc(blueImage, redImage, radius)
	alignedRedImg = align(redImage, redDisplacement)
	print("Offset {0} (Green: {1}, Red: {2})".format((img_name[:-4]).capitalize(), greenDisplacement, redDisplacement))
	resultIMG = overlap_images(alignedRedImg, alignedGreenImg, blueImage)

	# Baseline:G
	# print("Baseline: G") 
	# blueDisplacement = fast_align_ncc(blueImage,greenImage,radius)
	# alignedBlueImg = align(blueImage, blueDisplacement)
	# redDisplacement = fast_align_ncc(greenImage, redImage, radius)
	# alignedRedImg = align(redImage, redDisplacement)
	# print("Offset {0} (Blue: {1}, Red: {2})".format((img_name[:-4]).capitalize(), blueDisplacement, redDisplacement))
	# resultIMG = overlap_images(alignedRedImg,greenImage,alignedBlueImg)

	# Baseline: R
	# print("Baseline: R")	
	# blueDisplacement = fast_align_ncc(blueImage,redImage,radius)
	# alignedBlueImg = align(blueImage, blueDisplacement)
	# greenDisplacement = fast_align_ncc(greenImage, redImage, radius)
	# alignedGreenImg = align(greenImage, greenDisplacement)
	# print("Offset {0} (Blue: {1}, Green: {2})".format((img_name[:-4]).capitalize(), blueDisplacement, greenDisplacement))
	# resultIMG = overlap_images(redImage,alignedGreenImg,alignedBlueImg)	


	write(dest_dir, img_name, resultIMG, suffix)
