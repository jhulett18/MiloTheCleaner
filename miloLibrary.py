import os, shutil 


# Finds current user
user = os.getlogin()

def findBooks():

	


	list = os.listdir("C:\\Users\\" + user +"\\Downloads")
	

	for file in list:

		# Grabbing User's Download dir
		dest = "C:\\Users\\"+ user +"\\Downloads\\Milo_Books"

		BOOK_dest = "C:\\Users\\"+ user +"\\Downloads\\Milo_Books\\Books"
		DOC_dest = "C:\\Users\\"+ user +"\\Downloads\\Milo_Books\\Documents"
		source = "C:\\Users\\"+ user +"\\Downloads\\" + file  
		 

		# Create New Folder if it does not exist
		if not os.path.exists(dest):
			os.makedirs(dest)

		if not os.path.exists(BOOK_dest):
			os.makedirs(BOOK_dest)

		if not os.path.exists(DOC_dest):
			os.makedirs(DOC_dest)

		




		# Move epub 
		if file.endswith(".epub"):
			print("EPUB: " + file + " has been moved successfully!") 
			shutil.move(source, BOOK_dest)

		# Move pdf 
		if file.endswith(".pdf"):
			print("PDF: " + file + " has been moved successfully!") 
			shutil.move(source, DOC_dest)

		if file.endswith(".txt"):
			print("TXT: " + file + " has been moved successfully!") 
			shutil.move(source, DOC_dest)

			
def findAudio():

	# Dynamically grabbing all directories 
	list = os.listdir("C:\\Users\\"+ user +"\\Downloads")

	for file in list:

		# Variables
		dest = "C:\\Users\\"+ user +"\\Downloads\\Milo_Audio"
		MP3_dest = "C:\\Users\\"+ user +"\\Downloads\\Milo_Audio\\MP3"
		MP4_dest = "C:\\Users\\"+ user +"\\Downloads\\Milo_Audio\\MP4"
		WAV_dest = "C:\\Users\\"+ user +"\\Downloads\\Milo_Audio\\WAV"
		source = "C:\\Users\\"+ user +"\\Downloads\\" + file 
		 

		# Create New Folder if it does not exist
		
		if not os.path.exists(dest):
			os.makedirs(dest)

		if not os.path.exists(MP3_dest):
			os.makedirs(MP3_dest)

		if not os.path.exists(MP4_dest):
			os.makedirs(MP4_dest)

		if not os.path.exists(WAV_dest):
			os.makedirs(WAV_dest)



		if file.endswith(".mp3"): 
			print("MP3: " + file + " has been moved successfully!")
			shutil.move(source, MP3_dest)
		if file.endswith(".mp4"):
			print("MP4: " + file + " has been moved successfully!") 
			shutil.move(source, MP4_dest)
		if file.endswith(".wav"): 
			print("WAV: " + file + " has been moved successfully!")
			shutil.move(source, WAV_dest)

		


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







