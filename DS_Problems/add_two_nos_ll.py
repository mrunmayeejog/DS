class sll_node:
    def __init__(self, value):
        self.data = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def insert_athead(self, value):
        new_node = sll_node(value)
        if not self.head:
            self.head = new_node
            self.head.next = None
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        curr = self.head
        print("LinkedList is: ")
        while curr:
            print(" --> ", str(curr.data), end = " ")
            curr = curr.next
        print(" --> NULL")


class Solution:
    def recursive_sum(self, op, c1, c2, carry=0):
        if c1 and c2:
            carry = self.recursive_sum(op, c1.next, c2.next, carry)
            print(c1.data,c2.data, carry)
            if carry:
                sum = c1.data + c2.data + carry
            else:
                sum = c1.data + c2.data
            if sum > 9:
                rem = (sum % 10)
                carry = (sum - rem)//10
            else:
                carry = 0
                rem = sum
            print("sum", rem, carry)
            op.insert_athead(rem)
            return carry

    def add_numbers(self, no1, no2):
        l1 = linked_list()
        l2 = linked_list()
        for i in range(len(no1) -1, -1, -1):
            l1.insert_athead(no1[i])
        l1.print_list()
        for i in range(len(no2) - 1, -1, -1):
            l2.insert_athead(no2[i])
        l2.print_list()
        curr1 = l1.head
        curr2 = l2.head
        op = linked_list()
        carry, sum, rem  = 0, 0, 0
        if curr1 and curr2:
            self.recursive_sum(op, curr1, curr2, carry)
        return op


if __name__ == "__main__":
    no1 = [2, 0, 0, 8, 8]
    no2 = [4, 6, 9]
    if len(no1) > len(no2):
        no2 = [0] * (len(no1) - len(no2)) + no2
    if len(no2) > len(no1):
        no1 = [0] * (len(no2) - len(no1)) + no1
    s = Solution()
    op = s.add_numbers(no1, no2)
    print("After addition :")
    op.print_list()



# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         head = None
#         tail = head
#         c = s = 0
#         while(l1 or l2):
#             if l1:
#                 s = s + l1.val
#             if l2:
#                 s = s + l2.val
#             if c:
#                 s = s + c
#             if (s > 9):
#                 r = s%10
#                 c = int((s - s%10)/10)
#             else:
#                 c = 0
#                 r = s
#             if (head):
#                 tail.next = ListNode(r)
#                 tail = tail.next
#             else:
#                 head = ListNode(r)
#                 tail = head
#             if l1 : l1 = l1.next
#             if l2 : l2 = l2.next
#             s = 0
#         if c:
#             tail.next = ListNode(c)
#         return head






