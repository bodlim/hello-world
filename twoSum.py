class Solution:
    def twoSum(self, arr: [int], target: int):
        d = {}
        for i in range(len(arr)):
            a = target - arr[i]
            if a in d:
                return [d[a], i]
            d[arr[i]] = i

ab = Solution()
print(ab.twoSum([11, 7, 2, 13], 9))
print("good luck")
