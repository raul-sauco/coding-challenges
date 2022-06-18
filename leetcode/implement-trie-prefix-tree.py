# https://leetcode.com/problems/implement-trie-prefix-tree/

# Runtime: 144 ms, faster than 96.10% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 27.6 MB, less than 86.88 % of Python3 online submissions for Implement Trie(Prefix Tree).
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current['?'] = True

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            if w not in current:
                return False
            current = current[w]
        return current.get('?', False)

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            if w not in current:
                return False
            current = current[w]
        return True

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)


def test():
    trie = Trie()
    assert trie.insert('apple') == None
    assert trie.search('apple') == True
    assert trie.search('app') == False
    assert trie.startsWith('app') == True
    assert trie.insert('app') == None
    assert trie.search('app') == True
    assert trie.startsWith('ape') == False
    assert trie.insert('ape') == None
    assert trie.search('ape') == True


test()
