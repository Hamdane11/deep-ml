import numpy as np
def calculate_brightness(img):
	# Write your code here

	if len(img) ==0 or len(img[0]) ==0:
		return -1
	if any(len(ligne) != len(img[0]) for ligne in img   ):
		return -1
	img = np.asarray(img, dtype=float)

	if (img >=255).any()  or (img < 0).sum()>=1:
		return -1
	

	return round( float(np.mean(img)) , 2)


		
	
