# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        count = 0
        res = []
        curr = head
        while curr:
            curr = curr.next
            count += 1
            
        part = count // k
        leftover = count % k
        curr = head
        prev = None
        
        for _ in range(k):
            res.append(curr)
            for _ in range(part):
                if curr:
                    prev = curr
                    curr = curr.next
            if leftover and curr:
                prev = curr
                curr = curr.next
                leftover -= 1
            if prev:
                prev.next = None
        return res