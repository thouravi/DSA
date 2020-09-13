A = [-2, 1, 2, 4, 7, 11]
target = 13

'''
Brute Force Technique
Time Complexity = O(n^2) - Looping Twice through Array A
Space Complexity = O(1) - Not using any Data Structure
'''

def twoSum(A, target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True 
    return False


'''
Hash Table Technique
Time Complexity = O(n) - Looping once through Array A
Space Complexity = O(n) - Storing Dictionary Item Once
'''

def twoSum(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True 
        else:
            ht[target - A[i]] = A[i]
    return False


'''
Time Complexity: O(n) - Looping once through Array A
Space Complexity: O(1) - No Data Structure Used
'''

def twoSum(A, target):
    i = 0
    j = len(A) - 1

    while i <=j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True 
        elif A[i] + A[j] < target:
            i+=1
        else:
            j-=1
    return False
