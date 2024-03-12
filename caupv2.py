class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def nthToLast(head, n):
  if not head or n <= 0:
    return None

  ptr1 = head
  ptr2 = head

  for _ in range(n):
    if not ptr2:
      return None
    ptr2 = ptr2.next

  while ptr2:
    ptr1 = ptr1.next
    ptr2 = ptr2.next
  return ptr1.val


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2
print("The {}th to last element of the linked list is: {}".format(
    n, nthToLast(head, n)))