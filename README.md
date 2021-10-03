# GoldenHack

This is a webapp that allow user to upload their course outline and get a downloadable excel sheet after it is uploaded. 

### The filtering/ extract method
The filtering of the course outline is done by converting the pdf file into HTML structure. This is to allow us to have a easier structure to navigate throught and locate the keyword that we need such as Instructor info, Schedule, and Weighting. We use Camelot to find potential table where most of the schedule or weighting information will be presented in tables. We use Beautiful Soup to navigate throught the converted HTML and get the keywords that we need. 

This solution is not perfect and not scalable. We are planning to further extend the filtering system with computer vision and machine learning. We can use computer vision to scan through the file and give us the most important part of the page and feed into a ML system where we can predict which part do we need to extract. 

### The modify
After getting all the data into an excel file, we use openpyxl to modify the Weighting sheets where we locate the columns of weight and started to modify the weightage by changing the number formate in excel, so that the calculation can be done easily after the user downloaded the file. This part is not scalable too but we are planning to brainstorm more idea to make this processs more "smart"
