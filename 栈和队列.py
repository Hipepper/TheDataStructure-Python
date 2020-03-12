# 栈类  队列   list法   区别在于pop(0)

class Stack:
    def __init__(self):      #构造一个空栈
        self.data=[]
    
    def En(self,value):      #进栈
        self.data.append(value)
    
    def De(self):            #出栈
        self.data.pop()     #注意，如果是pop(0),那就变成队列了
    
    def isEmpty(self):       #判断是否是空
        return(self.data==[])
    
    def clear(self):         #删除栈
        del(self.data)
    
    def size(self):          #链表长度
        return(len(self.data))
    
    def print(self):
        print(self.data)
    

q=Stack()
print(q.isEmpty())

for i in range(10,100,10):
    q.En(i)

print(q.isEmpty())
print(q.size())
print(q.print())

q.De()
q.De()
print(q.print())

#队列  链表法

class Node:       #节点结构
    def __init__(self,value):
        self.value=value
        self.next=None

class Head:       #定义一个头结构，两个指针指向头节点和尾节点
    def __init__(self):
        self.left=None 
        self.right=None 
        self.Length=0

class Queue:
    def __init__(self):     #初始化队列，头结构为空
        self.head=Head()    #初始化要带self
       
    
    def is_empty(self):
        if self.head.left:
            return False
        else:
            return True
    
    def En(self,value):     #进入队列
        node=Node(value)         #注意出错了，value要带入初始化
        if(self.head.left==self.head.right):  #空队列
            node.value=value
            self.head.right=node
            self.head.left=node
        else:
            temp=self.head.right
            self.head.right=node
            temp.next=node
        self.head.Length+=1


    def De(self):              #出队列
        p = self.head
        if p.left and (p.left == p.right):  #队列中仅有一个元素
            temp = p.left
            p.left = p.right = None
            p.Length-=1
            return temp.value   
        if p.left and (p.left != p.right):  #队列中不止一个元素
            temp=p.left
            temp.next=p.left
            p.Length-=1
            return(temp.value)
    def __str__(self):          #打印队列
        string=""
        node = self.head.left
        for i in range(self.head.Length):
            string += str(node.value)+'->'       #打印链表值有点问题？！！！ 
           # node=node.next                               
        return string
            
            



        
Q=Queue()
Q.En(19)
Q.En(15)
Q.En(13)

print("队列长度：{}".format(Q.head.Length))
print(Q)
