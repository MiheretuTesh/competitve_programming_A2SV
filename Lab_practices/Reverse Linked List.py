# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
    
        node = head.next
        if head == None:
            return head
        while head.next != None:
            head.next = prevNode
            prevNode = head
            head = node
            node = head.next
        head.next = prevNode
        return head