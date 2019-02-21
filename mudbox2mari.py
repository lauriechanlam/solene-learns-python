#!/usr/bin/env python

def create_directory():
	return 'rename'

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
