import inspect
import re
from removecmt import rmv_cmt_py
def printMe(prt):
    info=inspect.stack()[1]
    path=info.filename
    line=info.lineno
    if isinstance(prt,(list,tuple)):
        content="\n".join(str(item)for item in prt)
    elif isinstance(prt,(dict)):
        content=""
        for i in prt.keys():
            content=content+(f"\n{i}:{prt[i]}")
    else:
        content=prt
    print(f"\n\n_______{path}_at {line}__{type(prt)}___________\n")
    print(content)
    print("\n_____________________\n\n")
    
def garbagefilter():
    file=inspect.stack()[1]
    print(file.filename.split("/")[-1])
    loc=f"./garbageCode/{file.filename.split('/')[-1]}"
    with open(file.filename,'r') as f:
        content=f.read()

    content1=re.findall(r"#.*",content)
    for con in content1:
        with open(loc,'a') as w:
            w.write(f"{con}\n")
    content2=re.findall(r"'''.*?'''",content,re.DOTALL)
    for con in content2:
        with open(loc,'a') as w:
            w.write(f"{con}\n")
    content=rmv_cmt_py(content)
    with open(file.filename,'w') as f:
        f.write(content)