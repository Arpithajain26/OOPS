class Database:
    def __init__(self):
        self.storage={}
    def write(self,key,value):
        self.storage[key]=value
        
    def read(self,key):
        if self.storage:
            print(self.storage[key])
        else:
            print("DB item is not available")
db=Database()
db.write("chandan","1")
db.read("chandan")