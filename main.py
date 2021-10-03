from flask import * 
from werkzeug.debug import DebuggedApplication
from main import app
from bs4 import BeautifulSoup
import requests
import camelot
import pandas as pd 
from openpyxl import load_workbook
from openpyxl.styles.numbers import FORMAT_PERCENTAGE
from filter import filter

app = DebuggedApplication(app, evalex=True)
app = Flask(__name__)

HTMLFile = open('./data/outline2.html', "r")

# read the HTML file
index = HTMLFile.read()

soup = BeautifulSoup(index, "html.parser")
tables = camelot.read_pdf('./data/outline2.pdf')
weight_table = tables[0]

@app.route('/')  
def hello():  
    return render_template("index.html")

# 
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # uploaded_file.save('Files/' + uploaded_file.filename)
        filter(soup,weight_table) # this function will generate the excel sheet call output.xlsx
        return redirect('success')
    return render_template(url_for('index'))

@app.route('/success')
def success():
    return render_template('success.html')

  
if __name__ == '__main__':  
    app.run(debug = True)  