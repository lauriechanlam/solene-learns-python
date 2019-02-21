#!/usr/bin/env python
import os

def create_directory():
	directory = 'rename'
	n = 1
	while os.path.exists(directory):
		directory = 'rename_' + str(n).zfill(2)
		n = n + 1
	os.makedirs(directory) # create the directory
	print('created directory ' + directory) # show information to user
	return directory

def get_mudbox_files_in_folder():
	return ['u0_v0.tif', 'u0_v1.exr', 'u1_v0.tiff']

def transform_file(filename):
	pass

######################################################

create_directory()
files = get_mudbox_files_in_folder()
for file in files:
	transform_file(file)

print 'done'
