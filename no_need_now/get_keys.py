from get_default import get_default
from helper import printMe
import random
import re
def get_key(more_info):
    # printMe(more_info)
    more_info_lower=[item.lower() for item in more_info]
    data=dict()
    if 'key' in more_info_lower:
        idx=more_info_lower.index('key')
        data['key']=more_info[idx-1]
        more_info.pop(idx)
        more_info.pop(idx-1)
        more_info_lower.pop(idx)
        more_info_lower.pop(idx-1)
        if data['key'].lower()=='foreign':
            idx=more_info_lower.index('references')+1
            data['key_assign']=more_info[idx-2]
            data['key']=f"FOREIGN\nREFERENCES {more_info[idx]}({more_info[idx+1]})"
            # printMe(data)
            more_info.pop(idx+1)
            more_info.pop(idx)
            more_info.pop(idx-1)
            more_info_lower.pop(idx+1)
            more_info_lower.pop(idx)
            more_info_lower.pop(idx-1)
            if 'on' in more_info_lower:
                idx=more_info_lower.index('on')
                data[f"{more_info[idx]} {more_info[idx+1]}"]=more_info[idx+2:]
                for i in range(idx,len(more_info)):
                    # print(more_info)
                    # print(more_info_lower)
                    more_info.pop(idx)   
        return data
    elif 'unique' in more_info_lower:
        more_info.pop(more_info_lower.index('unique'))
        data['key']='UNIQUE'
    else:
        data['key']='NOT PRIMARY KEY OR UNIQUE'
    if 'on' in more_info_lower:
        idx=more_info_lower.index('on')
        data[f"{more_info[idx]} {more_info[idx+1]}"]=more_info[idx+2:]
        for i in range(idx,len(more_info)):
            # print(more_info)
            # print(more_info_lower)
            more_info.pop(idx)       
    return data|get_default(more_info)

def get_key_str(cmd):
    command=cmd.lower().replace('\n',' ').replace(',',' ').split(" ")
    command=list(filter(None,command))
    cmd2=cmd.lower()
    if 'primary' in command:
        ("PRIMARY KEY")
        if (key:=re.search(r"\((.*)\s*PRIMARY\s*KEY,",cmd,re.DOTALL)):
            k=key.group(1).strip()
            if(k[0]=='`'):
                col_name=re.search(r"`(.*)`",k,re.DOTALL)
                (col_name.group(1))
            # else:
            #     print(k.split(' ')[0])
        elif (key:=re.search(r".*\s*PRIMARY\sKEY\s*\(`(.*)`\)",cmd,re.DOTALL)):
            (k:=key.group(1).strip(" "))
        key=dict(key=f"PRIMARY KEY" ,key_assign=k)
        return key
    # if 'unique' in command:
    #     key=re.findall(r"\s*unique(?:\s*key)?\s*\((.*)\)",cmd2)
    #     key=dict(key=f"UNIQUE KEY", assign=key.strip())
    #     # print(key)
    if 'foreign' in command:
        key=re.findall(r"\s*foreign\s*key\s*\((.*)\)\s*references\s*(.*)\s*\((.*)\)",cmd2)
        key=dict(key=f"FOREIGN KEY ({key[0][0]}) REFERENCES {key[0][1]}({key[0][2]})")
        return (key)

    
