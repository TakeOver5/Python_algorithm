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

    def length(self):
        '''計算節點數量'''
        ptr = self.head
        counter = 0
        while ptr:
            counter += 1
            ptr = ptr.next
        return counter
    
    def search(self, *value_List):
        mydict = dict.fromkeys(value_List, 0)
        ptr = self.head
        while ptr:
            if ptr.data in mydict:
                mydict[ptr.data] += 1
            ptr = ptr.next
        return mydict

link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(5)
link.head.next = n2
n2.next = n3

print('所建的鏈結串列')
link.print_list()

print('分別列出數值 5, 15, 20 的出現次數')
mydict = link.search(5, 15, 20)

for key, value in mydict.items():
    print(f'{key :<2} 出現 {value} 次')