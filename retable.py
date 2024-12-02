import re

def extract_table_data(content):
  table_info = re.findall(r"CREATE TABLE `(\w+)` \(?(.*?)\s+(.*?);", content,re.DOTALL)
  
  table_name=table_info[0]
  table_column=re.findall(r"(.*)\s*,?",table_info[0][2])
  print(f"Table Name:{table_column}")
  column_data=re.findall(r"(\w+)",table_column[0].strip(" "))
  not_what=re.findall(r"NOT\s*(\w+)",table_column[0],re.DOTALL)
  key=re.findall(r"(\w+)\*KEY",table_column[0])
  print(f"Not:{not_what}")
  print(f"Table Name:{column_data}")
  
  fpk(content)
  
  rdata=[]
  tableName=[]
  data=[]
  # for table in table_name:
  #   tableName.append(table[0])
  #   tdata=extract_row_data(table[2])
  #   rdata.append(tdata)
  data.append(tableName)
  data.append(rdata)
  return data

def extract_row_data(content):
  data=re.findall(r"`(\w+)`\s+(.*?)\s+(\w+\s\w+)?\,?",content,re.DOTALL)
  return data

def insertData(tab,content):
  column=re.findall(rf'INSERT INTO\s*`{tab}`\s*\((.*?)\) VALUES\s*\(.*?\)\s*',content,re.DOTALL)
  values=re.findall(rf'INSERT INTO\s*`{tab}`\s*\(.*?\) VALUES\s*\((.*?)\)\s*',content,re.DOTALL)
  print(f"Column:{column}")
  print(f"Values:{values}")
  
insertData('admin',"""INSERT INTO `admin` (`admin_id`, `username`, `password`) VALUES
(1, 'rafat', '@sif');""")

def fpk(content):
  pk=re.findall(r"TABLE `(\w+)`\s*.*?\s*(\w+)\s*KEY\s*\(`(\w+)",content,re.DOTALL)
  for i in range(len(pk)):
    if(pk[i][1]=='FOREIGN'):
      print(f"FKEY:{pk[i][2]}") 
      fk=re.findall(rf"FOREIGN\s+KEY\s+\(`{pk[i][2]}`\)\s+REFERENCES\s+`(\w+)` \(`(\w+)`\)",content,re.DOTALL)
      print(f"PK:{fk}")
      
