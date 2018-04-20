class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hashfunction(self, data):
        return data % self.size

    def insert(self, data):
        index = self.hashfunction(data)
        self.table[index].append(data)

    def getsize(self):
        return self.size

    def __str__(self):
        return(str(self.table))
        

a = HashTable(10)
print("Hashtable size is: ", a.getsize())
print("11 hash is: ", a.hashfunction(11))

print("Hashtable:")
print(a)

print("Inserting 9...")
a.insert(9)
print(a)

print("Inserting 10")
a.insert(10)
print(a)

print("Inserting 0")
a.insert(0)
print(a)


