def compare_version (version1,version2):
    
    p=version1
    q=version2
    emp_list_v1=[]
    emp_list_v2=[]
    mapping=[]
    new_like_orig=[]
    final=[]
    
    emp_list_v1=p.split('.')
    emp_list_v2=q.split('.')
    
    mapped=list(map(int,emp_list_v1))
    mapping.append(mapped)
    mapped=list(map(int,emp_list_v2))
    mapping.append(mapped)
    
    
    mapping.sort()
    

    for i in mapping:
        mp=list(map(str,i))
        new_like_orig.append(mp)

    
    for j in new_like_orig:
        h='.'.join(j)
        final.append(h)

        
    if p != final[0] and p!=q:
        return 1        #first num is greater then RETURN 1
        
    elif p!=q and p==final[0]:
        return -1       #Second num is greater then RETURN -1
        
    else:
        return 0
        
