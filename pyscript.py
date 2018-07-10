import random
def randomIntegers(start, finish):
    #returns random integers from start to finish
    ans = []
    for i in range(start, finish):
        ans.append(random.randint(start, finish))
    return ans
    
