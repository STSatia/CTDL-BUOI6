class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def removeElements(head, val):
  # Create a dummy node to simplify the removal process
  dummy = ListNode(0)
  dummy.next = head
  current = dummy

  while current.next:
    if current.next.val == val:
      current.next = current.next.next
    else:
      current = current.next

  return dummy.next


# Helper function to print the linked list
def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(6)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(5)
head1.next.next.next.next.next.next = ListNode(6)

print("Original linked list:")
printLinkedList(head1)

val1 = 6
head1 = removeElements(head1, val1)
print("\nLinked list after removing elements with value", val1)
printLinkedList(head1)

head2 = ListNode(7)
head2.next = ListNode(7)
head2.next.next = ListNode(7)
head2.next.next.next = ListNode(7)

print("\nOriginal linked list:")
printLinkedList(head2)

val2 = 7
head2 = removeElements(head2, val2)
print("\nLinked list after removing elements with value", val2)
printLinkedList(head2)