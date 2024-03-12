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

  def remove_duplicates(self):
    if self.head is None:
      return

    current = self.head

    while current:
      runner = current
      while runner.next:
        if runner.next.data == current.data:
          runner.next = runner.next.next
        else:
          runner = runner.next
      current = current.next

  def display(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")


linked_list = LinkedList()

linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(4)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.insert_at_end(2)

print("Original singly linked list:")
linked_list.display()

linked_list.remove_duplicates()

print("\nLinked list after removing duplicates:")
linked_list.display()