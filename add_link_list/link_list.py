class Node:
    def __init__(self , data):
        ##node 初始化
        def __repr__(self):
            return str(self.data)

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def append(self , this_node):
        if isinstance(this_node , Node):
            pass
        else:
            this_node = Node(data=this_node)
        if self.is_empty():
            self.head = this_node
        else:
            node = self.head
            while node.pnext:
                node = node.pnext
            node.pnext = this_node
        self.length +=1

    def insert(self , value , index):
        if type(index) is int:
            if index > self.length:
                return
            else:
                this_node = Node(data=value)
                current_node = self.head

            if index == 0:
                self.head = this_node
                this_node.pnext = current_node
                return

            while index -1:
                current_node = current_node.pnext
                index-=1

            this_node.pnext = current_node.pnext
            current_node.pnext = this_node
            self.length+=1
            return

    def delete(self , index):
        if type(index) is int:
            if index > self.length:
                return
            else:
                if index == 0:
                    self.head = self.head.pnext
                else:
                    current_node = self.head
                    while index - 1:
                        current_node = current_node.pnext
                        index-=1
                    current_node.pnext = current_node.pnext.pnext