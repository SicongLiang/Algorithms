# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 哨兵机制
        p = ListNode(0)
        curr = p

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1 is None:
            while l2 is not None:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        if l2 is None:
            while l1 is not None:
                curr.next = l1
                l1 = l1.next
                curr = curr.next

        return p.next

        # 1. 迭代法 时间复杂度：O(n+m)，空间复杂度：0(1)
        # 这里设置了一个哨兵指针，防止最后找不到应该返回的头节点
        ###
        if l1 is None: # 当有空链表时，直接无需merge，直接返回另外一个
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2) # 判断哪个节点的值更小，递归的决定添加到结果的节点
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        # 2. 递归法 时间复杂度：O(n+m)，空间复杂度:O(n+m)
        # Space: 递归调用 mergeTwoLists 函数时需要消耗栈空间，栈空间的大小取决于递归调用的深度。
        # 结束递归调用时 mergeTwoLists 函数最多调用 n+m 次
        # 实现递归的两点：
        # (1) 递归函数必须要有终止条件，否则会出错；
        # (2) 递归函数先不断调用自身，直到遇到终止条件后进行回溯，最终返回答案。
        # 本地解法：
        # (1) 终止条件：当两个链表都为空时，表示我们对链表已合并完成
        # (2) 如何递归：我们判断 l1 和 l2 头结点哪个更小，然后较小结点的next指针指向
        # 其余结点的合并结果！！！(递归调用)
        
