from flask import * 
from werkzeug.debug import DebuggedApplication
from main import app

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
        return redirect('success')
    return render_template(url_for('index'))

@app.route('/success')
def success():
    return render_template('success.html')
  
if __name__ == '__main__':  
    app.run(debug = True)  