import re
def rmv_cmt(content):
  content=re.sub(r"/\*.*?\*/","",content,flags=re.DOTALL)
  content=re.sub(r"--.*?\n","",content)
  return content