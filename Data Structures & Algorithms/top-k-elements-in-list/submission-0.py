class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for key in nums:
            freq[key] = freq.get(key, 0) + 1
        
        sort_list = sorted(freq.items(), key = lambda x:x[1])[-k:]
        result = []

        for i in sort_list:
            result.append(i[0])

        return result