class Solution:
    List = None
    def moveZeroes(self, nums: List[int]) -> None:
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_index], nums[i] = nums[i], nums[write_index]
                write_index += 1
