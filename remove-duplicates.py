# Link to Leetcode Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

# [:] = makes a shallow copy of the array, hence allowing you to modify your copy without 
# damaging the original. The reason this also works for strings is that in Python, 
# Strings are arrays of bytes representing Unicode characters.