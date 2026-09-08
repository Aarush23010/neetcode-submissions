class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        half = (len(nums))/2
        for key, value in hashmap.items():
            if value>half:
                major = key
        return major
    