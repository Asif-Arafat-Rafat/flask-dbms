from get_default import get_default
def get_key(more_info):
    more_info_lower=[item.lower() for item in more_info]
    data=dict()
    if 'key' in more_info_lower:
        idx=more_info_lower.index('key')
        data['key']=more_info[idx-1]
        more_info.pop(idx)
        more_info.pop(idx-1)
    elif 'unique' in more_info_lower:
        more_info.pop(more_info_lower.index('unique'))
        data['key']='UNIQUE'
    else:
        data['key']='NOT PRIMARY KEY OR UNIQUE'
    return data|get_default(more_info)
