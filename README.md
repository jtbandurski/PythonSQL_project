# PythonSQL-Project
PythonSQL project, group members: Ahmed Abdelmaksoud, Jakub Bandurski, Hamed Ahmed Hamed Ahmed

-- We Are using github to ease the process of integrating the code between us and to simulate the work as a team
-- for the project we are using Django , and Django is following MVT pattern which divide the structure into
 Mode => responsible for the database tables
 View => responsible for recieving the user request and render the write view to the user as response 
 template => contain all the visualization part that is related to the html

-- there is a PDF file "Habit-Tracker-Report.pdf" contain a describtion about the project Idea and the requirment installtion to run the project.
-- The project Structure contain 2 application 
- Habitstracker app => whiche only contain the main route to the application iside the urls.py file 

- BackEnd 
our main code is inside the habits folder 
- models.py contain the classes that refelct the tabls inside the databse
- urls.py contain the route for each page 
- views.py contain the main functionality which is reponsible about read/write the data from the database 
and processing these data to be rendered in the suitable html page

-- Database 
we are using sqlite the databse name is "database.db"

-- front-end 

we are using html, javascript css, and bootstrap
all the html part is inside "templates" file
all the css/js/bootstrap files are inside "static" file

