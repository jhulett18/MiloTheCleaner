import os, shutil 


def findBooks():

	
	list = os.listdir("C:\\Users\\JT\\Downloads")

	for file in list:

		# Variables
		dest = "C:\\Users\\JT\\Downloads\\Books"
		source = "C:\\Users\\JT\\Downloads\\" + file  
		 

		# Create New Folder
		if not os.path.exists(dest):
			os.makedirs(dest)


		# Move file from source to new dest 
		if file.endswith(".epub"): 
			shutil.copy(source, dest)

			# del original file
			os.remove(source)
			print("Moved file: " + file + " BOOK to " + dest + " -- ALL DUPLICATES DELETED \n")
			
def findAudio():

	list = os.listdir("C:\\Users\\JT\\Downloads")

	for file in list:

		# Variables
		
		dest = "C:\\Users\\JT\\Downloads\\Audio"
		source = "C:\\Users\\JT\\Downloads\\" + file  
		 

		# Create New Folder if it does not exist
		if not os.path.exists(dest):
			os.makedirs(dest)


		# Move file from source to new dest 
		if file.endswith(".mp3"): 
			shutil.copy(source, dest)
		if file.endswith(".mp4"): 
			shutil.copy(source, dest)
		if file.endswith(".wav"): 
			shutil.copy(source, dest)

			# del original file
		os.remove(source)
		print("Moved file: " + file + " AUDIO to " + dest + " -- ALL DUPLICATES DELETED \n")
			
		
		
		



# Next is going to be walking through subdirs and dirs to collect files



# The actual walk through the directories works as you have coded it. If you replace the contents of the inner loop with a simple print statement you can see that each file is found:

# import os
# rootdir = 'C:/Users/sid/Desktop/test'

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         print os.path.join(subdir, file)

# If you still get errors when running the above, please provide the error message.

# Updated for Python3

# import os
# rootdir = 'C:/Users/sid/Desktop/test'

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         print(os.path.join(subdir, file))







