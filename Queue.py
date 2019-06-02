#coding: utf8
class Queue(object):
    def __init__(self):
        self.list1 = []

    def is_empty(self):
        return self.list1 == []

    def enqueue(self, item):
        self.list1.append(item)

    def dequeue(self):
        self.list1.pop(0)

    def size(self):
        return len(self.list1)
if __name__ == "__main__":
    q=Queue()
    print(q.is_empty())
    print(q.size())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.is_empty())
    print(q.size())
    q.dequeue()
    q.dequeue()
    print(q.size())
