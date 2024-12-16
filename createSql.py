import re
from col_data import col
from helper import printMe,garbagefilter
from createCol import getCol
import random
table_info={}

def spliter(col):
    br=re.findall(r"(\(.*?\))",col,re.DOTALL|re.IGNORECASE)
    brc={}
    for b in br:
        var= f"___BRprot3cti0n_{random.randint(100000,999999)}"
        brc[var]=b
        col=col.replace(b,var)
    # print(brc)
    ecol= re.findall(r"(.*?)(?:,|$)",col,re.DOTALL|re.IGNORECASE)
    
    return [ecol,brc]
        


def extract_table_data(content,checked):
    if checked is True:
        chk=f"./tmp/{content}CreateTab.tql"
        with open(chk,'r') as c:
            content=c.read()
    info={}
    fnd= re.findall(r"create table\s*(IF NOT EXISTS)?\s*(`[^`]*`|\S+)\s\((.*?)\s*;",content,re.IGNORECASE|re.DOTALL)
    for i in fnd:
        n=re.findall(r".*\)",i[2],re.DOTALL|re.IGNORECASE)
        a=n[0].replace('\n',"").strip().replace("  "," ")
        a=a[:-1] if a[-1]==")" else a 
        a=spliter(a)
        # for i ,e in enumerate(a[0]):
        #     a[0][i]=a[0][i].strip(" ")
        #     for k,v in a[1].items():
        #         a[0][i]=a[0][i].replace(k,v)
        info[i[1]]=a
    for i in info:
        j=getCol(info[i])
        info[i]=j
    return info
   