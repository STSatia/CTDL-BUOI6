class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def getIntersectionNode(headA, headB):
  if not headA or not headB:
    return None

  def getLength(node):
    length = 0
    while node:
      length += 1
      node = node.next
    return length

  lenA, lenB = getLength(headA), getLength(headB)
  tailA, tailB = headA, headB
  while tailA.next:
    tailA = tailA.next
  while tailB.next:
    tailB = tailB.next

  if tailA != tailB:
    return None

  ptrA, ptrB = headA, headB

  diff = abs(lenA - lenB)
  if lenA > lenB:
    for _ in range(diff):
      ptrA = ptrA.next
  else:
    for _ in range(diff):
      ptrB = ptrB.next

  while ptrA != ptrB:
    ptrA = ptrA.next
    ptrB = ptrB.next

  return ptrA


def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(0)
headB.next.next = headA.next.next
print("List A:")
printLinkedList(headA)
print("\nList B:")
printLinkedList(headB)

intersection_node = getIntersectionNode(headA, headB)
if intersection_node:
  print("\nThe two lists intersect at node with value:", intersection_node.val)
else:
  print("\nThe two lists do not intersect.")