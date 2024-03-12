class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self, value):
    self.head = Node(value)
    self.tail = self.head
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1

  def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
    self.length += 1

  def insert(self, index, value):
    if index >= self.length:
      self.append(value)
      return
    if index == 0:
      self.prepend(value)
      return

    new_node = Node(value)
    leader = self.traverse_to_index(index - 1)
    new_node.next = leader.next
    leader.next = new_node
    self.length += 1

  def remove(self, index):
    if index >= self.length:
      print("Index out of range")
      return
    if index == 0:
      self.head = self.head.next
      self.length -= 1
      return

    leader = self.traverse_to_index(index - 1)
    unwanted_node = leader.next
    leader.next = unwanted_node.next
    self.length -= 1

  def traverse_to_index(self, index):
    current_node = self.head
    current_index = 0
    while current_index != index:
      current_node = current_node.next
      current_index += 1
    return current_node

  def display(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.value, end=" -> ")
      current_node = current_node.next
    print("None")


linked_list = LinkedList(10)
linked_list.append(20)
linked_list.append(30)
linked_list.prepend(5)
linked_list.insert(2, 25)
linked_list.remove(1)
linked_list.display()