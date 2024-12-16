import re
def replace_values(input_dict, replacements):
    
    for key, value in input_dict.items():
        if isinstance(value, str):
            for placeholder, replacement in replacements.items():
                value = value.replace(placeholder, replacement)
            input_dict[key] = value
        elif isinstance(value, list):
            input_dict[key] = [replacements.get(v, v) for v in value]
    return input_dict
def foreign_key_dec(c,locks):
    # print(c)
    c=c.replace(" _","_")
    if f_k:=re.findall(r"foreign key(.*?)\sreferences\s*(.*?)\s*(.*)",c,re.IGNORECASE):
        return(f_k)
    ref=re.findall(r"\sreferences\s(.*?)\s",c,re.IGNORECASE)
    return ref
def colDiff(c,locks):
    c=re.sub(r"\s*\(","(",c).strip(" ")
    # print(c)
    data={}
    if key:=re.search(r"\b(primary|foreign|unique)\b\s*(?:key)?",c,re.IGNORECASE):
        data['Key']=key[0]
        c=c.replace(data['Key'],"")
    if default:=re.search(r"\b(auto_increment|default\s*'?([a-zA-Z0-9_]+)'?\b|not null|null)\b",c,re.IGNORECASE):
        # print("entered")
        data['Default']=default[0]
        # print(data['Default'])
        c=c.replace(data['Default'],"")
    if c[0]=="`":
        more_info=re.match(r"`(?P<name>.*?)`(?P<data>.*)",c,re.DOTALL|re.IGNORECASE)
        name=more_info['name']
        data['more_info']=more_info['data'].strip(" ").split(" ")
    else:
        info=c.split(" ")
        name=info[0]
        data['more_info']=info[1:]
    data['DataType']=data['more_info'][0]
    data['more_info']=data['more_info'][1:]
    data['name']=name
    data=replace_values(data,locks)
    return(data)

def getCol(col):
    lst=[]
    col[0]=list(filter(lambda x:x!="",col[0]))
    for c in col[0]:
        if re.search(r"references",c,re.IGNORECASE):
            for i , v in col[1].items():
                c=c.replace(i,v)
            print(c.strip(" "))
        else:
            lst.append(colDiff(c,col[1]))
    return lst

colDiff("job_title ENUM('Manager', 'Developer', 'Analyst', 'Intern') DEFAULT 'Intern'",{})