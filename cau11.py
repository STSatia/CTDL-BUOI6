class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def reverseList(head):
  prev_node = None
  current_node = head

  while current_node:
    next_node = current_node.next
    current_node.next = prev_node
    prev_node = current_node
    current_node = next_node

  return prev_node


# Helper function to print the linked list
def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
printLinkedList(head)

reversed_head = reverseList(head)

print("\nReversed linked list:")
printLinkedList(reversed_head)