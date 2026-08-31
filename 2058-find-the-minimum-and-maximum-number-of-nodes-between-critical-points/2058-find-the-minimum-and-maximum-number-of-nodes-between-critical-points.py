# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        asn = []
        current = head
        prev_val = current.val

        counter = 1
        distances = []
        while current is not None:
            if (current.next is not None) and (current.val < prev_val and current.val < current.next.val):
                distances.append(counter)
            
            if (current.next is not None) and (current.val > prev_val and current.val > current.next.val):
                distances.append(counter)

            prev_val = current.val
            current = current.next
            counter += 1

        if not distances or len(distances) < 2:
            return [-1, -1]

        if len(distances) == 2:
            return [abs(distances[1]-distances[0])] * 2

        min_distances = float('inf')
        for idx in range(1, len(distances)):
            current = distances[idx] - distances[idx-1]
            min_distances = min(min_distances, current)

        return [min_distances, max(distances)-min(distances)]