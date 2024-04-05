# print("this is a statement", end="hksdAHKDJH")
# print("2nd statment")


# i=1 

# while i<=1000:
#     print(i,end=" ")
#     i+=1

# i=1

# while i<10:
#     if i%2 !=0:
#         print(i)

#     i+=1    


# # range(5) means 0 to 4
# print(*range(5))

# #range(2,5,1) - range(start,end,increment)
# print(*range(2,15,2))

# #range(2,5) - range(start,end)
# print(*range(2,5))



# #for loops
# for i in range(20,50):
#     print(i)


# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     N = int(input())

#     for i in range(1,N+1):
#         if i%2 ==0:
#             print(i, end=" ")
#     return 0

# if __name__ == '__main__':
#     main()



# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output

#     T = int(input())
#     i=1
#     while i<=T:
#         A= int(input())
#         j=1
#         count =0
#         if A==1:
#             count= 0;
#         else :    
#             while A !=0:
#                 A= A//10
#                 count+=1
#         print(count)    
#         i+= 1    
#     return 0

# if __name__ == '__main__':
#     main()



#PASS - It is used so that there is no error in that block of code
x=15
if x==5:
    pass