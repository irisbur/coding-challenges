import heapq
from typing import List


class Solution:
    # This solution runs in O(nlogk) since pushing and replacing to a
    # min heap of size k takes at most log(k).
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]

        # This solution runs in O(nlog(n)).

    def findKthLargestWithSort(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]
