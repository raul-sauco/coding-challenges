# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from data import TrieNode


# Easier to read version of the word dictionary that uses TriedNode as a node
# Runtime: 16930 ms, faster than 27.61% of Python3 online submissions for Design Add and Search Words Data Structure.
# Memory Usage: 80 MB, less than 12.93 % of Python3 online submissions for Design Add and Search Words Data Structure.
class WordDictionaryEasyRead:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        # Recursively add the nodes
        for w in word:
            current = current.children[w]
        # Mark the last character of the word as the end of a word
        current.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node, word) -> bool:
            # If our query string is longer than this branch of the exploration, return False
            if node:
                # If we have exhausted the characters in the search word, exit
                # Return True if we are at a word, False otherwise
                # False returns will be ignored by the caller
                if len(word) == 0:
                    if node.isWord:
                        return True

                # If we have not exhausted all the characters
                else:
                    # We still have characters to explore in word
                    if word[0] == '.':
                        for n in node.children.values():
                            if dfs(n, word[1:]):
                                return True
                    else:
                        node = node.children.get(word[0])
                        if node and dfs(node, word[1:]):
                            return True

        res = dfs(self.root, word)  # True or None
        return res if res else False


def testEasyRead():
    wd = WordDictionaryEasyRead()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") == False
    assert wd.search("bad") == True
    assert wd.search(".ad") == True
    assert wd.search("b..") == True
    assert wd.search("..d") == True
    assert wd.search("..e") == False
    assert wd.search("...") == True
    assert wd.search("bade") == False
    assert wd.search("....") == False
    assert wd.search(".") == False


testEasyRead()


# Runtime: 16919 ms, faster than 27.72% of Python3 online submissions for Design Add and Search Words Data Structure.
# Memory Usage: 55.9 MB, less than 87.04 % of Python3 online submissions for Design Add and Search Words Data Structure.
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current = self.root
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current['?'] = True

    def search(self, word: str) -> bool:
        def searchFromNode(index, node) -> bool:
            current = node
            for i in range(index, len(word)):
                w = word[i]
                # Handle wildcards
                if w == '.':
                    # Recursive call to all the children with the sliced word
                    for key, child in current.items():
                        if key != "?" and searchFromNode(i+1, child):
                            return True
                    return False
                else:
                    if w not in current:
                        return False
                    current = current[w]
            return current.get('?', False)

        return searchFromNode(0, self.root)

        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)


def test():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") == False
    assert wd.search("bad") == True
    assert wd.search(".ad") == True
    assert wd.search("b..") == True
    assert wd.search("..d") == True
    assert wd.search("..e") == False
    assert wd.search("...") == True
    assert wd.search("bade") == False
    assert wd.search("....") == False


test()
