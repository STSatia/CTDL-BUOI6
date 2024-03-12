class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def sumLists(l1, l2):
  dummy_head = ListNode()
  current = dummy_head
  carry = 0

  while l1 or l2 or carry:
    sum_val = carry
    if l1:
      sum_val += l1.val
      l1 = l1.next
    if l2:
      sum_val += l2.val
      l2 = l2.next

    carry = sum_val // 10
    current.next = ListNode(sum_val % 10)
    current = current.next

  return dummy_head.next


def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


l1 = ListNode(7)
l1.next = ListNode(1)
l1.next.next = ListNode(6)

l2 = ListNode(5)
l2.next = ListNode(9)
l2.next.next = ListNode(2)

print("Linked list 1:")
printLinkedList(l1)
print("\nLinked list 2:")
printLinkedList(l2)

result = sumLists(l1, l2)
print("\nSum of the two linked lists:")
printLinkedList(result)