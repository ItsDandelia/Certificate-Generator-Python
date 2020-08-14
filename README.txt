# Certificate-Generator-Python


This project is used to generate Certificates using Python script. It also has GUI for user's convinence. There two tabs in GUI. Many times suppose a workshop is conducted for 3 days
then we want to provide certificates to only those the participants who have attended the workshop for all 3 days. The first tab in GUI does the similar work. There we are supposed to
provide spreadsheet IDs of Google sheet for the attendance of respective days, workshop name and year of conduction of that workshop is also needed and this will generate a new Google sheet with
the common names and unique IDs with it. In the second tab, i.e. the Certificate Generator tab there we are supposed to input the spreadsheet ID of the sheet that was created in first tab.
Now a basic png or jpg template will be loaded on which text from the Google sheet created will be pasted using Pillow library. Afer setting the coordinates for the text and pasting the
generated certificate will be stored in the specified location as well as on Google Drive(just for user's access from anywhere). Here, I have used Google's Sheets and Drive API. Generally,
the text to be pasted using Pillow library depends on many coordinates, so I have tried to minimise the no. of coordinates involved. The GUI was designed using PyQt5 designer and then its
Python script was imported and necessary changes were made to it. Here are the packages which should be installed before running the script:

pip install Pillow         #For adding text on template
pip install googleapiclient #For using Google APIs
pip install pyqt5	#For using PyQt5 
pip install pyqt5-tools    #For using PyQt5 Designer
