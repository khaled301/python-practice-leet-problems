class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if left == right and nums[left] == target:
            return left

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
            if left == right and nums[left] == target:
                return left

        return -1