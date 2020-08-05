from functions import *

dest_dir = 'results/'
source_dir = 'prokudin-gorskii/'
suffix = '.jpg'

#the search radious
radius = 7

#simple pictures
img_names = ['00125v.jpg']

for img_name in img_names:

	# Load the Image 
	orig_img = sk.img_as_float(skio.imread(source_dir + img_name))

	# Split Image by Colors
	blueImage, greenImage, redImage = map(crop, split(orig_img))

	# Baseline:G SSD
	#align
	blueDisplacement = simple_align_ssd(blueImage,greenImage,radius)
	alignedBlueImg = align(blueImage, blueDisplacement)
	redDisplacement = simple_align_ssd(greenImage, redImage, radius)
	alignedRedImg = align(redImage, redDisplacement)
	print("Offset {0} (Blue: {1}, Red: {2})".format((img_name[:-4]).capitalize(), blueDisplacement, redDisplacement))

	#crop
	alignedRedImg = crop(alignedRedImg)
	alignedBlueImg = crop(alignedBlueImg)
	greenImage = crop(greenImage)
	
	resultIMG = overlap_images(alignedRedImg,greenImage,alignedBlueImg)
	write(dest_dir, img_name, resultIMG, suffix)
