class Node():
    '''節點'''
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class Double_linked_list():
    '''鏈結串列'''
    def __init__(self):
        self.head = None
        self.tail = None

    def add_Double_list(self, new_node):
        if isinstance(new_node, Node):
            if self.head == None:
                self.head = new_node
                new_node.previous = None
                new_node.next = None
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
    
    def print_list_from_head(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def print_list_from_tail(self):
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous

list_data = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']

linked_list = Double_linked_list()

for str in list_data:
    linked_list.add_Double_list(Node(str))

print("從頭部列印雙向鏈結串列")
linked_list.print_list_from_head()

print("從尾部列印雙向鏈結串列")
linked_list.print_list_from_tail()
