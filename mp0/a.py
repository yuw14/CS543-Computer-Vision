from functions import *

dest_dir = 'results/wonky'
source_dir = 'prokudin-gorskii/'
suffix = '.jpg'

#the search radious
radius = 7


#code for question 3.a

orig_img = sk.img_as_float(skio.imread(source_dir + '00125v.jpg'))

blueImage, greenImage, redImage = map(crop, split(orig_img))

resultIMG = overlap_images(blueImage, greenImage, blueImage)

write(dest_dir, 'wonky', resultIMG, suffix)