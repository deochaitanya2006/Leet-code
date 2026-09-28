class Solution:
    def twoSum(self, nums, target):
        numbers = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required in numbers:
                return [numbers[required], i]
            numbers[nums[i]] = i