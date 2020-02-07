'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
import time
def isPandigital(n):
    #n is a number
    result = False
    my_list = list(str(n))
    for i in range(0, len(my_list)): 
        my_list[i] = int(my_list[i]) 
    my_set = set(my_list)
    list_length = len(my_list)
    set_length = len(my_set)
    if list_length == set_length and set(range(list_length)) == my_set:
        result = True
    return result

def CreatingPermutations(n):
    result_perms = [[]]
    for i in n:
        new_perms = []
        for perm in result_perms:
            for j in range(len(perm)+1):
                new_perms.append(perm[:j]+[i]+perm[j:])
                result_perms = new_perms
    return result_perms

def creatingNumbers(my_list):
    #my_list is list which will create a list of lists from Creating Permutations
    new_list = CreatingPermutations(my_list)
    final_list = []
    for eachList in new_list:
        each_str = ''
        if eachList[0] != 0:
            for eachNumber in eachList:
                each_str += str(eachNumber)
            final_list.append(int(each_str))
    return final_list

def SubStringDivisibility(my_list):
    start_time = time.time()
    final_list = creatingNumbers(my_list)
    final_number = 0
    for eachNumber in final_list:
        new_list = []
        testing_list = [2,3,5,7,11,13,17]
        result = True
        for i in range(1,8):
            new_list.append(int(str(eachNumber)[i:i+3]))
        for i, j in zip(new_list, testing_list):
            if i % j != 0:
                result = False
                break
        if result == True:
            final_number += eachNumber
    return final_number, time.time() - start_time

final = SubStringDivisibility([0,1,2,3,4,5,6,7,8,9])
print(final)