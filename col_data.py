import re
from get_keys import get_key
def col(column):
    if(column[0]=='`'):
        cold=re.search("`(.*)`\s*(.*)",column)
        cold=[cold.group(1),cold.group(2)]
        cold1=re.findall("(\w+)\(?(\d+)?\)?",cold[1])
        cold2=[(name,size) if size else name for name,size in cold1]
        data=dict(name=cold[0],datatype=cold2[0],more_info=cold2[1:])
        
    else:
        cold=re.findall("(\w+)\s*\(?(\d+)?\)?",column)
        cold1=[(name,size) if size else name for name,size in cold]
        data=dict(name=cold1[0],datatype=cold1[1],more_info=cold1[2:])

    print("\n\n")
    print(data)
    print("\n\n")
    return data|get_key(data['more_info'])