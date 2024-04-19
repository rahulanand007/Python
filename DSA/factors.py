import math
#Brute Force
def noOfFactors(N):
    count=0
    for i in range(1,N+1):
        if N%i == 0:
            count+=1

    return count        


# print(noOfFactors(16))


def noOfFactors1(N):
    count=0
    for i in range(1,int(math.sqrt(N)) + 1):
        if N%i == 0:
            if i==N/i:
                count+=1
            else:
                count+=2

    return count   

# print(noOfFactors1(16))


def checkPrime(N):
    
    if noOfFactors1(N) == 2:
        return True
    else:
        return False
    
print(checkPrime(2))