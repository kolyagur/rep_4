def inspect(concat):
    def ret_arguments(*args, **kwargs):
        print('Args :',args)
        print('Kwargs :',kwargs)
        print('Retvalue',concat('1','2','3','4',Reversed=True))
        print(concat('1','2','3','4',Reversed=True))
        concat(*args, **kwargs)
    return ret_arguments

@inspect
def concat(*str,Reversed = False):
    ret_str=''
    
    if reversed == True:
        for x in str[::-1]:
            ret_str += x
    else:
        for s in str:
            ret_str += s
    return ret_str
    
concat('1','2','3','4',Reversed=True)