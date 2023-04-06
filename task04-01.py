s = 'Here are UPPERCASE and lowercase chars.'


d = {}

for i in range(0,len(s)):
    if s[i] in d:
        d[s[i]].append(i+1)
    else:
        d[s[i]] = [i+1]
    

print(d)
