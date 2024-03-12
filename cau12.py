class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def isPalindrome(head):
  # Store elements of the linked list in an array
  values = []
  current = head
  while current:
    values.append(current.val)
    current = current.next

  # Check if the array is a palindrome
  left, right = 0, len(values) - 1
  while left < right:
    if values[left] != values[right]:
      return False
    left += 1
    right -= 1

  return True


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)

print("Is the linked list a palindrome?", isPalindrome(head1))