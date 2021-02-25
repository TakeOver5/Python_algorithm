class Queue():
    def __init__(self):
        '''Queue 佇列'''
        self.queue = []
    
    def enqueue(self, data):
        '''data 插入佇列'''
        self.queue.insert(0, data)
        print(f'成功插入 {data} 至佇列')

    def dequeue(self):
        '''讀取佇列'''
        if len(self.queue):
            return self.queue.pop()
        return "佇列是空的"
    
    def size(self):
        '''回傳佇列長度'''
        return len(self.queue)

q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print('佇列長度是：', q.size())

    