"""
2816. Double a Number Represented as a Linked List
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
Return the head of the linked list after doubling it.
Example 1:
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378

Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(h):
            prev=None
            curr=h
            next=h.next
            while next:
                curr.next=prev
                prev=curr
                curr=next
                next=next.next
            curr.next=prev
            return curr
        newHead=reverse(head)  
        temp=newHead
        carry=0
        while temp:
            temp.val=temp.val*2+carry
            carry=temp.val//10
            temp.val%=10
            temp=temp.next
        if carry:
            head.next=ListNode(1)
        return reverse(newHead)

