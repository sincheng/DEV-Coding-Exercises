class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while (current):
            if (current.next is not None and current.val==current.next.val):
                current.next = current.next.next
            else:
                current = current.next
        return head
                
