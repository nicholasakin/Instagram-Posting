# Instagram-Posting

Application posts to instagram photos with corresponding descriptions from a specified folder. 

Originally labled "PicsToPost"

After posting, the program moves the pictures and images to a backup folder originally called "PostedPics"

Upon running the application, a prompt is given for a username and password. This information is stored
locally in "secret.txt" inside the config folder. If application is shared, DELETE config folder as it is
generated if not found. 

USER AND PASSWORD FOR FIRST RUN AHVE TO BE STORED AS ENVIRONMENT VARIABLES/TYPED INTO CODE - 
can reference "secret.txt" after if desired (this implementation uses only the environment vars)


Images and descriptions should be labeled post1.jpg, post2.jpg, ... post#.jpg and 
post1.txt, post2.txt ... post#.txt for program to find files correctly

Program can be modified to post a picture once a day for a month, once a minute, or 
whatever time specification is desired!

Inside of the postPhoto method: "month", "startDay", "endDay" have to be modified for users desired day or time of post
Descriptions on modification are in code
