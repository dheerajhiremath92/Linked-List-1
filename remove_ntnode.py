class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast=slow=head
        for i in range(n):
            fast=fast.next     
        if not fast :         
            return head.next
        while fast.next:           
            slow=slow.next
            fast=fast.next       
        slow.next=slow.next.next
        return head
            