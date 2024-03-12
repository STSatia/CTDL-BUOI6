class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def removeDuplicates(head):
  if not head:
    return head

  seen = set()
  current = head
  prev = None

  while current:
    if current.val in seen:
      prev.next = current.next
    else:
      seen.add(current.val)
      prev = current
    current = current.next

  return head


def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next.next = ListNode(5)

print("Original linked list:")
printLinkedList(head)

head = removeDuplicates(head)
print("\nLinked list after removing duplicates:")
printLinkedList(head)