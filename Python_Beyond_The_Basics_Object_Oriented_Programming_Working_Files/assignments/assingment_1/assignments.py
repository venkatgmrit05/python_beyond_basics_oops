



class MaxSizeList(object):
    def __init__(self,size):
        assert isinstance(size, int),'list max size must be a number'
        self.limit = size
        self.data = []

    def push(self,item):
        if len(self.data) >= self.limit:
            self.data.pop(0)
            self.data.append(item)
        else:
            self.data.append(item)
            
    def get_list(self):
        return self.data



class MaxSizeList2(object):
    def __init__(self,size):
        assert isinstance(size, int),'list max size must be a number'
        self.limit = size
        self.data = []

    def push(self,item):
        self.data.append(item)
        if len(self.data) > self.limit:
            self.data.pop(0)
            
            
    def get_list(self):
        return self.data



