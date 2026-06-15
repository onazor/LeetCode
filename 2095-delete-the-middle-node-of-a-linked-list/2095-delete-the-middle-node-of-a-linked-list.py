class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # edge case
        if length == 1:
            return None
        
        target_index = length // 2
        
        current = head
        for _ in range(target_index - 1):
            current = current.next
        
        current.next = current.next.next
        
        return head
