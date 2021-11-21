class GetSet(object):
    def __init__(self,value):
        self.attrval = None
        self.var2 = None

    @property
    def var(self):
        print('getting the var')
        return self.attrval

    @var.setter
    def var(self,value):
        print('settin value')
        self.attrval = value

    @var.deleter
    def var(self):
        print('deleting value')
        self.attrval = None

    @var.getter
    def var(self):
        print('returning thru getter')
        return self.attrval

    @property
    def vara(self):
        print('getting the var')
        return self.var2

    @vara.setter
    def vara(self,value):
        print('settin value')
        if isinstance(value,int):
            self.var2 = value
        else:
            self.var2 = None

num = GetSet(1)
