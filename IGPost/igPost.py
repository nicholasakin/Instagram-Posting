import os, shutil, datetime, instabot
from instabot import Bot

#secret.txt should have username:password


#calculates number of pics
def getNumPics(photoPath):
	numPics = os.listdir(photoPath)
	numPics = int(len(numPics))/2 #should be a description for every picture
	return int(numPics);



#copies original photo & text to postedPics folder
#posts photo to ig
def postPhoto(picsToPost, textToPost, postedPics):
	

	#change month, start day, end day(inclusive), to be your desired dates
	#startDay < endDay
	#range of endDay - startDay should match number of pictures or numFiles/2
	month = 8 
	startDay = 11
	endDay = 16




	#gets number of pics to post
	numPics = getNumPics(picsToPost)		

	#Current time
	# %d-day of month, %m - month as number, %M - minute,
	dt = datetime.datetime.now();
	numberOfMonth = dt.strftime("%m") 	#month as number 01-12
	dayOfMonth = dt.strftime("%M") 		#month day as number 01-31

	#posts photo at specified time
	counter = 0 #Number of photos posted
	imageIndex = 1 #index of images
	if int(month) == int(numberOfMonth): 
		for i in range (startDay, endDay):
			#stays in loop until correct day/minute to post
			while int(startDay + counter) != int(dayOfMonth):
				
				dt = datetime.datetime.now();
				dayOfMonth = int(dt.strftime("%M"))
				

			#posts picture on specified time
			if int(startDay + counter) == int(dayOfMonth):
				#formats path to image and text file correctly
				pathToImage = picsToPost + "\\post" + str(imageIndex) + ".jpg"
				pathToText = textToPost + "\\post" + str(imageIndex) + ".txt"
				
				#gets image description
				file = open(pathToText, "r")
				descrip = file.read();

				#copies original image and description into postedPics folder
				shutil.copy(pathToImage, postedPics)
				shutil.copy(pathToText, postedPics)

				counter += 1
				imageIndex += 1
				#posts image
				print("posting: " + pathToImage)
				bot.upload_photo(pathToImage, caption = descrip)
	
	


		
	

#uses instabot library
bot = Bot()

#username and password stored in environment variables for safety
username = os.environ.get('igUser')
password = os.environ.get('igPass')

#username = YOURUSERNAME
#password = YOURPASSWORD


#logs into instagram
bot.login(username = username, password = password)

#paths to folders: "PicsToPost", "PostedPics"
picsToPost = "C:\\Users\\nicho\\Python\\Personal Projects\\IGPOST\\PicsToPost"
textToPost = "C:\\Users\\nicho\\Python\\Personal Projects\\IGPOST\\PicsToPost"
postedPics = "C:\\Users\\nicho\\Python\\Personal Projects\\IGPOST\\PostedPics" 


#posts photos
postPhoto(picsToPost, textToPost, postedPics)