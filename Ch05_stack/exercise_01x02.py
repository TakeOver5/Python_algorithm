class Stack():
    def __init__(self):
        self.my_stack = []
        self.index = 0
    
    def my_push(self, data):
        self.index += 1
        self.my_stack.append(data)
    
    def my_pop(self):
        if self.index:
            self.index -= 1
            return self.my_stack.pop()
    
    def size(self):
        return len(self.my_stack)

    def isEmpty(self):
        return self.my_stack == []

    def get(self):
        return self.my_stack[self.index - 1]

    def cls(self):
        del self.my_stack[:]

stack = Stack()

fruits = ['Grape', 'Mange', 'Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print('將 %s 水果堆入堆疊' % fruit)

print('堆疊有 %d 種水果' % stack.size())

for x in range(3):
    print('堆疊取出 %s 水果，同時不刪除' % stack.get())

stack.cls()

while not stack.isEmpty():
    print(stack.my_pop())

print('程式結束')