from get_default import get_default
def get_key(more_info):
    more_info_lower=[item.lower() for item in more_info]
    data=dict()
    if 'key' in more_info_lower:
        idx=more_info_lower.index('key')
        data['key']=more_info[idx-1]
        more_info.pop(idx)
        more_info.pop(idx-1)
        more_info_lower.pop(idx)
        more_info_lower.pop(idx-1)
        if data['key'].lower()=='foreign':
            idx=more_info_lower.index('references')+1
            data['key']=f"FOREIGN\nREFERENCES {more_info[idx]}({more_info[idx+1]})"
            more_info.pop(idx+1)
            more_info.pop(idx)
            more_info.pop(idx-1)
            more_info_lower.pop(idx+1)
            more_info_lower.pop(idx)
            more_info_lower.pop(idx-1)
            if 'on' in more_info_lower:
                idx=more_info_lower.index('on')
                data[f"{more_info[idx]} {more_info[idx+1]}"]=more_info[idx+2:]
                for i in range(idx,len(more_info)):
                    # print(more_info)
                    # print(more_info_lower)
                    more_info.pop(idx)   
            data['key_assign']=more_info[0]             
        return data
    elif 'unique' in more_info_lower:
        more_info.pop(more_info_lower.index('unique'))
        data['key']='UNIQUE'
    else:
        data['key']='NOT PRIMARY KEY OR UNIQUE'
    if 'on' in more_info_lower:
        idx=more_info_lower.index('on')
        data[f"{more_info[idx]} {more_info[idx+1]}"]=more_info[idx+2:]
        for i in range(idx,len(more_info)):
            # print(more_info)
            # print(more_info_lower)
            more_info.pop(idx)       
    return data|get_default(more_info)



