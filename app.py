from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os
import re
from alter import alter
from createSql import extract_table_data
from removecmt import rmv_cmt
from fileSplit import fileSplit,preChk
from data_change import data_assign
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

def read_sql_file(file_path):
    with open(file_path,'r') as file:
        content=file.read()
        content=rmv_cmt(content)
    return content

@app.route('/view/<filename>')
def view(filename):
    sql_path=os.path.join('./uploads',filename)
    sql_checker=preChk(filename)
    if sql_checker[0] is False:
        sql_content=read_sql_file(sql_path)
        data=extract_table_data(sql_content,False)
    else:
        data=extract_table_data(filename,True)
    # if sql_checker[1] is False:
    #     sql_content=read_sql_file(filename)
    #     data1=alter(data,sql_content,False)
    # else:
    #     data1=alter(data,filename,True)
    # # data_assign(data,data1)
    key=[]
    file=[filename,data]
    key=data.keys()
    return render_template('view.html',file=file,key=key)


if __name__ == '__main__':
    app.run(debug=True,port=500)
