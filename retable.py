import re

def extract_table_data(content):
  table_name = re.findall(r"CREATE TABLE `(\w+)` (.*?)\s+(.*?);", content,re.DOTALL)
  rdata=[]
  data=[]
  for table in table_name:
    rdata.append(table[0])
    tdata=extract_row_data(table[2])
    rdata.append(tdata)
    data.append(rdata)
  print(data)
  return data

def extract_row_data(content):
  data=re.findall(r"`(\w+)`\s+(.*?)\s+(\w+\s\w+)?\,?",content,re.DOTALL)
  return data