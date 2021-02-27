# 基礎演算法

## 鏈結串列

欲想建立鏈結串列，應撰寫兩個類別，分別為 Node 類和 Linked_list 類。

### Node 類

該類為節點，用於存放資料與指標。
其中應建立兩個屬性，如果是雙向鏈結，則是三個屬性。

data: 用於存放資料
next: 指向下一筆資料的地址
previous: 指向上一筆資料的地址

### Linked_list 類

該類用於存放 Node 類，與操作鏈結串列。
另外應建立兩個屬性，head 和 tail 屬性，分別指向鏈結串列的頭尾，便於方法操作。

head: 用於指向鏈結的第一筆資料

tail: 用於指向鏈結的末尾資料

Linked_list(): 打印資料。while 與 head 屬性搭配使用，直到某 Node(節點).next = false

begining(newdata): 在第一個節點前插入新節點。注意 head 屬性必須改為指向 newdata

ending(newdata): 在末端插入新節點。注意如果 head 為 None 則直接讓 head = new_node，

between(pre_node, newdata): 在 pre_node 節點前插入新節點。插入前先判斷 pre_node 是否存在。

rm_node(rekey): 刪除值是 rmkey 的節點。如果刪除節點剛好是 head 要特別處理。

add_double_list(new_node): 將節點加入雙向鏈結串列。注意串列是否為空。

print_list_from_head(): 從頭部列印鏈結串列。

print_list_from_tail(): 從尾部列印鏈結串列。

## 佇列

先進先出的特性。
Python 內建有 queue 模組。分別有 put(data)、get() 和 empty() 方法。 

### Queue 類

queue: 用於存放佇列資料。是一個列表

enqueue(data): 將 data 插入佇列

dequeue(): 讀取佇列，注意佇列是否為空

size(): 回傳佇列長度

empty(): 佇列是否為空

## 堆疊

先進後出的特性。
Python 的串列可以簡單模擬此特性。append() 和 pop()。

### Stack 類

stack: 用於存放佇列資料。是一個列表

push(data): 將 data 加入堆疊

pop(): 傳回堆疊頂端資料，並同時刪除

get(): 傳回堆疊頂端資料，但不刪除

size(): 回傳堆疊長度

empty(): 堆疊是否為空，return stack == []

cls(): 清空堆疊











