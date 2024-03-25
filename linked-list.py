class Node:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  
  def printList(self):
    if self.head is None:
      print("Linked list is empty")
      return

    itr = self.head
    while itr:
      if itr.next:
        print(itr.val, end = "-->")
        itr = itr.next
      else:
        print(itr.val)

  
  def insertAtBeginning(self, val):
    node = Node(val, self.head)
    node.next = self.head
    self.head = node


llist = LinkedList()

llist.insertAtBeginning(10)
llist.insertAtBeginning(20)
llist.insertAtBeginning(30)
# Print the linked list
llist.printList()

  
 

