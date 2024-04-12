#Tuples are simir to lists but are used inside () insted of []
#Data inside a Tuple are not updatable.

test = (1,2,4,5,6,7,8,9)

print(type(test))


#To create a tuple of only a single element- put a trailing comma(,)
t = (5,)


#Empty tuple
t= tuple()


t1 =1,2,3,4
print(type(t1)) #By default it is a tuple



#UNPACKING and PACKING
a,b,c = 1,2,3

print(a,b,c)



#----------------------------------------------------------------------------------

#SETS- It is unordered
#    - Contains only unique values
#    - Cannot put mutable data inside sets

s= {1,9,85,3,2}


#Create empty set
s1=set()


#add inside set
s.add(60)


#remove from set
s.remove(60)

print(s)

#check if value exists in set
print(85 in s)

#INTERSECTION
A ={1,2,3,4,5}
B ={4,5,6,7}

C= A.intersection(B)
D = A&B                #Same as above

print(C,D)


#UNION
E = A.union(B)
F = A | B              #Same as above

print(E,F)


#DIFFERENCE
G = A-B
print(G)


#Symmetric DIFFERENCE
I = A^B
print(I)

u= set([1,2,3,4,5,6,7,1,2,3])

print(len(u))

