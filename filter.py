from bs4 import BeautifulSoup
import requests
import camelot
import pandas as pd 
from openpyxl import load_workbook
from openpyxl.styles.numbers import FORMAT_PERCENTAGE




# get the html file (we might need to build it )
HTMLFile = open('./data/outline2.html', "r")

# read the HTML file
index = HTMLFile.read()

soup = BeautifulSoup(index, "html.parser")
tables = camelot.read_pdf('./data/outline2.pdf')
weight_table = tables[0]



#TODO: find the instructor contact ( name , office hours, office location~zoom link , email)




# name
try: 
    instructor_name = soup.find(text="Name:").parent.parent.findNext('td').contents[0]
    print(instructor_name.text.strip())
except:
    instructor_name = soup.find(text="Instructor").parent.parent.parent.find_next_sibling('tr').findNext('td').contents[0]
    print(instructor_name.text.strip())

#email
email = soup.find(text="Email:").parent.parent.findNext('td').contents[0]
print(email.text)

# office location
office = soup.find(text="Office:").parent.parent.findNext('td').contents[0]
print(office.text)

# office hours
try: 
    instructor_office_hrs = soup.find(text="Office Hours:").parent.parent.findNext('td').contents[0]
    print(instructor_office_hrs.text.strip())
except:
    print("No Office Hours Yet")

# write those info to excel spreadsheet 
# create a dataframe

#TODO: lecture hours 

#TODO: Weighting of each element -> create a function that can create the calcuation 
df = weight_table.df
df = df.rename({0: "component" , 1 : "weight"} , axis=1)
df = df.iloc[1:, : ]
df.to_excel("output.xlsx", sheet_name="Course Weight")
wb= load_workbook(filename="./output.xlsx")
sheet = wb.active
sheet["D1"]= "Your input"
sheet["E1"]= "Total Score"

for i , cellObj in enumerate(sheet['E'], start=1):
    if i > 1 :
        sheet[f"C{i}"]= int(sheet[f"C{i}"].value) / 100 
        print(sheet[f"C{i}"].value)
        sheet[f"C{i}"].number_format = FORMAT_PERCENTAGE
        cellObj.value =f'=C{i}*D{i}'
sheet["D7"] = "Total"
sheet["E7"].value ='=E2+E3+E4+E5+E6'
wb.save('output.xlsx')
wb.close



#TODO: course schedule -> with google calender integration
# find the tr that has td=week , td=Date , td=Topic
schedule_header = soup.find(lambda tag: tag.name == "td" and "Date" in tag.text)
schedule_table = schedule_header.parent.parent
table_data = schedule_table.findChildren("tr", recursive=False)

# find the tr that has td=Date , td=Description





