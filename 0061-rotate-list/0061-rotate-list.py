class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next

        k = k % length
        if k == 0:
            return head
        
        counter = 0
        curr1 = head

        removed_dummy = ListNode()
        removed_tail = removed_dummy 

        while counter < length - k:
            new_node = ListNode(curr1.val)
            removed_tail.next = new_node 
            removed_tail = removed_tail.next 
            
            curr1 = curr1.next
            counter += 1
            
        new_head = curr1
            
        while curr1.next is not None:
            curr1 = curr1.next
            
        curr1.next = removed_dummy.next
        
        return new_head