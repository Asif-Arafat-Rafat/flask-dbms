import re

def extract_table_data(content):
  info=[]
  table_info = re.findall(r"CREATE TABLE `(\w+)` \(?(.*?)\s+(.*?);", content,re.DOTALL)
  for t in range(len(table_info)):
    td={}
    table_name=re.findall(r"(.*)\s*,?",table_info[t][0])
    table_column=re.findall(r"(.*)\s*,?",table_info[t][2])
    col_data=re.findall(r"(\w+)(?:\((\d+)\))?",table_column[0])
    
    formater=[(name,size) if size else name for name,size in col_data]
    print(f"Column Data:{formater}")
    td['Table Name']=table_name[0]
    td['Table Columns']=table_column[0]
    info.append(td)
  print(f"Table Info:{info}\n")
#   for t in range(len(table_column)):
    # column_data=re.findall(r"(\w+)",table_column[t].strip(" "))
    # print(f"Column Data:{column_data}")
#   not_what=re.findall(r"NOT\s*(\w+)",table_column[0],re.DOTALL)
#   print(f"Not:{not_what}")
#   key=re.findall(r"(\w+)\*KEY",table_column[0])
#   fpk(content)
  
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
  
# insertData('admin',"""INSERT INTO `admin` (`admin_id`, `username`, `password`) VALUES
# (1, 'rafat', '@sif');""")

def fpk(content):
  pk=re.findall(r"TABLE `(\w+)`\s*.*?\s*(\w+)\s*KEY\s*\(`(\w+)",content,re.DOTALL)
  for i in range(len(pk)):
    if(pk[i][1]=='FOREIGN'):
      print(f"FKEY:{pk[i][2]}") 
      fk=re.findall(rf"FOREIGN\s+KEY\s+\(`{pk[i][2]}`\)\s+REFERENCES\s+`(\w+)` \(`(\w+)`\)",content,re.DOTALL)
      print(f"PK:{fk}")
      
