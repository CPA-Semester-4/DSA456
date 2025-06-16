class Sentinal:
    class Node:
        def __init__(self, data = None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.front = Sentinal.Node()
        self.back = Sentinal.Node(None, None, self.front)
        self.front.next = self.back

    def push_front(self, data):
        nn = Sentinal.Node(data, self.front.next, self.front)
        self.front.next.prev = nn
        self.front.next = nn

    def pop_front(self):
        if self.front.next != self.back:
            rm = self.front.next
            retVal = rm.data

            # self.front.next = rm.next
            # rm.next.prev = self.front

            rm.next.prev = rm.prev
            rm.prev.next = rm.next
            
            del rm

            return retVal
    
    def pop_back(self):
        if self.front.next != self.back:
            rm = self.back.prev
            retVal = rm.data

            rm.prev.next = rm.next
            rm.next.prev = rm.prev
            del rm

            return retVal
        
    def push_back(self, data):
        nn = Sentinal.Node(data, self.back, None)
        nn.prev = self.back.prev
        self.back.prev.next = nn
        self.back.prev = nn


sn = Sentinal()
sn.push_front(3)
sn.push_front(2)
sn.push_front(1)
sn.push_front(0)
sn.push_back(12)
print(sn.pop_front())
print(sn.pop_front())
print(sn.pop_back())
print(sn.pop_back())
