def dict_freq(str1):
    '''str1 is a string
       Ouput -> A dictionary is expected to be returned'''

    # YOUR CODE GOES HERE
    l1 = list(str1)
    dictionary = {}

    for i in set(l1):
        if i not in dictionary:
            dictionary[i] = l1.count(i)

    return dictionary


print(dict_freq('ABC'))