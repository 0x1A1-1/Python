class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, key):
        self.stack.append(key)

    def pop(self):
        if not self.stack:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def preorder(root):
    if root:
        print root.val
        preorder(root.left)
        preorder(root.right)

def preInter(root):
    stack = Stack()
    stack.push(root)

    while(stack.size()>0):
        root = stack.pop()
        if root:
            print root.val
        if root.right:
            stack.push(root.right)
        if root.left:
            stack.push(root.left)


def inorder(root):
    if root:
        inorder(root.left)
        print root.val
        inorder(root.right)

def inoInter(root):
    stack = Stack()
    done=False
    while not done:
        if root:
            stack.push(root)
            root=root.left
        else:
            if(stack.size()>0):
                root = stack.pop()
                print root.val
                root = root.right
            else:
                done=True




def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.val

def postInter(root):
    stack=Stack();
    done=0
    while True:
        while root:
            if root.right:
                stack.push(root.right)
            stack.push(root)
            root=root.left

        root = stack.pop()

        if (root.right is not None and stack.peek()==root.right) :
            stack.pop()
            stack.push(root)
            root = root.right
        else:
            print root.val
            root=None

        if (stack.size()<=0):
            break

def levelorder(root):
    for i in range(1, treeHeight(root)+1):
        print printGivenLevel(root, i)

def printGivenLevel(root, level):

    if root is None:
        return
    print "level is", level
    print "root is ", root.val
    if root.left is None:
        print "left is ", root.left.val
    if not root.right:
        print " right is ",root.right.val
    if level == 1:
        return root.val
    elif level<1:
        return
    elif level>1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def levelOrderQue(root):
    queue = list()
    if not root:
        return
    else:
        queue.append(root)
        while len(queue)>0:
            root=queue.pop(0)
            if root:
                print root.val
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

def treeHeight(root):
    if not root:
        return 0
    else:
        left = treeHeight(root.left)
        right = treeHeight(root.right)

        if left>right:
            return left+1
        else:
            return right+1



root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.right.right.left = Node(8)
root.left.right.right.right = Node(9)

# preorder(root)
# print "hey"
# preInter(root)

levelOrderQue(root)
