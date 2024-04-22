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
    
# print(checkPrime(2))



def solve(A):
        sum = 0

        for i in range(1,int(A**0.5)+1):
            print(sum,A,i)
            print("---------")
            if A%i ==0:
                if i==1:
                    sum+=1
                elif i == A/i:
                    sum +=i
                else:
                    sum+= i +A/i    
        print(sum)
        if int(sum) == A:
            return 1
        else:
            return 0   
        

# print(solve(1))