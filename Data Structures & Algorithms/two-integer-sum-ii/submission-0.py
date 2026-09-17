class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        q = len(numbers) - 1
        while i < q:
            current_sum = numbers[i] + numbers[q]
            if current_sum == target:
                return [i + 1, q + 1]
            if current_sum < target:
                i += 1
            else: 
                q -= 1

