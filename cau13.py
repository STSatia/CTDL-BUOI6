class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def middleNode(head):
  slow_ptr = head
  fast_ptr = head

  while fast_ptr and fast_ptr.next:
    slow_ptr = slow_ptr.next
    fast_ptr = fast_ptr.next.next

  return slow_ptr


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

middle_node1 = middleNode(head1)
print("Middle node of the linked list:", middle_node1.val)