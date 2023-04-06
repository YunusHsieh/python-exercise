s = input() # This company is not poor at all. 
end = ""

d_list = []
if s[-1] in [".", "!", "?"]:
    end = s[-1]
    s = s[:-1]

words = s.split(" ")
print(words)

check = 0

for i, word in enumerate(words[:-1]):
    if check != 0:
        if word == "at" and words[i+1] == "all":
            d_list = words[:check] + ["good"] + words[i+2:]
            break
            
    if word == "not":
        check = i
        #print(check)
        
if d_list == []:
    d = s + end
else:
    d = " ".join(d_list) + end

print(d) # This company is good.
