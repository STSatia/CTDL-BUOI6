class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def mergeTwoLists(list1, list2):
  dummy_head = ListNode()
  current = dummy_head

  while list1 and list2:
    if list1.val < list2.val:
      current.next = list1
      list1 = list1.next
    else:
      current.next = list2
      list2 = list2.next
    current = current.next

  if list1:
    current.next = list1
  elif list2:
    current.next = list2

  return dummy_head.next


# Helper function to print the linked list
def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

print("First sorted linked list:")
printLinkedList(list1)

print("\nSecond sorted linked list:")
printLinkedList(list2)

merged_list = mergeTwoLists(list1, list2)
print("\nMerged sorted linked list:")
printLinkedList(merged_list)