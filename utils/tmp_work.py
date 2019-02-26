import os 
from object_detection.utils import dataset_util

dir_name = 'data/images/'

file_name = 'data/annotations/trainval.txt'

images = []

for parent,dirnames,filenames in os.walk(dir_name):
	for filename in filenames:
		images.append(filename)

with open(file_name,'w+') as f:
	for i in images:
		f.write(i[:i.index('.')] + " \r\n")

a = dataset_util.read_examples_list(file_name)
print(a)