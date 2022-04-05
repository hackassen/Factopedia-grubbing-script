def SmartStringCatitalise(string:str) -> str:
    arr_s=string.split(" ")
    out_arr_s=list()
    for s in arr_s:
        uppers_cnt=0
        for l in s:
            if l.isupper(): uppers_cnt+=1
            
        if uppers_cnt<2:
            out_arr_s.append(s.lower())
        else:
            out_arr_s.append(s)
            
    out_str=" ".join(out_arr_s)
    out_str=out_str.replace('[\&]', 'and')
    out_str=out_str.replace('[\+]', ' plus ')
    
    return out_str[0].upper()+out_str[1:]


#res=SmartStringCatitalise("Field HDMI stuff Field (IT like)")
#print(res)
