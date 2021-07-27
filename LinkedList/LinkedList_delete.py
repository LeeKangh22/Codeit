# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete_after(self, previous_node):
        data = previous_node.next.data

        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next
        return data            

    def insert_after(self, previous_node, data):
        new_node = Node(data)
        
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

    def get_node(self, index):
        iterator = self.head
        
        for i in range(0,index):
            iterator = iterator.next
        return iterator

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

# Make new linked list 
my_list = LinkedList()

# Append data
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

iterator = my_list.head
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
print('------')
# Insert node
node_1 = my_list.get_node(2)
my_list.insert_after(node_1, 6)

iterator = my_list.head
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
print('-------')

# Delete node
node_2 = my_list.get_node(3)
my_list.delete_after(node_2)

iterator = my_list.head
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
print('------')

# Print
iterator = my_list.head
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next