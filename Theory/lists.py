#Lists in python are similar to array 

A= [10,20,30,4,5,6,7,8,4]

print(type(A))
print(len(A)) #gives the length of list A


# print(A[7])

#Insert at index
A.insert(1,1.5)


A.extend([9,10,11,12])

#Here + is same as extend
A= A+[13,14,15]


#Add the data at the last index of list
A.append([100,200])

#it will remove the first occurance of value passed
A.remove(1.5)

#Gives the count of occurances of value
print(A.count(3))

#Deletes all the values from the list
# A.clear()


#Gives the index of first occurance of the value passed
print(A.index(4))


#in operator - check if value passed exists in list or not
print(1 in A)


# print(A)

#slicing -list[start:end] -slices from start to end-1
print(A[1:5])

#slicing -list[start:end:increment] -slices from start to end-1 with jump of imcrement
print(A[1:5:2])


#NEGATIVE list slicing
print(A[5:0:-1])

print(A[-2:-5:-1])

# for i in A:
#     print(i)



