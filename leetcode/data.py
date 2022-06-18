# Definitions for classes that get used in other files

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a trie node
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
