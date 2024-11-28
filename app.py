from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os
import re
from retable2 import extract_table_data

app = Flask(__name__)
app.secret_key='secret'
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route('/uploads',methods=['POST'])
def upload():
    file=request.files['file']
    filename=file.filename
    ext=filename.split('.')[-1]
    if ext not in ['db','sql']:
        flash('Invalid file type')
        return redirect(url_for('index'))
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    flash('File uploaded successfully')
    return redirect(url_for('index'))
  
@app.route('/form',methods=['GET','POST'])
def form():
    return render_template('form.html')
  
@app.route('/')
def index():
    files= os.listdir('./uploads')
    return render_template('index.html',files=files)

@app.route('/view/<filename>')
def view(filename):
    sql_path=os.path.join('./uploads',filename)
    sql_content=read_sql_file(sql_path)
    data=extract_table_data(sql_content)
    file=[filename,data]
    # print(data)
    return render_template('view.html',file=file)


def read_sql_file(file_path):
    with open(file_path,'r') as file:
        content=file.read()
    return content

if __name__ == '__main__':
    app.run(debug=True,port=5001)
