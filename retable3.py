import re
from removecmt import rmv_cmt
from helper import garbagefilter
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
    col_data=re.findall(r"(\w+)(?:\((\d+)\))?",table_column[0])
    print("\nAFTER FILTER")
    for tab in table_column:
      print(f"Table col:{tab.strip(",")}")
      print("\n\n")
      col_name=re.findall(r"`([^`]+)`|([^\s`]+)",tab.strip(","))
      print(f"Column Name:{col_name}")
      not_null=re.search(r"NOT NULL",tab,re.IGNORECASE)
      defa=re.search(r"DEFAULT\s*(\w+)",tab,re.IGNORECASE)
garbagefilter()