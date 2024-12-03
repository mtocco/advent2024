# https://adventofcode.com/2024/day/2

from datetime import datetime

def determineSafe(nums):
    sortedNums = nums.copy()
    if nums[0] < nums[1]:
        sortedNums.sort()
    else:
        sortedNums.sort(reverse=True)
        
    if sortedNums != nums:
        return False
    for i in range(len(nums)-1):
        if int(nums[i+1]) == int(nums[i]):
            return False
        if abs(int(nums[i+1]) - int(nums[i])) > 3:
            return False
    return True

    
def main():
    start_time = datetime.now()
    safeCount = 0
    rejects =[]
    with open("advent2024Day2Input.txt", "r") as file:
        for line in file:
            splitLine = [int(num) for num in line.split()]
            if determineSafe(splitLine):
                safeCount+=1
            else:
                rejects.append(splitLine)
    
    print(safeCount) # Day2Pt1
    
    for i in rejects:
        for j in range(len(i)):
            testPop = i.copy()
            testPop.pop(j)
            if determineSafe(testPop):         
                safeCount+=1
                break
    print(safeCount) # Day2Pt2

    end_time = datetime.now()
    duration = end_time - start_time
    print("Duration:", duration)
    
main()
