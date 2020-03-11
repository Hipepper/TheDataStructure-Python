class Node:                          ##定义节点类
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None             #前后指针（前后驱）为空
    def getData(self):               #获取节点数据
        return self.data
 
    def setData(self, data):         #修改节点数据
        self.data = data    

    def getNext(self):               #获取下一个节点
        return self.next

    def getPrev(self):               #获取上一个节点
        return self.prev

class DoubleList:                    #定义双链表类
    def __init__(self):              #析构函数 
        self.phead = None            #头尾指针为空
        self.ptail = None
        self.lenOfList = 0           #链表长度
    def isEmpty(self):
        return self.phead == None

    def append(self, data):          #尾插节点，先判断链表是否是空
        if self.lenOfList == 0:   
            node = Node(data)
            self.phead = node
            self.ptail = node
            self.lenOfList = 1
            return
        node = Node(data)            #定义新节点
        ptail = self.ptail           #此时ptail就是最后一个节点，用尾指针指向
        ptail.next = node            #位置在下移，头不动
        node.prev = ptail
        self.ptail = node
        self.lenOfList += 1


    def insert(self, index, data):   #插入节点函数，index是下标值，data是插入的数据
        lenOfList = self.lenOfList
        if (index<0 and abs(index)>lenOfList) or (index>0 and index>=lenOfList):   #运行用户从后往前插入，但是注意绝对值
            return False
        if index < 0:                #倒插
            index = index + lenOfList
        if index == 0:               #index=0,就是从头插入，如果链表不为空就前移指针，如果为空，就用尾指针指向
            node = Node(data)
            if self.phead != None:   
                self.phead.prev = node
            else:
                self.ptail = node
            node.next = self.phead
            self.phead = node
            self.lenOfList += 1
            return True
        if index == lenOfList - 1:  #下标值就是尾部，直接尾插数据
            return self.append(data)

        node1 = self.phead
        for i in range(0, index):   #借助其他人思想，既然节点没有下标，就用头指针遍历到下标位置
            node1 = node1.next
        node2 = node1.next
        node = Node(data)
        node.prex = node1
        node.next = node2
        node1.next = node
        node2.prev = node
        self.lenOfList += 1
        return True

    def getByData(self, data):   #根据数据找节点
        node = self.phead
        for i in range(self.lenOfList):
            if node.data == data:
                return node
            else:
                node = node.next
        else:
            return False

    def getByIndex(self, index):  #根据下标返回节点？？？
        if index >= self.lenOfList:
            print("下标值无效")
            return False
        if index == 0:
            return self.phead
        node = self.phead
        for i in range(self.lenOfList):
            if i == index:
                return node
            node = node.next

    def setData(self, index, data):  #更新数据
        if index >= self.lenOfList:
            return False
        if index == 0:
            self.phead.data = data
        now = self.phead
        for i in range(self.lenOfList):
            if i == index:
                now.data = data
                return True
            now = now.next

    def remove(self, index):  #删除指定下标节点
        if index >= self.lenOfList:
            return False
        if index == 0:
            self.phead = self.phead.next
            if self.lenOfList != 1:
                self.phead.prev = None
            self.lenOfList -= 1
            return True
        if index == self.lenOfList-1:
            self.ptail = self.ptail.prev
            self.ptail.next = None
            self.lenOfList -= 1
            return True
        node = self.phead
        for i in range(self.lenOfList):
            if i == index:
                node.next.prev = node.prev
                node.prev.next = node.next
                self.lenOfList -= 1
                return True
            node = node.next

    def reverse(self):  #倒置列表，跟别人学的
        now = self.phead
        last = None
        for i in range(self.lenOfList):
            last = now
            now = now.next
            tmp = last.prev
            last.prev = last.next
            last.next = tmp
        tmp = self.phead
        self.phead = self.ptail
        self.ptail = tmp
        return True

    def delete(self):     #怎么释放已经创建的节点数据???
        self.phead = None
        self.ptail = None
        self.lenOfList = 0

    def __str__(self):    #打印链表
        string = ''
        node = self.phead
        for i in range(self.lenOfList):
            string += str(node.data) + '->'
            node = node.next
        return string



test=DoubleList()
test.append(12)
test.append(13)
test.append(14)
test.append(15)
test.append(16)


print(test)
print("链表长度:{}".format(test.lenOfList))

test.insert(3,1)  #3的后面插入1
print("修改之后的链表为：{}".format(test))

test.remove(0)
print("修改之后的链表为：{}".format(test))

test.setData(2,2) #2号位置改为2
print("修改之后的链表为：{}".format(test))

print(test.getByData(16).data)
print(test.getByIndex(1).data)