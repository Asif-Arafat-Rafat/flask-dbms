import re
from get_keys import get_key
def col(column,sptype):
    print(sptype)
    if(re.search(r"^PRIMARY KEY",column,re.IGNORECASE) or re.search(r"^FOREIGN KEY",column,re.IGNORECASE)):
        data=dict(more_info=re.findall(r"(\w+)",column))
        # print(data)
        # get_key(column.strip(","))
    elif(column[0]=='`'):
        cold=re.search("`(.*)`\s*(.*)",column)
        cold=[cold.group(1),cold.group(2)]
        cold1=re.findall("(\w+)\(?(\d+)?\)?",cold[1])
        cold2=[(name,size) if size else name for name,size in cold1]
        if cold2[0] in sptype.keys():
            cold2[0]=sptype[cold2[0]]
        data=dict(name=cold[0],datatype=(cold2[0]),more_info=cold2[1:])
        
    else:
        cold=re.findall("(\w+)\s*\(?(\d+)?\)?",column)
        cold1=[(name,size) if size else name for name,size in cold]
        if cold1[1] in sptype.keys():
            cold1[1]=sptype[cold1[1]]

        data=dict(name=cold1[0],datatype=cold1[1],more_info=cold1[2:])

    data= data|get_key(data['more_info'])
    if data['key']=='PRIMARY':
        data['default']='NOT NULL'
    if 'not_null' in data:
        data['default']='NOT NULL'
    if 'default' not in data:
        data['default']='NULL'
    return data