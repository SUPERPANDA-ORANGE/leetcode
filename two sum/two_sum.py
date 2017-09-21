class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        list1 = []
        for index in range(len(numbers)-1):
            i = 1
            while i < len(numbers) - index:
                if numbers[index] + numbers[index + i] == target:
                    list1.append(index + 1)
                    list1.append(index + i + 1)
                    return list1
                else:
                    i+=1