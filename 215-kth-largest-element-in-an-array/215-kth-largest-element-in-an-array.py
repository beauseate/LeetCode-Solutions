class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        
        for n in nums[k:]:
            heapq.heappush(pq, n)
            heapq.heappop(pq)
        return pq[0]