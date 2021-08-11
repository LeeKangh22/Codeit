# Hash Function
class Node:
    # for linked list
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    # Lineked list
    def __init__(self):
        self.head = None
        self.tail = None
    
    def find_node_with_key(self, key):
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator
            iterator = iterator.next
        
        return None

    def append(self, key, value):
        new_node = Node(key, value)
        # empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, node_to_delete):
        # last data
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        # head data
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None
        # tail data
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next 
            node_to_delete.next.prev = node_to_delete.prev
    
    def __str__(self):
        res_str = ""

        iterator = self.head
        while iterator is not None:
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next
        
        return res_str

def hash_fuction_remainder(key, array_size):
    return key % array_size

def hash_function_multiplication(key, array_size, a):
    """Make hash table's size with multiplication to 0 ~ array_size - 1"""
    temp = a * key 
    temp = temp - int(temp) 

    return int(array_size * temp)

    