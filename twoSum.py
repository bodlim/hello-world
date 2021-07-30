class Solution:
    def twoSum(self, arr: [int], target: int):
        d = {}
        for i in range(len(arr)):
            a = target - arr[i]
            if a in d:
                return [d[a], i]
            d[arr[i]] = i

ab = Solution()
final = ab.twoSum([11, 7, 2, 13], 9)
print(final)
print("well done!")
print("Perfect!")
print("hmm, not perfect yet!")
