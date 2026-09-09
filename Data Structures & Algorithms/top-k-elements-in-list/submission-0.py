class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}
        output = []
        for i, num in enumerate(nums):
            if num not in frq:
                frq[num]=1
            else:
                frq[num]+=1
        for j in range(0,k):
            key = sorted(frq, key=frq.get, reverse = True)[j]
            output.append(key)
        return output

