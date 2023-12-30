from itertools import combinations


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        combs = combinations(nums, 2)
        index = []
        for num in combs:
            if sum(num) == target:
                for n in num:
                    index.append(nums.index(n))
                    nums[int(nums.index(n))] = 'a'
                return index
            else:
                print('The solution is not possible')


sol = Solution()
print(sol.twoSum([3,3], 6))
