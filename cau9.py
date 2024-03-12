class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def deleteDuplicates(head):
  current = head

  while current and current.next:
    if current.val == current.next.val:
      current.next = current.next.next
    else:
      current = current.next

  return head


# Helper function to print the linked list
def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


head1 = ListNode(1)
head1.next = ListNode(1)
head1.next.next = ListNode(2)

print("Original linked list:")
printLinkedList(head1)

head1 = deleteDuplicates(head1)
print("\nLinked list after removing duplicates:")
printLinkedList(head1)

head2 = ListNode(1)
head2.next = ListNode(1)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(3)
head2.next.next.next.next = ListNode(3)

print("\nOriginal linked list:")
printLinkedList(head2)

head2 = deleteDuplicates(head2)
print("\nLinked list after removing duplicates:")
printLinkedList(head2)