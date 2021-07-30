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
    
    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        # 코드를 쓰세요
        data = self.head.data
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
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
    
    def delete_after(self, previous_node):
        data = previous_node.next.data

        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next
        return data    
    
    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        # 코드를 쓰세요
        iterator = self.head
        while iterator.next is not None: #iterator is not None
            if iterator.data == data:
                return iterator
            else:
                iterator = iterator.next
                if iterator.next is None:
                     if iterator.data == data:
                        return iterator
        return None
    
    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        # 코드를 쓰세요
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.data = data
            self.head = new_node
'''
# Make new linked list 
my_list = LinkedList()

# Append data
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
node_1 = my_list.get_node(2)
my_list.insert_after(node_1, 6)

# Print
iterator = my_list.head
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

'''