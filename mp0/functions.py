import numpy as np
import skimage as sk
import skimage.io as skio
from skimage.transform import resize
from PIL import Image

# preprocess the image: split
# splits the image into the blue, green, red image
def split(img):
	height = int(np.floor(img.shape[0] / 3.0))
	b = img[:height]
	g = img[height: 2*height]
	r = img[2*height: 3*height]
	return b, g, r

# preprocess the image: crop
# Crop 10% off the borders of the image
# We could also use this function to do the optimization for extra credit
def crop(img):
	height, width = img.shape
	newHeight, newWidth = int(height/1.11), int(width/1.11)
	return img[height-newHeight:newHeight, width-newWidth:newWidth]

# Normalized Cross-Correlation: (a./||a|| dot b./||b||)
def ncc(a, b):
	return ((a/np.linalg.norm(a)) * (b/np.linalg.norm(b))).ravel().sum()

# Sum of Square Differences: sum(sum((a-b).^2))
def ssd(a, b):
	return (((a-b)**2).sum()).sum()

# Searches over a radius in given images 
# and returns best displacement based on ssd
def find_dis_ssd(img1, img2, bound, radius):
	least_difference = 100000
	for column in range(-radius + bound[0], radius + bound[0] ):
		for row in range(-radius + bound[1], radius + bound[1]):
			curr = ssd(img1, np.roll(np.roll(img2, column, axis = 0), row, axis = 1))
			if (curr < least_difference): 
				least_difference= curr
				displacement = [column, row]
	return displacement

# Searches over a radius in given images 
# and returns best displacement based on ncc
def find_dis_ncc(img1, img2, bound, radius):
	best = -1
	for column in range(-radius + bound[0], radius + bound[0] ):
		for row in range(-radius + bound[1], radius + bound[1]):
			curr = ncc(img1, np.roll(np.roll(img2, column, axis = 0), row, axis = 1))
			if (curr > best): 
				best = curr
				dis = [column, row]
	return dis

# simple finding displacement when using ssd
def simple_align_ssd(img1, img2, radius):
	bound = [0, 0]		
	displacement = find_dis_ssd(img1, img2, bound, radius)
	return displacement

# simple finding displacement when using ncc
def simple_align_ncc(img1, img2, radius):
	bound = [0, 0]	
	dis = find_dis_ncc(img1, img2, bound, radius)
	return dis

# Aligns images themselves with displacement vectors 
def align(img, displacement):
	result = np.roll(np.roll(img, displacement[0], axis = 0), displacement[1], axis = 1)
	return result

# two-level image pyramid
# Recursively 
# ssd
def fast_align_ssd(img1, img2, radius):
	rows, columns = img1.shape
	if max(rows, columns) > 200:			
		halved_img1 = imresize(img1, 0.5)
		halved_img2 = imresize(img2, 0.5)
		offset = fast_align_ssd(halved_img1, halved_img2, radius)
		scaled_offset = [i*2 for i in offset] 
		displacement = find_dis_ssd(img1, img2, scaled_offset, radius)
	else:
		displacement = simple_align_ssd(img1, img2, 15)
	return displacement

# ncc
def fast_align_ncc(img1, img2, radius):
	rows, columns = img1.shape
	if max(rows, columns) > 200:
		h1, w1 = img1.shape
		halved_img1 = resize(img1, (int(0.5*h1), int(0.5*w1)))
		h2, w2 = img2.shape
		halved_img2 = resize(img2, (int(0.5*h2), int(0.5*w2)))
		offset = fast_align_ncc(halved_img1, halved_img2, radius)
		print("coarse_offset {0}".format(offset))
		scaled_offset = [i*2 for i in offset] 
		displacement = find_dis_ncc(img1, img2, scaled_offset, radius)
	else:
		displacement = simple_align_ncc(img1, img2, 15)
	return displacement

def overlap_images(r, g, b):
	img = np.dstack([r, g, b])
	return img

# Saves image to the destination direction
def write(dest_dir, img_name, img, suffix):
	filename = dest_dir + img_name[:-4] + suffix
	skio.imsave(str(filename), img)
	print("Image {0} has been saved to {1}".format(img_name, filename))
