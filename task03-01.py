a, b = input(), input() # 11, 20
number_1, number_2 = 0, 0


for i in range(int(a),int(b)+1):
    number = str(i)
    divid_fail = False
    for j in range(0,len(number)):
        if int(number[j])==0 or i % int(number[j]) != 0:
            divid_fail = True
            break
    if divid_fail == False:

        if number_1 == 0:
            number_1 = i
        elif number_2 == 0:
            number_2, temp = i, number_1
        elif number_2 - number_1 < i - temp:
            number_1, number_2 = temp, i

        temp = i

            
d = (number_1, number_2)


print(d) # (12, 15)
