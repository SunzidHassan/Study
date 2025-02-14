import sys                                              # import library (e.g., for read functionalityy)

class Trie:                                             # define Trie class
    def __init__(self):                                 # define instance variables
        self.start = None                               # instance variable of Trie class

    class TrieNode:                                     # define TrieNode class
        def __init__(self, item, next = None, follows = None):  # define instance variables
            self.item = item                            # instance variable of TrieNode - item
            self.next = next                            # instance variable of TrieNode - next
            self.follows = follows                      # instance variable of TrieNode - follows

    def __insert(node, key):                            # insert keys in dictionary
        if len(key) == 0:                               # return None if empty key
            return None

        if node == None:                                # if node is None, create a new node with unit of the key
            return Trie.TrieNode(key[0], None, Trie.__insert(None, key[1:]))

        if key[0] == node.item[0]:                      # if first unit matches, insert rest of the key into follows link of current node
            node.follows = Trie.__insert(node.follows, key[1:])
            return node
        
        node.next = Trie.__insert(node.next, key)       # otherwise, insert key into next link of current node
        return node
    
    def insert(self, key):                              # insert function
        self.start = Trie.__insert(self.start, key+"$")

    def __contains(node, key):
        
        ### WRITE YOUR CODE HERE###
        if len(key) == 0:                               # if key length is 0, it means the word is in the dictionary
            return True

        if node == None:                                # if node is None, the word isn't in the dictionary
            return False

        if key[0] == node.item[0]:                      # If first unit of key matches unit of current node
            return Trie.__contains(node.follows, key[1:]) # Check membership of rest of the key starting with follows node
        
        return Trie.__contains(node.next, key)          # Otherwise, check membership of key starting with next node
        
    def __contains__(self, key):                        # method for contain check
        return Trie.__contains(self.start, key+"$")

    def __str(node, indent):                            # printing string
        if node == None:                                # avoid printing None
            return ""
        return f"\n{indent}{str(node.item)}{Trie.__str(node.follows, indent + ' ')}{Trie.__str(node.next, indent)}"     # string representation

    def __str__(self):                                  # string representation
        return Trie.__str(self.start, "")

def main():
    words = open(sys.argv[1], "r")                      # open dictionary
    trie = Trie()                                       # initiate variable
    for line in words:                                  # take lines in the dictionary
        word = line.strip()                             # strip whitespaces and insert words in trie
        trie.insert(word)                               # insert them in trie        
    text = open(sys.argv[2], "r")                       # open the test file
    print("Misspelled words:")
    for line in text:                                   # get lines in the text file
        for word in line.split():                       # get words in the lines
            word = word.lower().strip(',').strip('.')   # trim white spaces, lower them, eliminate ',' and '.'
    ### WRITE YOUR CODE HERE###
            if word not in trie:                        # print misspelled words 
                print(" ", word)

main()

