class Person():
    def insert(self,name,age,idnum):
        self.name=name
        self.age=age
        self.idnum=idnum
    def output(self):
        print("name is "+self.name+"age is "+self.age+"idnum is "+self.idnum)
j=Person()
j.insert("sai","33",12345)
j.output
