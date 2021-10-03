from flask import * 
import os
from werkzeug.debug import DebuggedApplication
from werkzeug.utils import secure_filename
from main import app
from openpyxl import load_workbook
from openpyxl.styles.numbers import FORMAT_PERCENTAGE
from filter import filter
from values import get_vals

app = DebuggedApplication(app, evalex=True)
app = Flask(__name__)

UPLOAD_FOLDER = './uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')  
def hello():  
    return render_template("index.html")
 

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('Files/' + uploaded_file.filename)
        file = list(uploaded_file.filename.split('.'))[0]
        soup, weight_table = get_vals(file)
        filter(file, soup,weight_table) # this function will generate the excel sheet call output.xlsx
        return redirect('/downloadfile/'+ file)
    return render_template(url_for('index'))


# @app.route('/success')
# def success():
#     return render_template('done.html')

@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html',value=filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = UPLOAD_FOLDER + filename + '.xlsx'
    print(file_path)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':  
    app.run(debug = True)  