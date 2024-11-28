import re
import ast
import os
from validate import validate
def fileSplit(filename,content):
    fileSplitCreate(filename,content)
    
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