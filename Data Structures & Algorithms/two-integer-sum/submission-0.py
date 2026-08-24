class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for i, item in enumerate(nums):
            diff = target - item
            if sum_map and diff in sum_map:
                return [sum_map[diff],i]
            else:
                sum_map[item] = i
        return []

        