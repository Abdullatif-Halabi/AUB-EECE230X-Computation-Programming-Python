lenn = len
class Queue(object):
    def __init__(self,maxSize=10):
        self.L = [None]*maxSize
        self.size = 0
        self.maxSize = maxSize
        self.tail = 0
        self.head = 0

    def enqueue(self,value):
        assert not self.isFull(), "Queue Full"
        self.L[self.tail] = value
        if self.tail<self.maxSize-1:
            self.tail+=1
        else:
            self.tail = 0
        self.size +=1

    def dequeue(self):
        assert not self.isEmpty(), 'Queue Empty'
        val = self.L[self.head]
        if self.head < self.maxSize-1:
            self.head +=1
        else:
            self.head = 0
        self.size -=1
        return val
    
    def peakhead(self):
        assert not self.isEmpty(),'Queue Empty'
        return self.L[self.head]
    
    def isFull(self):
        return self.size == self.maxSize
    
    def isEmpty(self):
        return self.size==0
    
    def __str__(self):
        s=""
        index = self.head
        for count in range(self.size):
            s = s+ str(self.L[index])+","
            if index<self.maxSize-1:
                index+=1
            else:
                index = 0
        return '['+s[:-1]+']'
    
    def __len__(self):
        return self.size

class UnboundedQueue(Queue):
    def __doubleList(self):
        newL = [None] *(2*self.maxSize)
        for i in range(self.head ,lenn(self.L)):
            newL[i-self.head] = self.L[i]
        if self.tail <= self.head :
            j = 0
            for i in range(0,self.head):
                newL[lenn(self.L)-self.head +j]=self.L[i]
                j+=1
        self.tail = lenn(self.L)
        self.head = 0
        self.maxSize = lenn(newL)
        self.L = newL
        # self.size = self.size

    def enqueue(self,value):
        if self.isFull():
            self.__doubleList()
            self.L[self.tail] = value
            self.tail +=1 
            self.size += 1
        else:
            self.L[self.tail] = value
            if self.tail<self.maxSize-1:
                self.tail+=1
            else:
                self.tail = 0
            self.size +=1



Q = UnboundedQueue(5)
for i in range(5):
    Q.enqueue(i)
print(Q)
Q.dequeue()
print(Q)
Q.dequeue()
print(Q)
for i in range(5):
    Q.enqueue(i)
print(Q)
for i in range(10):
    Q.enqueue(i)
print(Q)

# L =[1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
# print(len(L) , sum(L))
# for i in L:
#     if i==1:
#         Q.enqueue(1)
#     else :
#         Q.dequeue()
# print(Q)
