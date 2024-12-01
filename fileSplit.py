import re
import ast
import os
from helper import printMe
from validate import validate
def fileSplit(filename,content):
    fileSplitCreate(filename,content)
    fileSplitAlter(filename,content)
    fileSplitInsert(filename,content)
def preChk(filename):
    con=[]
    con.append(chkFile(filename,'create'))
    con.append(chkFile(filename,'alter')) 
    con.append(chkFile(filename,'insert'))
    printMe(con)
    return con
    
def chkFile(filename,action):
    if action == 'create':
        file=f"./tmp/checker"
        with open(file,'r') as f:
            content=f.read()
        if re.search(rf"___\s*{filename}:::create\s*___",content):
            return True
        else:
            return False
    elif action == 'alter':
        file=f"./tmp/checker"
        with open(file,'r') as f:
            content=f.read()
        if re.search(rf"___\s*{filename}:::alter\s*___",content):
            return True
        else:
            return False
    elif action == 'insert':
        file=f"./tmp/checker"
        with open(file,'r') as f:
            content=f.read()
        if re.search(rf"___\s*{filename}:::insert\s*___",content):
            return True
        else:
            return False
    else:
        return "somethings wrong "
    
def fileSplitCreate(filename,content):
    cre=re.findall(r"CREATE TABLE `?.*?`?\s*\(.*?\)(?:\s*ENGINE=.*?)?\s*;",content,re.DOTALL)
    loc=f"./tmp/{filename}CreateTab.tql"
    chk=f"./tmp/checker"
    with open(loc,'w') as f:
        f.write("")
    for c in cre:
        with open(loc,'a') as f:
            f.write(c)
            f.write("\n________________________\n")

    with open(loc,"r") as f:
        con1=f.read()
    if validate(con1,content,"create"):
        with open(chk,"a") as f:
            f.write(f"___ {filename}:::create ___\n")
    else:
        print("validation failed")
        
def fileSplitInsert(filename,content):
    cre=re.findall(r"INSERT INTO `?.*?`?\s*\(.*?\)\s*;",content,re.DOTALL)
    loc=f"./tmp/{filename}Insert.tql"
    chk=f"./tmp/checker"
    with open(loc,'w') as f:
        f.write("")
    for c in cre:
        with open(loc,'a') as f:
            f.write(c)
            f.write("\n_____\n")
    with open(loc,"r") as f:
        con1=f.read()
    if validate(con1,content,"insert"):
        with open(chk,"a") as f:
            f.write(f"___ {filename}:::insert ___\n")

def fileSplitAlter(filename,content):
    cre=re.findall(r"ALTER Table\s*.*?;",content,re.DOTALL|re.IGNORECASE)
    loc=f"./tmp/{filename}Alter.tql"
    chk=f"./tmp/checker"
    with open(loc,'w') as f:
        f.write("")
    for c in cre:
        with open(loc,'a') as f:
            f.write(c)
            f.write("\n_____\n")
    with open(loc,"r") as f:
        con1=f.read()
    if validate(con1,content,"alter"):
        with open(chk,"a") as f:
            f.write(f"___ {filename}:::alter ___\n")
    else:
        print("Alter Validation Failed")
        
