'''
Test cases are failing
'''
def reduce_string(s):
    ss = list(s)
    while True:
        check = False
        i = 0
        while i < len(ss) - 1:
            if ord(ss[i]) + 1 == ord(ss[i + 1]):
                ss.pop(i)
                ss.pop(i)  
                check = True
                i = max(0, i-1)  
            else:
                i += 1
        
        if not check:
            break
            
    return len(ss)

s = "ABFCACDB"
s = "ACBBD"
result = reduce_string(s)
print(result)  
