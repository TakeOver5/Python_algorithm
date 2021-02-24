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
    
    def add_double_list(self, new_node):
        '''將節點加入雙向鏈結串列'''
        if isinstance(new_node, Node):      # 先確定這個 item 是節點
            if self.head == None:           # 如果串列為空
                self.head = new_node        # 頭節點是 new_node
                new_node.previous = None    # 指向前方
                new_node.next = None        # 指向後方
                self.tail = new_node        # 尾節點也是 new_node
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
    
    def print_list_from_head(self):
        '''從頭部列印鏈結串列'''
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def print_list_from_tail(self):
        '''從尾部列印鏈結串列'''
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous

double_link = Double_linked_list()
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)

for n in [n1, n2, n3]:
    double_link.add_double_list(n)

print("從頭部列印雙向鏈結串列")
double_link.print_list_from_head()

print("從尾部列印雙向鏈結串列")
double_link.print_list_from_tail()