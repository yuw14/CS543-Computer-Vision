from functions import *

dest_dir = 'results/'
source_dir = 'prokudin-gorskii/'
suffix = '.jpg'

#the search radious
radius = 7

#code for question 3.b
# simple align

#simple pictures
img_names = ['00125v.jpg', '00149v.jpg', '00153v.jpg', '00351v.jpg', '00398v.jpg', '01112v.jpg']

for img_name in img_names:

	# Load the Image 
	orig_img = sk.img_as_float(skio.imread(source_dir + img_name))

	# Split Image by Colors
	blueImage, greenImage, redImage = map(crop, split(orig_img))

	# Align Colors

	# ssd
	# print("method: ssd")

	# Baseline: B
	print("Baseline: B")	
	greenDisplacement = simple_align_ssd(blueImage, greenImage, radius)
	alignedGreenImg = align(greenImage, greenDisplacement)
	redDisplacement = simple_align_ssd(blueImage, redImage, radius)
	alignedRedImg = align(redImage, redDisplacement)
	print("Offset {0} (Green: {1}, Red: {2})".format((img_name[:-4]).capitalize(), greenDisplacement, redDisplacement))
	resultIMG = overlap_images(alignedRedImg, alignedGreenImg, blueImage)


	# Baseline:G
	# print("Baseline: G") 
	# blueDisplacement = simple_align_ssd(blueImage,greenImage,radius)
	# alignedBlueImg = align(blueImage, blueDisplacement)
	# redDisplacement = simple_align_ssd(greenImage, redImage, radius)
	# alignedRedImg = align(redImage, redDisplacement)
	# print("Offset {0} (Blue: {1}, Red: {2})".format((img_name[:-4]).capitalize(), blueDisplacement, redDisplacement))
	# resultIMG = overlap_images(alignedRedImg,greenImage,alignedBlueImg)

	# Baseline: R
	# print("Baseline: R")	
	# blueDisplacement = simple_align_ssd(blueImage,redImage,radius)
	# alignedBlueImg = align(blueImage, blueDisplacement)
	# greenDisplacement = simple_align_ssd(greenImage, redImage, radius)
	# alignedGreenImg = align(greenImage, greenDisplacement)
	# print("Offset {0} (Blue: {1}, Green: {2})".format((img_name[:-4]).capitalize(), blueDisplacement, greenDisplacement))
	# resultIMG = overlap_images(redImage,alignedGreenImg,alignedBlueImg)

	# ncc
	# print("method: ncc")

	# Baseline: B
	# print("Baseline: B")	
	# greenDisplacement = simple_align_ncc(blueImage, greenImage, radius)
	# alignedGreenImg = align(greenImage, greenDisplacement)
	# redDisplacement = simple_align_ncc(blueImage, redImage, radius)
	# alignedRedImg = align(redImage, redDisplacement)
	# print("Offset {0} (Green: {1}, Red: {2})".format((img_name[:-4]).capitalize(), greenDisplacement, redDisplacement))
	# resultIMG = overlap_images(alignedRedImg, alignedGreenImg, blueImage)

	# # Baseline:G
	# print("Baseline: G") 
	# blueDisplacement = simple_align_ncc(blueImage,greenImage,radius)
	# alignedBlueImg = align(blueImage, blueDisplacement)
	# redDisplacement = simple_align_ncc(greenImage, redImage, radius)
	# alignedRedImg = align(redImage, redDisplacement)
	# print("Offset {0} (Blue: {1}, Red: {2})".format((img_name[:-4]).capitalize(), blueDisplacement, redDisplacement))
	# resultIMG = overlap_images(alignedRedImg,greenImage,alignedBlueImg)

	# # Baseline: R
	# print("Baseline: R")	
	# blueDisplacement = simple_align_ncc(blueImage,redImage,radius)
	# alignedBlueImg = align(blueImage, blueDisplacement)
	# greenDisplacement = simple_align_ncc(greenImage, redImage, radius)
	# alignedGreenImg = align(greenImage, greenDisplacement)
	# print("Offset {0} (Blue: {1}, Green: {2})".format((img_name[:-4]).capitalize(), blueDisplacement, greenDisplacement))
	# resultIMG = overlap_images(redImage,alignedGreenImg,alignedBlueImg)	

	write(dest_dir, img_name, resultIMG, suffix)