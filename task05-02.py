def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else :
        return staircase(n-1) +  staircase(n-2)

print(staircase(5))
