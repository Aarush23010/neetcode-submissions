class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        hashmap={}
        if not nums:
            return 0
        for i,num in enumerate(nums):
            if num-1 not in num_set:
                hashmap[num]=1
                next_num = num+1
                while next_num in num_set:
                    hashmap[num]+=1
                    next_num += 1
        key = max(hashmap.values())

        return key
