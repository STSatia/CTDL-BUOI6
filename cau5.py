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

  def reverse(self):
    prev_node = None
    current_node = self.head
    while current_node:
      next_node = current_node.next
      current_node.next = prev_node
      prev_node = current_node
      current_node = next_node
    self.head = prev_node

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

print("Original linked list:")
linked_list.display()

linked_list.reverse()

print("\nLinked list after reversal:")
linked_list.display()