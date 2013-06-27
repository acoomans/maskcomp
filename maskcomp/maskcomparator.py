import Image
import math, operator
import os.path

def mask_image(image, mask):
	image.paste(mask, (0, 0), mask.convert('RGBA'))
	return image

def compare_images(image1, image2):
	h1 = image1.histogram()
	h2 = image2.histogram()
	rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
	return rms

def compare(image1, image2, mask=False):
	if isinstance(image1, str): image1 = Image.open(image1)
	if isinstance(image2, str): image2 = Image.open(image2)
	if isinstance(mask, str) and os.path.isfile(mask): mask = Image.open(mask)
	else: mask = False
	
	if mask:
		return compare_images(
			mask_image(image1, mask),
			mask_image(image2, mask)
		)
	else:
		return compare_images(image1, image2)