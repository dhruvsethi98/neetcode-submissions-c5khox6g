class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        max_sum = window_sum
        window_cnt = 0

        if window_sum >= threshold * k:
                window_cnt += 1

        for i in range (1, len(arr) - k + 1):
            window_sum = window_sum - arr[i-1] + arr[i+k-1]
            if window_sum >= threshold * k:
                window_cnt += 1
        
        return window_cnt




        