class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = []
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key in [x[0] for x in self.hashMap]:
            for index, key1 in enumerate(self.hashMap):
                if key1[0] == key:
                    save_index = index
                    self.hashMap[save_index] = [key, value]
                    break
        else:
            self.hashMap.append([key, value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in [x[0] for x in self.hashMap]:
            for key1, value1 in self.hashMap:
                if key == key1:
                    return value1
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        save_index = 0
        
        for index, key1 in enumerate(self.hashMap):
            if key1[0] == key:
                save_index = index
                
                self.hashMap.pop(save_index)
                break
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
