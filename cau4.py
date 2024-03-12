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

  def delete_node_at_index(self, index):
    if self.head is None:
      return None

    if index == 0:
      deleted_node = self.head
      self.head = self.head.next
      deleted_node.next = None
      return deleted_node

    prev_node = None
    current_node = self.head
    count = 0

    while current_node and count != index:
      prev_node = current_node
      current_node = current_node.next
      count += 1

    if current_node is None:
      return None

    deleted_node = current_node
    prev_node.next = current_node.next
    deleted_node.next = None
    return deleted_node

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

deleted_node = linked_list.delete_node_at_index(2)
if deleted_node:
  print("\nDeleted node:", deleted_node.data)

print("\nLinked list after deletion:")
linked_list.display()