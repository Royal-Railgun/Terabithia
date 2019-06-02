#coding:utf8
#单向链表
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None

class SingleLink(object):
    def __init__(self):
        self.__head  = None

    def is_empty(self):
        return self.__head is None

    def len(self):
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count +=1
        return count

    def append(self,item):
        cur = self.__head
        node = Node(item)
        if cur is None:
            self.__head = node
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node



    def insert(self,pos,item):
        cur = self.__head
        node = Node(item)
        count =0
        if pos<1:
            self.add(item)
        elif pos>self.len()-1:
            self.append(item)
        else:
            while count < pos-1:
                cur = cur.next
                count+=1

            node.next = cur.next
            cur.next = node

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem,end="")
            cur = cur.next


    def remove(self,item):
        cur = self.__head
        if cur is None:
            return
        while cur is not None:
            if cur.elem == item:
                if cur is self.__head:
                    self.__head = cur.next

                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
    def search(self,item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            cur =cur.next
        return  False

if __name__ == "__main__":
    s=SingleLink()
    print(s.is_empty())
    print(s.len())
    s.add(1)
    s.add(2)
    s.append(8)
    s.append(9)
    s.travel()
    print(s.len())
    print(s.is_empty())
    s.insert(0,0)
    s.insert(3,3)
    s.insert(9,10)
    s.travel()
    s.remove(0)
    s.remove(10)
    s.remove(3)
    print("-------")
    s.travel()
    print(s.search(9))
    print(s.search(12))





