class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def insert_after(self, previous_node, data):
        """링크드 리스트 추가 연산 메소드"""
        # 코드를 쓰세요

        new_node = Node(data)

        if previous_node == self.tail:
            previous_node.next = new_node
            new_node.prev = previous_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            new_node.prev = previous_node
            previous_node.next = new_node
            new_node.next.prev = new_node

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        # 코드를 쓰세요
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node

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


    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)
        
        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        # 코드를 쓰세요
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        elif node_to_delete is self.head and node_to_delete is not self.tail:
            self.head = node_to_delete.next
            self.head.prev = None
        elif node_to_delete is self.tail and node_to_delete is not self.head:
            self.tail = node_to_delete.prev
            self.tail.next = None
        elif node_to_delete is not self.head and node_to_delete is not self.tail:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        return node_to_delete.data


    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next # 다음 노드로 넘어간다

        return res_str

my_list = DoubleLinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)