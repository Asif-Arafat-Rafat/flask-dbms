import re
from col_data import col
from helper import printMe,garbagefilter
import random
def extract_table_data(content,checked):
  if checked is True:
    chk=f"./tmp/{content}CreateTab.tql"
    with open(chk,'r') as c:
      content=c.read()
  info=[]
  content=ex_datatype(content)
  sptype=content[1]
  content=content[0]
  pattern = r"CREATE TABLE\s+`?([\w\s]+)`?\s+\((.*?);"
  table_info = re.findall(pattern, content, re.DOTALL)
  for t in table_info:
    table_information=dict()
    table_information['name']=t[0]
    table_information['columns']=t[1]
    test(table_information['columns'])
    table_info=list(filter(None,t))
    info.append(table_information)
  for i in info:
    table_column=re.findall(r"(.*)\s*,?",i['columns'])
    table_column=list(filter(None,table_column))
    table_column=list(filter(lambda x: not x.startswith(")"),table_column))
    tbl=[]
    for tab in table_column:
      tabs=tab.strip(" ")
      tabs=tabs.strip(',')
      tab=col(tabs,sptype)
      if 'key_assign' in tab.keys():
        data_dict = {item['name']: item for item in tbl}
        result = data_dict.get(tab['key_assign'])
        result['key']=tab['key']
        tab.pop('key_assign')
        for key, value in tab.items():
          if key not in result:
            result[key] = value
      else:
        tbl.append(tab)
    i['columns']=tbl
  return info
def ex_datatype(columns):
  def varName(var):
    return f"___{var.upper()}_{random.randint(000000,999999)}"
  colower=columns.lower()
  var=dict()
  for sres in (re.findall(r"(enum\s*\(.*?\))",columns,re.IGNORECASE)):
    varname=varName('ENUM')
    var[varname]=sres
    columns=columns.replace(sres,varname)
  for sres in (re.findall(r"(set\s*\(.*?\))",columns,re.IGNORECASE)):

    varname=varName('SET')
    var[varname]=sres
    columns=columns.replace(sres,varname)
  for sres in (re.findall(r"(decimal\s*\(.*?\))",columns,re.IGNORECASE)):
    varname=varName('DECI')
    var[varname]=sres
    columns=columns.replace(sres,varname)
  if 'numeric' in colower:
    sres=re.search(r"(numeric\s*\((.*?)\))",columns,re.IGNORECASE).group(1)
    varname=varName('NUM')
    var[varname]=sres
    columns=columns.replace(sres,varname)
  if 'index' in colower:
    sres=re.search(r"(index\s*\((.*?)\))",columns,re.IGNORECASE)
    varname=varName('IDX')
    var[varname]=sres
    columns=columns.replace(sres,varname)
  if 'interval' in colower:
    sres=re.search(r"(interval\s*\((.*?)\))",columns,re.IGNORECASE)
    varname=varName('ITV')
    var[varname]=sres.group(1)
    columns=columns.replace(sres,varname)  
  if 'geometry' in colower:
    sres=re.search(r"(geometry\s*\((.*?)\))",columns,re.IGNORECASE)
    varname=varName('GEO')
    var[varname]=sres.group(1)
    columns=columns.replace(sres,varname)  
  return [columns,var]

def test(columns):
  dt=ex_datatype(columns)
  # print(dt[0])
  # print(dt[1])
  colower=columns.lower()
  dataC=dict()
  # mulC=re.findall(r"(\w+\s*\((.*\))",columns)
  # print(mulC)
  pat=columns.split(') E')[0]
  pat=pat.replace(' (',"(")
  cleaned_data = [item.strip() for item in pat]
  
  # print(pat)
  
  for data in cleaned_data:
    # print(data)
    dat=data.split('`')
    dat=list(filter(None,dat))
    if len(dat)>1:
      dataC['name']=dat[0]
      dataC['type']=dat[1]
    else:
      # print(f"Data::{data}")
      dataa=data.split(' ')
      dataa=list(filter(None,dataa))
      # print(f"Dataa::{dataa}")

    # print(dataC)


