from bs4 import BeautifulSoup
import requests
import camelot
import pandas as pd 
from openpyxl import load_workbook
from openpyxl.styles.numbers import FORMAT_PERCENTAGE





# # get the html file (we might need to build it )
# HTMLFile = open('./data/outline2.html', "r")

# # read the HTML file
# index = HTMLFile.read()

# soup = BeautifulSoup(index, "html.parser")
# tables = camelot.read_pdf('./data/outline2.pdf')
# weight_table = tables[0]

def filter(soup , weight_table):

    class prof:
        def __init__(self, x, y):
            self.x, self.y = x, y


    #TODO: Weighting of each element -> create a function that can create the calcuation 
    df = weight_table.df
    df = df.rename({0: "component" , 1 : "weight"} , axis=1)
    df = df.iloc[1:, : ]

    # name
    prof_info = []
    try: 
        instructor_name = soup.find(text="Name:").parent.parent.findNext('td').contents[0]
        name = prof("name",instructor_name.text.strip())
        prof_info.append(name)
    except:
        instructor_name = soup.find(text="Instructor").parent.parent.parent.find_next_sibling('tr').findNext('td').contents[0]
        name = {"name": instructor_name.text.strip()}
        prof_info.append(name)

    #email
    email = soup.find(text="Email:").parent.parent.findNext('td').contents[0]
    email = prof("email",email.text.strip())
    prof_info.append(email)

    # office location
    office = soup.find(text="Office:").parent.parent.findNext('td').contents[0]
    office = prof("office",office.text.strip())
    prof_info.append(office)

    # office hours
    try: 
        instructor_office_hrs = soup.find(text="Office Hours:").parent.parent.findNext('td').contents[0]
        office_hrs = prof("office_hrs",instructor_office_hrs.text.strip())
        prof_info.append(office_hrs)
    except:
        print("No Office Hours Yet")

    prof_df = pd.DataFrame([t.__dict__ for t in prof_info])


    date_list = []
    topic_list=[]
    #TODO: course schedule -> with google calender integration
    # find the tr that has td=week , td=Date , td=Topic
    page_9 = soup.find('div', {"id": "page_9"})
    schedule_header = page_9.find(lambda tag: tag.name == "td" and "Date" in tag.text)
    schedule_table = schedule_header.parent.parent
    tr_elements = schedule_table.find_all('tr')
    for i , tr in enumerate(tr_elements, 0):
        if(i > 5):
            for j, td in enumerate(tr,0):
                p_tag = td.find("p")
                if(p_tag == -1 ):
                    continue
                else:
                    if (j == 1): 
                        date = p_tag.getText()
                        date_list.append(date)
                    else:
                        topic = p_tag.getText()
                        topic_list.append(topic)

    schedule_df = pd.DataFrame({'date': date_list,'topic': topic_list})


    with pd.ExcelWriter('output.xlsx') as writer:
        prof_df.to_excel(writer , sheet_name="Prof_info")
        schedule_df.to_excel(writer, sheet_name="Schedule")
        df.to_excel(writer, sheet_name="Course Weight")
    wb= load_workbook(filename="./output.xlsx")
    book = wb.active
    sheet = wb["Course Weight"]
    sheet["D1"]= "Your input"
    sheet["E1"]= "Total Score"

    for i , cellObj in enumerate(sheet['E'], start=1):
        if i > 1 :
            sheet[f"C{i}"]= int(sheet[f"C{i}"].value) / 100 
            sheet[f"C{i}"].number_format = FORMAT_PERCENTAGE
            cellObj.value =f'=C{i}*D{i}'
    sheet["D7"] = "Total"
    sheet["E7"].value ='=E2+E3+E4+E5+E6'

    wb.save('output.xlsx')
    wb.close





