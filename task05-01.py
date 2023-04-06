def create_letter(s1):
    if len(s1)==1:
        return [s1]
    result = []
    for i,j in enumerate(s1):
        rem = s1[:i] + s1[i+1:]
        sub = create_letter(rem)
        for k in sub :
            result.append(j + k)   
    return result
    
'''
Your Code
'''

s = input() # AB

d = create_letter(s)


print(d)
