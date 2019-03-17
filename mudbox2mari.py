#!/usr/bin/env python


### TO DO IN ORDER TO EXECUTE THIS CODE

# If you are on Windows, install Notepad++ (https://notepad-plus-plus.org/).
# Then you can open this file in Notepad++ and see that the text is colored.
# This helps hugely to highlight the structure of the code

# Download and install Python 3 (https://www.python.org/downloads/)

# Open the command line tool (type 'cmd' in the start menu and select the first option)
# In the command line tool, navigate to where this file is (type 'cd C:\Users\<username>\Downloads' without quotes for example)
# Run this file by typing 'python3 mudbox2mari.py'


###  IMPORT UTILITIES ###

import re                                                                       # imports utilities in order to parse strings such as file names
import os                                                                       # imports utilities in order to create directories, list and copy files, etc.
import shutil                                                                   # imports utilities in order to copy the files to the new directory


### DEFINITION OF FUNCTIONS ###

def create_directory():                                                         # defines the function that will create a rename_xx directory
	directory = 'rename'                                                          # assigns the string 'rename' to the variable directory
	n = 1                                                                         # assigns the integer 1 to the variable called n
	while os.path.exists(directory):                                              # creates a loop that will run while the condition 'directory is a string that represents an existing OS directory' is met. if the condition is already met, the code inside the while-loop is never run
		directory = 'rename_' + str(n).zfill(2)                                     # part of the while-loop: assign the string 'rename_01', 'rename_02', etc. to the variable directory
		n = n + 1                                                                   # part of the while-loop: increment the value of the integer n by 1
	os.makedirs(directory)                                                        # we now know that directory is a variable that contains a string representing a non-existing OS directory, we can create the OS directory!
	print('created directory ' + directory)                                       # we show information to the user
	return directory                                                              # when the code calls the create-directory function (writen as create_directory()), it can retrieve the name of the created directory. This is useful in order to know in which directory to copy the files (is it rename, rename_01 or rename_02 for example). After a return statement, the function has finished its execution.

def get_mudbox_files_in_directory():                                            # defines the function that will list the mudbox files in the current directory
	all_files_in_directory = os.listdir('.')                                      # assignes to the variable all_files_in_directory an array of strings. the strings represent all the files and directories present in the current directory
	pattern = 'u[0-8]_v[0-8]\..*'                                                 # mudbox files are called u then a number between 0 and 8, then _, then v, then a number bertween 0 and 8, then a dot (written \. in regular expression patterns), then any extension (written .* in regular expression patterns, . represents any character, * reprensents that they can appear as many times as we want). You don't need to understand this now.
	mudbox_files = [file for file in all_files_in_directory if re.match(pattern, file)] # assigns an array of string to mudbox_files. if re.match(pattern, file) is the condition that needs to be met for strings in all_files_in_directory to be kept in the array. All the strings that do not match the regular expression pattern are filtered out. We keep the files as is, we do not transform them this is why we write file for file. If we wanted to to prefix them with 'a_' (a_u0_v0.tif, a_u1_v1.epr, ewtc. for example) we would have written ('a_' + file) for file
	number_of_mudbox_files = len(mudbox_files)                                    # assigns an integer to the variable number_of_mudbox_files. this is the number of  elements in the mudbox_files array
	print(str(number_of_mudbox_files) + ' files to process')                      # prints information to the user. number_of_mudbox_files is an integer, we print only strings, so we convert number_of_mudbox_files to a string by writting str(number_of_mudbox_files)
	return mudbox_files                                                           # here we are only defining the behaviour of the function, when we are executing it, we need to retrieve the list of files in order to pass it to another function call. The return statement allows us to pass this value to another part of the code

def transform_file(directory, filename):
	u_and_v = re.findall('[0-8]', filename)                                       # assigns an array of strings to the variable u_and_v. this value is the list of values between 0 and 8 found in the filename provided. for example, if the filename is u0_v1.jpg, then u_and_v gets ['0', '1']. If the filename is u3_v7.jpeg2000, then u_and_v gets ['3', '7', '2', '0', '0', '0']. If the filename is uv.jpg, then u_and_v gets [].
	u = u_and_v[0]                                                                # assigns the string corresponding to the first element of the u_and_v array to the variable u. In Python and many programming languages, the first element of the array is accessible by using [0], the second element is accessible by using [1], etc.
	v = u_and_v[1]                                                                # assigns the string corresponding to the second element of the u_and_v array to the variable v.
	filename_parts = filename.split('.')                                          # assigns an array of strings to filename_parts. The parts are the segments of the filename separated by a dot. If the filename is 'u0_v0.tif', then the parts are ['u0_v0', 'tif']. If the filename is 'u5_v6', then the parts are ['u5_v6']. If the filename is 'u8_v1.jpg.tif' then the parts are ['u8_v1', 'jpg', 'tif']
	extension = filename_parts[len(filename_parts)-1]                             # assigns a string to the variable extension. This corresponds to the last element of the filename_parts array. We keep only the last part of the extension. For example, if filename_parts is ['u8_v1', 'jpg', 'tif'] then extension is 'tif'.
	new_filename = '10' + u + v + '.' + extension                                 # assigns a string to the variable new_filename. we use all the elements we computed in the previsous steps. The new filename corresponds to the Mari convention.
	new_fullfile = os.path.join(directory, new_filename)                          # the new file will be located into the directory. so we need to precise this before we actually copy the filename to new_filename.
	shutil.copyfile(filename, new_fullfile)                                       # copies the file called filename to the file called new_fullfile
	print('copied ' + filename + ' to ' + new_fullfile)                           # displays message to the user



### >EXECUTION ###
#
directory = create_directory()                                                  # assigns a string to the variable directory. this string is the return statement of the execution of the create_directory function.
files = get_mudbox_files_in_directory()                                         # assigns an array of strings to the variable files. this array is the result of the execution of the function get_mudbox_files_in_directory
for file in files:                                                              # defines a for-loop: for each element file of the array files, the following indented code will be executed
	transform_file(directory, file)                                               # for each file in files execute the function transform_file /!\ directory and file need to be in the right order.

print('done')                                                                   # once all files have been processed, print a message to the user
