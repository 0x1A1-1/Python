class queue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def enqueue(self,key):
        self.stack.append(key)

    def dequeue(self):
        if len(self.stack1)==0 and len(self.stack2==0):
            return
            while len(self.stack1)>0:
                if len(self.stack2)==0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
