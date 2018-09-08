import cv2
import os

ROOT_DIR = os.path.abspath("./")
IMAGE_DIR = os.path.join(ROOT_DIR, "images")

file_names = next(os.walk(IMAGE_DIR))[2]
print('filename', file_names)

for i in file_names:
	if os.path.sliptext(i)[1] == '.jpg' or 'jpeg':
		image = cv2.imread(os.path.join(IMAGE_DIR, i))
		newfilename = i.replace(".jpg", ".png")
		cv2.imwrite(os.path.join(IMAGE_DIR, newfilename), image)
