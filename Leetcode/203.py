class Solution(object):
    def removeElements(self, head, val):
        #If the head data is target to delete
        while head is not None and head.val == val:
            head = head.next
        current = head
        while current is not None:
            if current.next is not None and current.next.val == val:
                #Remove current.next
                current.next = current.next.next
            else:
                current = current.next
        return head
