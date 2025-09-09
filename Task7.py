from typing import List

def combine(list1: List[int], list2: List[int]) -> List[int]:
    result = []
    length = max(len(list1), len(list2))    #get the max length of the final list
    
    for i in range(length):
        if i < len(list1):                  #check if index not out of bound
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
    
    return result

print(combine([11,22,33,45], [1,2,3]))

