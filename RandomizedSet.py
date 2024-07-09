class RandomizedSet():
    def __init__(self):
        self.hm = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        self.hm[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        last_val = self.lst[-1]
        curr_index = self.hm[val]
        self.lst[curr_index] = last_val
        self.hm[last_val] = curr_index 
        self.hm.pop(val)
        self.lst.pop()
        return True


    def getRandom(self) -> int:
        import random
        random_index = random.randint(0, len(self.lst) - 1)
        return self.lst[random_index]


obj = RandomizedSet()
print(obj.insert(1)) # True
print(obj.remove(2)) # False
print(obj.insert(2)) # True
print(obj.getRandom()) # 1
print(obj.remove(1)) # True
print(obj.insert(2)) # False
print(obj.getRandom()) # 2
print(obj.insert(3)) # True
print(obj.getRandom()) # 3
print(obj.remove(2)) # True
print(obj.getRandom()) # 3
print(obj.remove(3)) # True

