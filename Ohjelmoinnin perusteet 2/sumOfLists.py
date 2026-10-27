def SumTheList(listOfNumLists):
    sumOfEveryNum = 0
    for numList in listOfNumLists:
        for num in numList:
            sumOfEveryNum += num
    return sumOfEveryNum


if __name__=="__main__":
    nums = [[3,1,4,1,5], [9,2,6,5,3], [5,8,9,7,9], [3,2,3,8,4], [6,2,6,4,3]]
    sumOFNums = SumTheList(nums)
    print(sumOFNums)
    