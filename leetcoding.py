from ast import List
import itertools
import string


class Solution:
    # Contains Duplicate
    def containsDuplicate(self, nums) -> bool:
        if (len(nums)) == len(set(nums)):
            return False
        else:
            return True

    # Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            a = tuple(sorted(list(s)))
            b = tuple(sorted(list(t)))
            print(a, b)
            if a == b:
                return True

        return False

    # Two Sum
    def twoSum1(self, nums: list[int], target: int):
        i = 1
        p = 0
        while i < len(nums):
            p = nums[0]

            if p+nums[i] == target:
                if nums.count(p) > 1:
                    index = [i for i, j in enumerate(nums) if j == p]
                    return index
                return [nums.index(p), nums.index(nums[i])]
            else:
                p = nums[i]
                i += 1
                if p+nums[i] == target:
                    if nums.count(p) > 1:
                        index = [i for i, j in enumerate(nums) if j == p]
                        return index
                    return [nums.index(p), nums.index(nums[i])]

    def twoSum(self, nums: list[int], target: int):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

    # Missing Number

    def missingNumber(self, nums: list[int]) -> int:

        m = set(range(0, (len(nums)+1))) - set(nums)
        if len(m) != 0:
            m = m.pop()
            return m
        else:
            return m

    # Find Disappeared Numbers
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        m = set(range(1, (len(nums)+1))) - set(nums)
        return m

    # Single Number
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        if nums != set(nums):
            for item in nums:
                n = nums.count(item)
                if n == 1:
                    return item

    # Climbing Stairs
    def climbStairs(self, n: int, memo={}):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n > 1:
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
            return memo[n]

    # Maximum Subarray
    def maximumSubarray(self, nums: list[int]) -> int:
        min_sum = max_sum = 0
        for running_sum in itertools.accumulate(nums):
            min_sum = min(min_sum, running_sum)
            max_sum = max(max_sum, running_sum-min_sum)
        return max_sum

    # Find Duplicates
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dup = []
        if(len(nums) == 1):
            return dup

        for item in nums:
            if(nums.count(item) == 2):
                dup.append(item)

        return list(set(dup))

    # Maximum Profit
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        profit = 0
        while r < len(prices):
            profit = prices[r]-prices[l]
            max_profit = max(max_profit, profit)
            if(profit < l):
                l = r
                r += 1
            else:
                r += 1
        return max_profit

    # Binary Search
    def binarySearch(self, nums: list[int], target: int, memo={}) -> int:
        low = 0
        high = len(nums)-1
        mid = 0
        if(target in memo):
            return memo[target]
        while(low <= high):

            mid = (low + high)//2
            if(target > nums[mid]):
                low = mid+1
            elif(target < nums[mid]):
                high = mid-1
            else:
                memo[target] = mid
                return memo[target]
        return -1

    # Counting Bits
    def countBits(self, n: int) -> list[int]:
        x = [i for i in (range(0, n+1))]

        y = [(bin(i).replace("0b", "")).count('1') for i in x]
        return y

    # Greatest Letter
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        y = target
        # letters=sorted(letters)
        alpha = (string.ascii_lowercase)
        alpha = [char for char in alpha]
        i = alpha.index(target)
        for item in letters:
            if item == i:
                return i
            else:
                return letters


if __name__ == '__main__':
    test = Solution()
    nums = [7,1,5,3,6,4]
    letters = ["c", "a", "f", "j"]
    s = "aacc"
    t = "ccac"

    print(test.maxProfit(nums))
