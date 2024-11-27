import re
from removecmt import rmv_cmt
def extract_table_data(content):
  content=rmv_cmt(content)
  info=[]
  table_info = re.findall(r"CREATE TABLE `?(\w+)`? \((.*?);", content,re.DOTALL)
  for table in table_info:
    for t in table:
      print(f"Table:{t}\n")
  for t in range(len(table_info)):
    td={}
    table_name=re.findall(r"(.*)\s*,?",table_info[t][0])
    table_column=re.findall(r"(.*)\s*,?",table_info[t][1])
    print("\n\n\nBEFORE FILTER")
    for tab in table_column:
      print(f"Table col:{tab.strip(",")}")
    table_column=list(filter(None,table_column))
    table_column=list(filter(lambda x: not x.startswith(")"),table_column))
    # print(f"Table Array:{table_column}\n")
    col_data=re.findall(r"(\w+)(?:\((\d+)\))?",table_column[0])
    print("\nAFTER FILTER")
    for tab in table_column:
      print(f"Table col:{tab.strip(",")}")
      print("\n\n")
      col_name=re.findall(r"`([^`]+)`|([^\s`]+)",tab.strip(","))
      print(f"Column Name:{col_name}")
      not_null=re.search(r"NOT NULL",tab,re.IGNORECASE)
      defa=re.search(r"DEFAULT\s*(\w+)",tab,re.IGNORECASE)
      typ=re.search(rf"{col_name[0][0]}`?\s*(\w+)\s*?",tab).group()
      print(f"Type:{typ}")
      if(re.search(r"INT",typ,re.IGNORECASE)):
        print(f"DataType: integer")
        if(re.search(r'INT\((\d+)\)',tab,re.IGNORECASE)):
          print(re.search(r'INT\((\d+)\)',tab,re.IGNORECASE).group(1))

      elif((re.search(r"VARCHAR",typ,re.IGNORECASE))):
        print(f"DataType: varchar of size:{re.search(r"VARCHAR\((\d+)\)",tab,re.IGNORECASE).group(1)}")
      elif((re.search(r"TEXT",typ,re.IGNORECASE))):
        print(f"DataType: text")
      elif((re.search(r"DATE",typ,re.IGNORECASE))):
        print(f"DataType: date")
      elif((re.search(r"TIME",typ,re.IGNORECASE))):
        print(f"DataType: time")
      elif((re.search(r"DATETIME",typ,re.IGNORECASE))):
        print(f"DataType: datetime")
      elif((re.search(r"TIMESTAMP",typ,re.IGNORECASE))):
        print(f"DataType: timestamp")
      elif((re.search(r"FLOAT",typ,re.IGNORECASE))):
        print(f"DataType: float")
      print('\n')
      if(not_null):
        print(f"Default:NOT NULL")
      elif(defa):
        print(f"Default:{defa.group(1)}")
      else:
        print(f"Default:NULL")
