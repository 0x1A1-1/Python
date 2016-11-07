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


class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node


    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)



    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node






    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print root.data
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print root.data
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)
            print root.data
