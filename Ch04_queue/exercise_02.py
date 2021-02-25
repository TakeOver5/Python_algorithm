from queue import Queue

q = Queue()

foods = ['漢堡', '薯條', '可樂']

for food in foods:
    q.put(food)
    print(f'成功插入 {food} 至佇列')

print("佇列輸出")

while not q.empty():
    print(q.get())