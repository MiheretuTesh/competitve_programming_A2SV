class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.d = [None] * k
        self.dequeSize = 0
        self.front = 0
        self.rear = -1
    def insertFront(self, value: int) -> bool:
        if (self.isFull()==False):
            self.front = (self.front-1)%self.k
            self.d[self.front] = value
            self.dequeSize += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if (self.isFull()==False):
            self.rear = (self.rear+1)%self.k
            self.d[self.rear] = value
            self.dequeSize += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if(self.isEmpty()==False):
            self.front = (self.front+1)%self.k
            self.dequeSize -= 1
            return True
        return False
    def deleteLast(self) -> bool:
        if(self.isEmpty()==False):
            self.rear = (self.rear-1)%self.k
            self.dequeSize -= 1
            return True
        return False

    def getFront(self) -> int:
        if(self.isEmpty()==False):
            return self.d[self.front]
        return -1

    def getRear(self) -> int:
        if(self.isEmpty()==False):
            return self.d[self.rear]
        return -1
    def isEmpty(self) -> bool:
        return True if self.dequeSize==0 else False

    def isFull(self) -> bool:
        return True if self.dequeSize==len(self.d) else False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()