def concat(*str,reversed = False):
    ret_str=''
    
    if reversed == True:
        for x in str[::-1]:
            ret_str += x
    else:
        for s in str:
            ret_str += s
    
    return ret_str

print(concat('1','2','3','4'))        
print(concat('1','2','3','4',reversed = True))
