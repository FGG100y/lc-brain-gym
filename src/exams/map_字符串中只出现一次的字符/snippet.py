import sys

def get_first_only(s):                                                                  
    seen_l = {}                                                                         
    for e in s:                                                                         
        cnt = 1                                                                         
        if e in seen_l.keys():                                                          
            new_cnt = seen_l[e] + 1                                                     
            seen_l.update({e: new_cnt})                                                 
        else:                                                                           
            seen_l.update({e: cnt})                                                     
                                                                                        
    res = [e for e in s if seen_l.get(e, -1) < 2]                                      
    if len(res) == 0:                                                                   
        return -1                                                                       
    else:                                                                               
        return res[0]

for line in sys.stdin:
    s = line.strip()
    print(get_first_only(s))