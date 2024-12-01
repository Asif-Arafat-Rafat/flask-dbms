from helper import printMe
import re
from get_keys import get_key,get_key_str
def alter(data,content,checked):
    if checked is True:
        chk=f"./tmp/{content}Alter.tql"
        with open(chk,'r') as c:
            content=c.read()
    pattern = r"ALTER TABLE\s+`?([\w\s]+)`?\s+\(?(.*?);"
    alt=re.findall(pattern,content,re.DOTALL|re.IGNORECASE)
    for i in alt:
        # printMe(f"for table ::{i[0]}")
        # print(get_key_str(i[1]))
        l1=(i[1].split(","))
        for l in l1:
            l=l.lower()
            if "foreign" in l:
                for j in data:
                    if i[0]==j['name']:
                        # print("")
                            (switchkey(j,listalter(l)))
            
    # table=[]
    # for a in alt:
    #     pos=[]
    #     pos.append(a[0])
    #     tab=re.sub(r"\n"," ",a[1]).split(",")
    #     for t in tab:
    #         t=t.strip()
    #         pos.append(t)
    #     table.append(pos)
    # for tab in table:
    #     for i in range(1,len(tab)):
    #         (listalter(tab[0],tab[i]))

    
        
    
def listalter(sql):    
    pattern = r'(\b(ADD|DROP|MODIFY|RENAME|CHANGE|ALTER|SET)\b.*?)(?=,|$)'
    actions = re.findall(pattern, sql, re.DOTALL | re.IGNORECASE)
    # print(actions)
    act=(actions[0][0].split(" "))
    
    return(get_key(act))
    # act1=[]
    # # print(f"action:::::::::{actions}")
    # for action in actions:
    #     act=re.findall(ptr,action[0],re.IGNORECASE)
    #     if 'KEY' in act:
    #         # print(act)
    #         # print(f"::::::::::::{get_key(act)}")
    #         act1.append(get_key(act))
    # print(act1)
    
    # act=[]
    # for i in alt:
    #     print(i[1].split(","))
    #     tab=re.sub(r"\n"," ",i[1])
    #     ta=listalter(tab)
    #     # print((ta[0]))
def switchkey(data,lst):
    # printMe(lst)
    l=lst['key']
    l=l.replace("(","")
    l=l.replace(")","")
    for d in data['columns']:
        if d['name']==l:
            d["key"]=f"{lst['key']} from alter"
    return data
