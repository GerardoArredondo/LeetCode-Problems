class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tamaño = len(nums)
        for i in range(tamaño-1):
            for j in range(i+1, tamaño):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]
        return
        