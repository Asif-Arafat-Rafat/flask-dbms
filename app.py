from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os
import re
from create import extract_table_data
from removecmt import rmv_cmt
from fileSplit import fileSplit
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
    content=read_sql_file(os.path.join('./uploads',filename))
    data=fileSplit(filename,content)
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
    key=[]
    file=[filename,data]
    for i in data:
        for j in i['columns']:
            for h in j.keys():
                if h not in key:
                    key.append(h)
    return render_template('view.html',file=file,key=key)


def read_sql_file(file_path):
    with open(file_path,'r') as file:
        content=file.read()
        content=rmv_cmt(content)
    return content

if __name__ == '__main__':
    app.run(debug=True,port=5001)
