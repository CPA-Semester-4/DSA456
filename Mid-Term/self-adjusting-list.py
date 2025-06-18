class SelfAdjustingList:
    class Node:
        def __init__(self, dat, nx, pr):
            self.data = dat
            self.next = nx
            self.prev = pr

    def __init__(self):
        self.front = None
        self.back = None
    
    def push_front(self, data):
        nn = SelfAdjustingList.Node(data, self.front, None)
        if self.front == None:
            self.back = nn
        else:
            self.front.prev = nn
        self.front = nn

    def pop_front(self):
        rm = self.front
        retVal = rm.data

        if(self.front != None):
            rm.next.prev = None
            self.front = rm.next
            rm.next = None
            del rm
        else:
            self.back = None
        
        return retVal

    def print_list(self):
        temp = self.front
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def search(self, v):
        temp = self.front
        
        # We loop until we find the data/until we reach the end
        while temp != None and temp.data != v:
            temp = temp.next

        # If there is no data in the list
        if temp == None:
            return False  # Not found

        # If there is more than one data in the list 
        if temp != self.front:
            # Detach temp
            if temp.prev != None:
                temp.prev.next = temp.next
            if temp.next != None:
                temp.next.prev = temp.prev
            else:
                # It was the last node, update self.back
                self.back = temp.prev

            # Move temp to front
            temp.next = self.front
            self.front.prev = temp
            temp.prev = None
            self.front = temp

        return True


nn = SelfAdjustingList()
nn.push_front(4)
nn.push_front(6)
nn.print_list()     # Outputs: 6, 4

nn.search(6)        # 6 is already at front, no movement

nn.print_list()     # Still: 6, 4

nn.search(4)

nn.print_list()

        