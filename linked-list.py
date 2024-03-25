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


  def getLength(self):
        count = 0
        if self.head is None:
            return count
            
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count

  
  def insertAtBeginning(self, val):
    node = Node(val, self.head)
    node.next = self.head
    self.head = node


  def insertAtEnd(self, val):
        node = Node(val, self.head)
        
        if self.head is None:
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = node
    

llist = LinkedList()

llist.insertAtBeginning(10)
llist.insertAtBeginning(20)
llist.insertAtBeginning(30)

llist.insertAtEnd(15)
llist.insertAtEnd(25)
llist.insertAtEnd(35)

# Print the linked list
llist.printList()
print("Length:", llist.getLength())

  
 

