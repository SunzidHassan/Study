class HashSet:
    def __init__(self, contents = []): # a = HashSet() - __init__ will be invoked
        self.items = [None] * 10 # we'll start with list of arbitary 10 elements - it can be changed later based on load factor
        self.numItems = 0 # initially 0, it'll increase as we add elements

        for item in contents:
            self.add(item)  # we'll define add function later - hashing, linear probing, rehashing... in modular parts


    def __add(item, items): #helper/private function - this add function will be a private/intenral function - won't be used outside of the class
        idx = hash(item) % len(items) # get a non-ridiculous hash > now we'll have to detect collision and do linear probing

        loc = -1 # check for collision case, not a storage location

        # in the while loop we'll update location by linear probing
        while items[idx] != None: #initially it'll be None, if there is already data there we'll have to do linear probing
            if items[idx] == item: #if it's duplicate, discard
                return False
            
            if (loc < 0) and (type(items[idx]) == HashSet.__Placeholder):
                loc = idx

            idx = (idx + 1) % len(items) # continue the while loop
        
        if loc < 0:
            loc = idx

        items[loc] = item

        return True
    
    # in order to keep constant time, we need to keep quarter of the list empty. if the length of list changes, the indeces will change, and we'll have to rehash the indices

    def __rehash(oldList, newList): # we'll take the old and new list
        for x in oldList: # for every elements in our old list
            if (x != None) and (type(x) != HashSet.__Placeholder):
                HashSet.__add(x, newList)
        return newList
    
    def add(self, item):
        if HashSet.__add(item, self.items): # check if an unique element was added to the lsit. If it returns false, we just move on, otherwise we check load factor
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items, [None]*2*len(self.items)) # returns new empty list twice the length of old list

    # Removing or discarding elements - we can add None before a None, but not in the middle of a chain - and add placeholder instead
    # iterate over items to find value, check if it's the next element is None, replace with None or Placeholder


    class __Placeholder:
        def __init__(self): # defining constructors for objects
            pass

        def __eq__(self, other):
            return False
        
    def __remove(item, items): # since it's a private function, we won't have to call self
        # where is the item located - hashing and linear probing
        idx = hash(item) % len(items)

        while items[idx] != None: # if items under that hash is not None
            if items[idx] == item: # if item equals to  item
                nextIdx = (idx + 1) % len(items)

                if items[nextIdx] == None: # if the next element is None, then we're at the end of the list
                    items[idx] = None # set to None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True
            idx = (idx+1) %len(items)
        return False
    
    def remove(self, item):
        if HashSet.__remove(item, self.items): # check if we have removed item from the list self.items is True
            self.numItems -= 1

            load = max(self.numItems, 10) / len(self.items) # we'll not shrink list beyond 10
            
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None] * len(self.items)//2)

        else: # __remove returned False as the value is not in the list
            raise KeyError("Item: {} not in HashSet".format(item))

    def discard(self, item): # without the key error
        if HashSet.__remove(item, self.items): # check if we have removed item from the list self.items is True
            self.numItems -= 1

            load = max(self.numItems, 10) / len(self.items) # we'll not shrink list beyond 10
            
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None] * len(self.items)//2)

    # for item in HashSet #we'll overwrite the in with a magic function
    def __contains__(self, item): # we'll check if an item is in the HashSet - hash it, iterate over chain - return T/F. It's a magic function so it will be invoked auto. But it's not private function (it takes self), and can be called outside function.
        idx = hash(item) %  len(self.item)

        while self.items[idx] != None:
            if self.items[idx] == None:
                return None
            idx = (idx + 1) % len(self.items)
        return False

    # for item in HashSet (ignoring None and Placeholders)
    def __iter__(self):
        for i in range(len(self.items)):
            if(self.items[i] != None) and (type(self.item[i] != HashSet.__Placeholder)):
                yield.self.items[i] # yield is like return, but it doesn't halt the for loop

    # HashSet A = {}

    def difference_update(self, other): # A = A - B / A.difference_update(B) -> A= = self, B = other
        for item in other: # based on the iter and contains
            self.discard(item)
        
    def difference(self, other): # C = A - B / C = A.difference(B) -> A = self, B = other
        result = HashSet(self)
        result.difference_update(other)
        return result

    def issuperset(self, other): # if every element of other contained in other
        for item in other:
            if item not in self:
                return False
        return True
    
    def clear(self): # delete all elements of cell
        self.numItems = 0
        self.items = [None] * 10

    def update(self, other):
        for item in other:
            self.add(item)

    # len(HashSet())
    def __len__(self):
        return self.numItems