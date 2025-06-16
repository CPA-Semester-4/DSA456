class LinkedList:
    class Node:
        def __init__(self, data, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.front = None
        self.back = None

    def push_front(self, data):
        nn = self.Node(data, self.front)
        self.front = nn
        if self.back == None:
            self.back = nn
        else:
            nn.next.prev = nn

    def pop_front(self):
        if self.front == None:
            raise IndexError('pop_front() used on empty list')
        
        rm = self.front
        rc = self.front.data
        self.front = self.front.next
        self.front.prev = None
        rm.next = None
        return rc

    def print(self):
        curr = self.front
        while(curr != None):
            print(curr.data)
            curr = curr.next

    def push_back(self, data):
        nn = LinkedList.Node(data, None, self.back)
        if self.back == None:
            self.front = nn
        else:
            self.back.next = nn
        self.back = nn
    
    def pop_back(self):
        rm = self.back
        retVal = rm.data
        self.back = self.back.prev

        if self.back == None:
            self.front = None
        else:
            self.back.next = None
        del rm
        return retVal
    
    def rev_print(self):
        curr = self.back
        while(curr != None):
            print(curr.data)
            curr = curr.prev

my_list = LinkedList()
my_list.push_front(5)
my_list.push_front(10)
my_list.push_front(7)
my_list.print()
my_list.rev_print()
my_list.pop_front()