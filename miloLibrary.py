import os, shutil 


def findBooks():

	
	list = os.listdir("C:\\Users\\JT\\Downloads")

	for file in list:

		# Variables
		dest = "C:\\Users\\JT\\Downloads\\Milo_Books"
		source = "C:\\Users\\JT\\Downloads\\" + file  
		 

		# Create New Folder if it does not exist
		if not os.path.exists(dest):
			os.makedirs(dest)


		# Move epub 
		if file.endswith(".epub"):
			print("EPUB: " + file + " has been moved successfully!") 
			shutil.move(source, dest)

		# Move pdf 
		if file.endswith(".pdf"):
			print("PDF: " + file + " has been moved successfully!") 
			shutil.move(source, dest)

		if file.endswith(".txt"):
			print("PDF: " + file + " has been moved successfully!") 
			shutil.move(source, dest)

			
def findAudio():

	list = os.listdir("C:\\Users\\JT\\Downloads")

	for file in list:

		# Variables
		
		dest = "C:\\Users\\JT\\Downloads\\Milo_Audio"
		source = "C:\\Users\\JT\\Downloads\\" + file  
		 

		# Create New Folder if it does not exist
		if not os.path.exists(dest):
			os.makedirs(dest)


		if file.endswith(".mp3"): 
			print("MP3: " + file + " has been moved successfully!")
			shutil.move(source, dest)
		if file.endswith(".mp4"):
			print("MP4: " + file + " has been moved successfully!") 
			shutil.move(source, dest)
		if file.endswith(".wav"): 
			print("WAV: " + file + " has been moved successfully!")
			shutil.move(source, dest)

		


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







