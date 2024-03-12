class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def find_middle(self):
    if self.head is None:
      return None

    slow_ptr = self.head
    fast_ptr = self.head

    while fast_ptr and fast_ptr.next:
      slow_ptr = slow_ptr.next
      fast_ptr = fast_ptr.next.next

    return slow_ptr

  def display(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")


linked_list = LinkedList()

linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)

print("Original singly linked list:")
linked_list.display()

middle_node = linked_list.find_middle()
if middle_node:
  print("\nMiddle node:", middle_node.data)