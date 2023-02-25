# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1reverse = self.makeList(l1)
        l2reverse = self.makeList(l2)
        l1Num = 0
        l2Num = 0
        for i, k in enumerate(l1reverse):
            l1Num += int(k) * 10 ** i
        for i, k in enumerate(l2reverse):
            l2Num += int(k) * 10 ** i
        return self.makeLinkedList([int(x) for x in list(str(l1Num+l2Num))])

    def makeList(self, l):
        lreverse = []
        next = l
        while True:
            lreverse.append(next.val)
            if next.next == None:
                break
            next = next.next
        return lreverse
    
    def makeLinkedList(self, l):
        past = ListNode(l[0], None)
        for i, k in enumerate(l):
            if i != 0:
                past = ListNode(k, past)
        return past

s = Solution()
print(s.makeList(s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))))