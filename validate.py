import re
def validate(con1,con2,action):
    if action=='create':
        pattern="CREATE TABLE"
        if len(re.findall(pattern,con1,re.IGNORECASE))==len(re.findall(pattern,con2,re.IGNORECASE)):
            return True
        else:
            return False
    elif action=='insert':
        pattern="INSERT TABLE"
        if len(re.findall(pattern,con1,re.IGNORECASE))==len(re.findall(pattern,con2,re.IGNORECASE)):
            return True
        else:
            return False
    elif action=='alter':
        pattern="Alter TABLE"
        if len(re.findall(pattern,con1,re.IGNORECASE))==len(re.findall(pattern,con2,re.IGNORECASE)):
            return True
        else:
            return False