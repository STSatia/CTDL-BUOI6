class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def partition(head, x):
  before_head = ListNode(0)
  before = before_head
  after_head = ListNode(0)
  after = after_head

  current = head
  while current:
    if current.val < x:
      before.next = current
      before = before.next
    else:
      after.next = current
      after = after.next
    current = current.next

  after.next = None
  before.next = after_head.next

  return before_head.next


def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(8)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(10)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(1)

print("Original linked list:")
printLinkedList(head)

x = 5
partitioned_head = partition(head, x)
print("\nLinked list after partitioning around {}: ".format(x))
printLinkedList(partitioned_head)