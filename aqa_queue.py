
class Queue:

    def __init__(self):
        self.__front = 0
        self.__rear = -1
        self.__size = 0
        self.__maxSize = 10
        self.__data = [None for _ in range(self.__maxSize)]

    def _isEmpty(self):
        if self.__size == 0:
            return True
        else:
            return False
    
    def _isFull(self):
        if self.__size == self.__maxSize:
            return True
        else:
            return False
        
    def _enqueue(self, newItem):
        if self._isFull():
            raise Exception("Queue is full")
        else:
            self.__rear = (self.__rear + 1) % self.__maxSize
            self.__data[self.__rear] = newItem
            self.__size += 1

        
    def _dequeue(self):
        if self._isEmpty():
            raise Exception("Queue is empty")
            item = None
        else:
            item = self.__data[self.__front]
            self.__front = (self.__front + 1) % self.__maxSize
            self.__size -= 1

        return item
    


q = Queue()

print("Test q empty error")
try:
    q._dequeue()
except Exception as e:
    print(e)

print("Test enqueue")
for i in range(10):
    q._enqueue(chr(i+65) * 5)

print("Test q full error")
try:
    q._enqueue("zzz")
except Exception as e:
    print(e)

print("Test dequeue")
print(q._dequeue())


