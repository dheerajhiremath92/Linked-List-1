class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        first=head
        if (not first) or (not first.next): return first
        first.next, curr, prev = None, first.next, first
        
        while curr.next:
            curr.next, curr, prev = prev, curr.next, curr
        curr.next=prev
        return curr