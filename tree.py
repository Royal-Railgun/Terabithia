class Node():
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class tree():
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        a = [self.root]
        if self.root is None:
            self.root = node
            return
        else:
            while a:
                cur = a.pop(0)

                if cur.lchild is None:
                    cur.lchild = node
                    return
                else:
                    a.append(cur.lchild)
                if cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    a.append(cur.rchild)

    def breadth_travel(self):
        if self.root is None:
            return
        a = [self.root]
        while a:
            cur = a.pop(0)
            print(cur.elem)
            if cur.lchild is not None:
                a.append(cur.lchild)
            if cur.rchild is not None:
                a.append(cur.rchild)

    def pre_travel(self,root):
        if root is None:
            return
        # print(root.elem)
        self.pre_travel(root.lchild)
        # print(root.elem)
        self.pre_travel(root.rchild)
        print(root.elem)



# def breadth_travel(root):
#     if root is None:
#         return
#     a=[root]
#     while a:
#         cur = a.pop(0)
#         print(cur.elem)
#         if cur.lchild is not None:
#             a.append(cur.lchild)
#         if cur.rchild is not None:
#             a.append(cur.rchild)



if __name__ == "__main__":
    t=tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    # t.breadth_travel(t.root)
    t.pre_travel(t.root)



