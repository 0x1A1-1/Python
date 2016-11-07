import operator

class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.data


def parseExpression(exp):
    RootNode = Node('')
    CurrNode = RootNode
    stack = []
    for i in range(len(exp)):
        if exp[i] == "(":
            CurrNode.left = Node('')
            stack.append(CurrNode)
            CurrNode = CurrNode.left
        elif exp[i] not in ["+","-","*","/",")"]:
            CurrNode.data = exp[i]
            CurrNode = stack.pop()
        elif exp[i] in ["+","-","*","/"]:
            CurrNode.data = exp[i]
            CurrNode.right = Node('')
            stack.append(CurrNode)
            CurrNode = CurrNode.right
        elif exp[i]==")":
            if CurrNode==RootNode:
                return RootNode
            else:
                CurrNode=stack.pop()
        else:
            raise ValueError
    return RootNode

def evaluate(root):
    operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = root.left
    rightC = root.right

    if leftC and rightC:
        func = operators[root.data]
        return func(evaluate(leftC), evaluate(rightC))
    else:
        return int(root.data)

test = parseExpression("(1+(1*(5+3)))")

print evaluate(test)
