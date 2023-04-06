def add1(n):
    return [i+1 for i in n ]
 
def isPrime(n):
    prime_list = []
    for i in n:
        check = True
        if i<2:
            break
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                check = False
                break
        prime_list.append(check)
    return(prime_list)



def f(L, F):
  return F(L)

L = [1,2,3,4,5,6]
F = add1
print(f(L, F)) # [2,3,4,5,6,7]

L = [2,3,4,5,6,7] 
F = isPrime
print(f(L, F)) # [True,True,False,True,False,True]
