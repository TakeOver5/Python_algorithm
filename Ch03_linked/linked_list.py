class Node():
    '''節點'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_list():
    '''鏈結串列'''
    def __init__(self):
        self.head = None
    
    def print_list(self):
        '''列印鏈結串列'''
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def begining(self, newdata):
        '''在第一個節點前插入新節點'''
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node
    
    def ending(self, newdata):
        '''在串列末端插入新節點'''
        new_node = Node(newdata)
        if self.head == None:
            self.head = new_node
            return
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_node

    def between(self, pre_node, newdata):
        '''在串列兩個節點間插入新節點'''
        if pre_node == None:
            print("缺插入節點的前一個節點")
            return
        new_node = Node(newdata)
        new_node.next = pre_node.next
        pre_node.next = new_node
        
    def rm_node(self, rmkey):
        '''刪除值是 rmkey 的節點'''
        ptr = self.head             # 暫時指標
        if ptr:
            if ptr.data == rmkey:
                self.head = ptr.next
        while ptr:
            if ptr.data == rmkey:
                break
            prev = ptr
            ptr = ptr.next
        if ptr == None:
            return
        prev.next = ptr.next

link = Linked_list()
link.head = Node(5)

n2 = Node(15)
n3 = Node(25)

link.head.next = n2
n2.next = n3

link.print_list()

print('''新的鏈結串列''')
link.rm_node(15)
link.print_list()