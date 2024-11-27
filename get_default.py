def get_default(more_info):
    more_info_lower = [item.lower() for item in more_info]
    data=dict()
    if 'not' in more_info_lower and 'null' in more_info_lower:
        idx=more_info_lower.index('not')
        data['not_null']=True
        more_info.pop(more_info_lower.index('null'))
        more_info.pop(idx)
    elif 'default' in more_info_lower:
        idx=more_info_lower.index('default')
        data['default']=more_info[idx+1]
        more_info.pop(idx+1)
        more_info.pop(idx)
    elif 'null' in more_info_lower:
        idx=more_info_lower.index('null')
        data['not_null']=False
        more_info.pop(idx)
    else:
        data['not_null']=False
    return data