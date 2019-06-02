#coding:utf8
class Stack(object):
    def __init__(self):
        self.list1 = []

    def is_empty(self):
        return self.list1 == []

    def push(self,item):
        self.list1.append(item)

    def pop(self):
        self.list1.pop()

    def top(self):
        # if self.list1:
        #     return self.list1[-1]
        # else:
        #     return None
        if self.list1 == []:
            return
        else:
            return self.list1[-1]
if __name__ == "__main__":
    s=Stack()
    print(s.top())
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.is_empty())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())




