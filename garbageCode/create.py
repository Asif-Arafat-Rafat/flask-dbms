# printMe(table_information['columns'])
# printMe(table_column)
# for i in info:
#   # print(f"Table Name:{i['name']}")
#   # print(f"Table Columns:{i['columns']}")
#   for j in i['columns']:
#     print(j)
#     print("::::")
#   print("-------------------------------------------------------------------------------------------")
# for t in range(len(table_info)):
#   td={}
#   table_name=re.findall(r"(.*)\s*,?",table_info[t][0])
#   print(f"Start of Table{table_name[t][0]}\n")
#   table_column=re.findall(r"(.*)\s*,?",table_info[t][1])
#   for tab in table_column:
#     print(f"Table col:{tab.strip(",")}")
#   # print(f"Table Array:{table_column}\n")
#   col_data=re.findall(r"(\w+)(?:\((\d+)\))?",table_column[0])
#   # print("\nAFTER FILTER")
#   dt=[]
#   for tab in table_column:
#     print(f"Table col:{tab.strip(",")}")
#     dt.append(col(tab.strip(",")))
#   print(f"END of Table {table_name[t][0]}\n")
#   return dt
#       print("\n\n")
# col_name=re.findall(r"`([^`]+)`|([^\s`]+)",tab.strip(","))
# print(f"Column Name:{col_name}")
# not_null=re.search(r"NOT NULL",tab,re.IGNORECASE)
# defa=re.search(r"DEFAULT\s*(\w+)",tab,re.IGNORECASE)
# typ=re.search(rf"{col_name[0][0]}`?\s*(\w+)\s*?",tab).group()
# print(f"Type:{typ}")
# if(re.search(r"INT",typ,re.IGNORECASE)):
#   print(f"DataType: integer")
#   if(re.search(r'INT\((\d+)\)',tab,re.IGNORECASE)):
#     print(re.search(r'INT\((\d+)\)',tab,re.IGNORECASE).group(1))
# elif((re.search(r"VARCHAR",typ,re.IGNORECASE))):
#   print(f"DataType: varchar of size:{re.search(r"VARCHAR\((\d+)\)",tab,re.IGNORECASE).group(1)}")
# elif((re.search(r"TEXT",typ,re.IGNORECASE))):
#   print(f"DataType: text")
# elif((re.search(r"DATE",typ,re.IGNORECASE))):
#   print(f"DataType: date")
# elif((re.search(r"TIME",typ,re.IGNORECASE))):
#   print(f"DataType: time")
# elif((re.search(r"DATETIME",typ,re.IGNORECASE))):
#   print(f"DataType: datetime")
# elif((re.search(r"TIMESTAMP",typ,re.IGNORECASE))):
#   print(f"DataType: timestamp")
# elif((re.search(r"FLOAT",typ,re.IGNORECASE))):
#   print(f"DataType: float")
# print('\n')
#       if(not_null):
#         print(f"Default:NOT NULL")
#       elif(defa):
#         print(f"Default:{defa.group(1)}")
#       else:
#         print(f"Default:NULL")
#     formater=[(name,size) if size else name for name,size in col_data]
#     # print(f"Column Data:{formater}")
#     td['Table Name']=table_name[0]
#     td['Table Columns']=table_column[0]
#     info.append(td)
#   # print(f"Table Info:{info}\n")
# #   for t in range(len(table_column)):
#     # column_data=re.findall(r"(\w+)",table_column[t].strip(" "))
#     # print(f"Column Data:{column_data}")
# #   not_what=re.findall(r"NOT\s*(\w+)",table_column[0],re.DOTALL)
# #   print(f"Not:{not_what}")
# #   key=re.findall(r"(\w+)\*KEY",table_column[0])
# #   fpk(content)
# rdata=[]
# tableName=[]
# data=[]
# # for table in table_name:
# #   tableName.append(table[0])
# #   tdata=extract_row_data(table[2])
# #   rdata.append(tdata)
# data.append(tableName)
# data.append(rdata)
#   # return data
# def extract_row_data(content):
#   data=re.findall(r"`(\w+)`\s+(.*?)\s+(\w+\s\w+)?\,?",content,re.DOTALL)
#   return data
# def insertData(tab,content):
#   column=re.findall(rf'INSERT INTO\s*`{tab}`\s*\((.*?)\) VALUES\s*\(.*?\)\s*',content,re.DOTALL)
#   values=re.findall(rf'INSERT INTO\s*`{tab}`\s*\(.*?\) VALUES\s*\((.*?)\)\s*',content,re.DOTALL)
#   print(f"Column:{column}")
#   print(f"Values:{values}")
# # insertData('admin',"""INSERT INTO `admin` (`admin_id`, `username`, `password`) VALUES
# # (1, 'rafat', '@sif');""")
# def fpk(content):
#   pk=re.findall(r"TABLE `(\w+)`\s*.*?\s*(\w+)\s*KEY\s*\(`(\w+)",content,re.DOTALL)
#   for i in range(len(pk)):
#     if(pk[i][1]=='FOREIGN'):
#       print(f"FKEY:{pk[i][2]}") 
#       fk=re.findall(rf"FOREIGN\s+KEY\s+\(`{pk[i][2]}`\)\s+REFERENCES\s+`(\w+)` \(`(\w+)`\)",content,re.DOTALL)
#       print(f"PK:{fk}")
