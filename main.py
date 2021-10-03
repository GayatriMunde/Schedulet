from flask import * 
import os
from werkzeug.debug import DebuggedApplication
from main import app
from openpyxl import load_workbook
from openpyxl.styles.numbers import FORMAT_PERCENTAGE
from filter import filter
from values import get_vals

app = DebuggedApplication(app, evalex=True)
app = Flask(__name__)


@app.route('/')  
def hello():  
    return render_template("index.html")
 

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('Files/' + uploaded_file.filename)
        file = uploaded_file.filename
        soup, weight_table = get_vals(file)
        filter(soup,weight_table) # this function will generate the excel sheet call output.xlsx
        return redirect('success')
    return render_template(url_for('index'))


@app.route('/success')
def success():
    return render_template('done.html')

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)

  
if __name__ == '__main__':  
    app.run(debug = True)  