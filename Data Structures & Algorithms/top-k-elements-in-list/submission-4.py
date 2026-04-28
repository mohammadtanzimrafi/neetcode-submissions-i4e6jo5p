class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = 0
        k_times = {}
        result_list = []
        for i in nums:
            if i not in k_times:
                k_times[i] = 1
            else:
                k_times[i] += 1

        # Sort dictionary keys by frequency in descending order
        sorted_keys = sorted(k_times, key=k_times.get, reverse=True)
        # Return the first k elements from the sorted list
        result_list = sorted_keys[:k]
        
        return result_list