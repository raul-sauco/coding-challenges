# Neetcode categorized list of problems

One of the best resources to get started with algorithms and data structures problems is the [neetcode list][neetcode].

The list is an extension of the Blind 75 list with an extra 75 problems, for a total of 150, that results in a more beginner-friendly list and covers the topics more in depth.

From their website:

> The Blind 75 is a popular list of Algorithm practice problems. I created the Neetcode 150 by adding 75 more problems to make a more beginner friendly and more comprehensive list.
>
> Get stuck? I've created a thorough 🎥 video explanation for each problem.

- [Neetcode categorized list of problems](#neetcode-categorized-list-of-problems)
  - [Arrays & Hashing](#arrays--hashing)
  - [Two Pointers](#two-pointers)
  - [Sliding Window](#sliding-window)
  - [Stack](#stack)
  - [Binary Search](#binary-search)
  - [Linked List](#linked-list)
  - [Trees](#trees)
  - [Tries](#tries)
  - [Heap / Priority Queue](#heap--priority-queue)
  - [Backtracking](#backtracking)
  - [Graphs](#graphs)
  - [Advanced Graphs](#advanced-graphs)
  - [1-D Dynamic Programming](#1-d-dynamic-programming)
  - [2-D Dynamic Programming](#2-d-dynamic-programming)
  - [Greedy](#greedy)
  - [Intervals](#intervals)
  - [Math & Geometry](#math--geometry)
  - [Bit Manipulation](#bit-manipulation)

## Arrays & Hashing

|     | B75 | Level     | Problem                                    | Solutions                              |
| :-: | --- | --------- | ------------------------------------------ | -------------------------------------- |
| ✅  | ⭐  | 🟢 Easy   | [217. Contains Duplicate][lc217]           | [![python](../../res/py.png)][lc217py] |
| ✅  | ⭐  | 🟢 Easy   | [242. Valid Anagram][lc242]                | [![python](../../res/py.png)][lc242py] |
| ✅  | ⭐  | 🟢 Easy   | [1. Two Sum][lc1]                          | [![python](../../res/py.png)][lc1py]   |
| ✅  | ⭐  | 🟠 Medium | [49. Group Anagrams][lc49]                 | [![python](../../res/py.png)][lc49py]  |
| ✅  | ⭐  | 🟠 Medium | [347. Top K Frequent Elements][lc347]      | [![python](../../res/py.png)][lc347py] |
| ✅  | ⭐  | 🟠 Medium | [238. Product of Array Except Self][lc238] | [![python](../../res/py.png)][lc238py] |
|     |     | 🟠 Medium | [36. Valid Sudoku][lc36]                   |                                        |
|     | ⭐  | 🟠 Medium | [271. Encode and Decode Strings][lc271]    |                                        |
| ✅  | ⭐  | 🟠 Medium | [128. Longest Consecutive Sequence][lc128] | [![python](../../res/py.png)][lc128py] |

[lc217]: https://leetcode.com/problems/contains-duplicate/
[lc217py]: ../contains-duplicate.py
[lc242]: https://leetcode.com/problems/valid-anagram/
[lc242py]: ../valid-anagram.py
[lc1]: https://leetcode.com/problems/two-sum/
[lc1py]: ../two-sum.py
[lc49]: https://leetcode.com/problems/group-anagrams/
[lc49py]: ../group-anagrams.py
[lc347]: https://leetcode.com/problems/top-k-frequent-elements/
[lc347py]: ../top-k-frequent-elements.py
[lc238]: https://leetcode.com/problems/product-of-array-except-self/
[lc238py]: ../product-of-array-except-self.py
[lc36]: https://leetcode.com/problems/valid-sudoku/
[lc271]: https://leetcode.com/problems/encode-and-decode-strings/
[lc128]: https://leetcode.com/problems/longest-consecutive-sequence/
[lc128py]: ../longest-consecutive-sequence.py

## Two Pointers

|     | B75 | Level     | Problem                                          | Solutions                              |
| :-: | --- | --------- | ------------------------------------------------ | -------------------------------------- |
| ✅  | ⭐  | 🟢 Easy   | [125. Valid Palindrome][lc125]                   | [![python](../../res/py.png)][lc125py] |
| ✅  |     | 🟠 Medium | [167. Two Sum II - Input Array Is Sorted][lc167] | [![python](../../res/py.png)][lc167py] |
|     | ⭐  | 🟠 Medium | [15. 3Sum][lc15]                                 |                                        |
|     | ⭐  | 🟠 Medium | [11. Container With Most Water][lc11]            |                                        |
| ✅  |     | 🔴 Hard   | [42. Trapping Rain Water][lc42]                  | [![python](../../res/py.png)][lc42py]  |

[lc125]: https://leetcode.com/problems/valid-palindrome/
[lc125py]: ../valid-palindrome.py
[lc167]: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
[lc167py]: ../two-sum-ii-input-array-is-sorted.py
[lc15]: https://leetcode.com/problems/3sum/
[lc11]: https://leetcode.com/problems/container-with-most-water/
[lc42]: https://leetcode.com/problems/trapping-rain-water/
[lc42py]: ../trapping-rain-water.py

## Sliding Window

|     | B75 | Level     | Problem                                                  | Solutions                              |
| :-: | --- | --------- | -------------------------------------------------------- | -------------------------------------- |
| ✅  | ⭐  | 🟢 Easy   | [121. Best Time to Buy and Sell Stock][lc121]            | [![python](../../res/py.png)][lc121py] |
| ✅  | ⭐  | 🟠 Medium | [3. Longest Substring Without Repeating Characters][lc3] | [![python](../../res/py.png)][lc3py]   |
| ✅  | ⭐  | 🟠 Medium | [424. Longest Repeating Character Replacement][lc424]    | [![python](../../res/py.png)][lc424py] |
| ✅  |     | 🟠 Medium | [567. Permutation in String][lc567]                      | [![python](../../res/py.png)][lc567py] |
|     | ⭐  | 🔴 Hard   | [76. Minimum Window Substring][lc76]                     |                                        |
| ✅  |     | 🔴 Hard   | [239. Sliding Window Maximum][lc239]                     | [![python](../../res/py.png)][lc239py] |

[lc121]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
[lc121py]: ../best-time-to-buy-and-sell-stock.py
[lc3]: https://leetcode.com/problems/longest-substring-without-repeating-characters/
[lc3py]: ../longest-substring-without-repeating-characters.py
[lc424]: https://leetcode.com/problems/longest-repeating-character-replacement/
[lc424py]: ../longest-repeating-character-replacement.py
[lc567]: https://leetcode.com/problems/permutation-in-string/
[lc567py]: ../permutation-in-string.py
[lc76]: https://leetcode.com/problems/minimum-window-substring/
[lc239]: https://leetcode.com/problems/sliding-window-maximum/
[lc239py]: ../sliding-window-maximum.py

## Stack

## Binary Search

## Linked List

|     | B75 | Level     | Problem                                      | Solutions                              |
| :-: | --- | --------- | -------------------------------------------- | -------------------------------------- |
| ✅  | ⭐  | 🟢 Easy   | [206. Reverse Linked List][lc206]            | [![python](../../res/py.png)][lc206py] |
| ✅  | ⭐  | 🟢 Easy   | [21. Merge Two Sorted Lists][lc21]           | [![python](../../res/py.png)][lc21py]  |
| ✅  | ⭐  | 🟠 Medium | [143. Reorder List][lc143]                   | [![python](../../res/py.png)][lc143py] |
| ✅  | ⭐  | 🟠 Medium | [19. Remove Nth Node From End of List][lc19] | [![python](../../res/py.png)][lc19py]  |
|     |     | 🟠 Medium | [138. Copy List with Random Pointer][lc138]  |                                        |
|     |     | 🟠 Medium | [2. Add Two Numbers][lc2]                    |                                        |
| ✅  | ⭐  | 🟢 Easy   | [141. Linked List Cycle][lc141]              | [![python](../../res/py.png)][lc141py] |
|     |     | 🟠 Medium | [287. Find the Duplicate Number][lc287]      |                                        |
|     |     | 🟠 Medium | [146. LRU Cache][lc146]                      |                                        |
|     | ⭐  | 🔴 Hard   | [23. Merge k Sorted Lists][lc23]             |                                        |
|     |     | 🔴 Hard   | [25. Reverse Nodes in k-Group][lc25]         |                                        |

[lc206]: https://leetcode.com/problems/reverse-linked-list/
[lc206py]: ../reverse-linked-list.py
[lc21]: https://leetcode.com/problems/reverse-linked-list/
[lc21py]: ../merge-two-sorted-lists.py
[lc143]: https://leetcode.com/problems/reorder-list/
[lc143py]: ../reorder-list.py
[lc19]: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
[lc19py]: ../remove-nth-node-from-end-of-list.py
[lc138]: https://leetcode.com/problems/copy-list-with-random-pointer/
[lc2]: https://leetcode.com/problems/add-two-numbers/
[lc141]: https://leetcode.com/problems/linked-list-cycle/
[lc141py]: ../linked-list-cycle.py
[lc287]: https://leetcode.com/problems/find-the-duplicate-number/
[lc146]: https://leetcode.com/problems/lru-cache/
[lc23]: https://leetcode.com/problems/merge-k-sorted-lists/
[lc25]: https://leetcode.com/problems/reverse-nodes-in-k-group/

## Trees

|     | B75 | Level     | Problem                                                                 | Solutions                              |
| :-: | --- | --------- | ----------------------------------------------------------------------- | -------------------------------------- |
| ✅  | ⭐  | 🟢 Easy   | [226. Invert Binary Tree][lc226]                                        | [![python](../../res/py.png)][lc226py] |
| ✅  | ⭐  | 🟢 Easy   | [104. Maximum Depth of Binary Tree][lc104]                              | [![python](../../res/py.png)][lc104py] |
| ✅  |     | 🟢 Easy   | [543. Diameter of Binary Tree][lc543]                                   | [![python](../../res/py.png)][lc543py] |
| ✅  |     | 🟢 Easy   | [110. Balanced Binary Tree][lc110]                                      | [![python](../../res/py.png)][lc110py] |
| ✅  | ⭐  | 🟢 Easy   | [100. Same Tree][lc100]                                                 | [![python](../../res/py.png)][lc100py] |
| ✅  | ⭐  | 🟢 Easy   | [572. Subtree of Another Tree][lc572]                                   | [![python](../../res/py.png)][lc572py] |
| ✅  | ⭐  | 🟢 Easy   | [235. Lowest Common Ancestor of a Binary Search Tree][lc235]            | [![python](../../res/py.png)][lc235py] |
| ✅  | ⭐  | 🟠 Medium | [102. Binary Tree Level Order Traversal][lc102]                         | [![python](../../res/py.png)][lc102py] |
| ✅  |     | 🟠 Medium | [199. Binary Tree Right Side View][lc199]                               | [![python](../../res/py.png)][lc199py] |
|     |     | 🟠 Medium | [1448. Count Good Nodes in Binary Tree][lc1448]                         |                                        |
| ✅  | ⭐  | 🟠 Medium | [98. Validate Binary Search Tree][lc98]                                 | [![python](../../res/py.png)][lc98py]  |
|     | ⭐  | 🟠 Medium | [230. Kth Smallest Element in a BST][lc230]                             |                                        |
| ✅  | ⭐  | 🟠 Medium | [105. Construct Binary Tree from Preorder and Inorder Traversal][lc105] | [![python](../../res/py.png)][lc105py] |
|     | ⭐  | 🔴 Hard   | [124. Binary Tree Maximum Path Sum][lc124]                              |                                        |
|     | ⭐  | 🔴 Hard   | [297. Serialize and Deserialize Binary Tree][lc297]                     |                                        |

[lc226]: https://leetcode.com/problems/invert-binary-tree/
[lc226py]: ../invert-binary-tree.py
[lc104]: https://leetcode.com/problems/maximum-depth-of-binary-tree/
[lc104py]: ../maximum-depth-of-binary-tree.py
[lc543]: https://leetcode.com/problems/diameter-of-binary-tree/
[lc543py]: ../diameter-of-binary-tree.py
[lc110]: https://leetcode.com/problems/balanced-binary-tree/
[lc110py]: ../balanced-binary-tree.py
[lc100]: https://leetcode.com/problems/same-tree/
[lc100py]: ../same-tree.py
[lc572]: https://leetcode.com/problems/subtree-of-another-tree/
[lc572py]: ../subtree-of-another-tree.py
[lc235]: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
[lc235py]: ../lowest-common-ancestor-of-a-binary-search-tree.py
[lc102]: https://leetcode.com/problems/binary-tree-level-order-traversal/
[lc102py]: ../binary-tree-level-order-traversal.py
[lc199]: https://leetcode.com/problems/binary-tree-right-side-view/
[lc199py]: ../binary-tree-right-side-view.py
[lc1448]: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
[lc98]: https://leetcode.com/problems/validate-binary-search-tree/
[lc98py]: ../validate-binary-search-tree.py
[lc230]: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
[lc105]: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
[lc105py]: ../construct-binary-tree-from-preorder-and-inorder-traversal.py
[lc124]: https://leetcode.com/problems/binary-tree-maximum-path-sum/
[lc297]: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

## Tries

|     | B75 | Level     | Problem                                                  | Solutions                              |
| :-: | --- | --------- | -------------------------------------------------------- | -------------------------------------- |
| ✅  | ⭐  | 🟠 Medium | [208. Implement Trie (Prefix Tree)][lc208]               | [![python](../../res/py.png)][lc208py] |
| ✅  | ⭐  | 🟠 Medium | [211. Design Add and Search Words Data Structure][lc211] | [![python](../../res/py.png)][lc211py] |
|     | ⭐  | 🔴 Hard   | [212. Word Search II][lc212]                             |                                        |

[lc208]: https://leetcode.com/problems/implement-trie-prefix-tree/
[lc208py]: ../implement-trie-prefix-tree.py
[lc211]: https://leetcode.com/problems/design-add-and-search-words-data-structure/
[lc211py]: ../design-add-and-search-words-data-structure.py
[lc212]: https://leetcode.com/problems/word-search-ii/

## Heap / Priority Queue

|     | B75 | Level     | Problem                                       | Solutions                               |
| :-: | --- | --------- | --------------------------------------------- | --------------------------------------- |
| ✅  |     | 🟢 Easy   | [703. Kth Largest Element in a Stream][lc703] | [![python](../../res/py.png)][lc703py]  |
| ✅  |     | 🟢 Easy   | [1046. Last Stone Weight][lc1046]             | [![python](../../res/py.png)][lc1046py] |
|     |     | 🟠 Medium | [973. K Closest Points to Origin][lc973]      |                                         |
| ✅  |     | 🟠 Medium | [215. Kth Largest Element in an Array][lc215] | [![python](../../res/py.png)][lc215py]  |
|     |     | 🟠 Medium | [621. Task Scheduler][lc621]                  |                                         |
|     |     | 🟠 Medium | [355. Design Twitter][lc355]                  |                                         |
|     | ⭐  | 🔴 Hard   | [295. Find Median from Data Stream][lc295]    |                                         |

[lc703]: https://leetcode.com/problems/kth-largest-element-in-a-stream/
[lc703py]: ../kth-largest-element-in-a-stream.py
[lc1046]: https://leetcode.com/problems/last-stone-weight/
[lc1046py]: ../last-stone-weight.py
[lc973]: https://leetcode.com/problems/k-closest-points-to-origin/
[lc215]: https://leetcode.com/problems/kth-largest-element-in-an-array/
[lc215py]: ../kth-largest-element-in-an-array.py
[lc621]: https://leetcode.com/problems/task-scheduler/
[lc355]: https://leetcode.com/problems/design-twitter/
[lc295]: https://leetcode.com/problems/find-median-from-data-stream/

## Backtracking

|     | B75 | Level     | Problem                                           | Solutions                             |
| :-: | --- | --------- | ------------------------------------------------- | ------------------------------------- |
|     |     | 🟠 Medium | [78. Subsets][lc78]                               |                                       |
|     |     | 🟠 Medium | [39. Combination Sum][lc39]                       |                                       |
|     |     | 🟠 Medium | [46. Permutations][lc46]                          |                                       |
|     |     | 🟠 Medium | [90. Subsets II][lc90]                            |                                       |
|     | ⭐  | 🟠 Medium | [40. Combination Sum II][lc40]                    |                                       |
|     | ⭐  | 🟠 Medium | [79. Word Search][lc79]                           |                                       |
|     |     | 🟠 Medium | [131. Palindrome Partitioning][lc131]             |                                       |
|     |     | 🟠 Medium | [17. Letter Combinations of a Phone Number][lc17] |                                       |
| ✅  |     | 🔴 Hard   | [51. N-Queens][lc51]                              | [![python](../../res/py.png)][lc51py] |

[lc78]: https://leetcode.com/problems/subsets/
[lc39]: https://leetcode.com/problems/combination-sum/
[lc46]: https://leetcode.com/problems/permutations/
[lc90]: https://leetcode.com/problems/subsets-ii/
[lc40]: https://leetcode.com/problems/combination-sum-ii/
[lc79]: https://leetcode.com/problems/word-search/
[lc131]: https://leetcode.com/problems/palindrome-partitioning/
[lc17]: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
[lc51]: https://leetcode.com/problems/n-queens/
[lc51py]: ../n-queens.py

## Graphs

|     | B75 | Level     | Problem                                                             | Solutions                              |
| :-: | --- | --------- | ------------------------------------------------------------------- | -------------------------------------- |
| ✅  | ⭐  | 🟠 Medium | [200. Number of Islands][lc200]                                     | [![python](../../res/py.png)][lc200py] |
|     | ⭐  | 🟠 Medium | [133. Clone Graph][lc133]                                           |                                        |
| ✅  |     | 🟠 Medium | [695. Max Area of Island][lc695]                                    | [![python](../../res/py.png)][lc695py] |
|     | ⭐  | 🟠 Medium | [417. Pacific Atlantic Water Flow][lc417]                           |                                        |
|     |     | 🟠 Medium | [130. Surrounded Regions][lc130]                                    |                                        |
|     |     | 🟠 Medium | [994. Rotting Oranges][lc994]                                       |                                        |
|     |     | 🟠 Medium | [286. Walls and Gates][lc286]                                       |                                        |
|     | ⭐  | 🟠 Medium | [207. Course Schedule][lc207]                                       |                                        |
|     |     | 🟠 Medium | [210. Course Schedule II][lc210]                                    |                                        |
|     |     | 🟠 Medium | [684. Redundant Connection][lc684]                                  |                                        |
|     | ⭐  | 🟠 Medium | [323. Number of Connected Components in an Undirected Graph][lc323] |                                        |
|     | ⭐  | 🟠 Medium | [261. Graph Valid Tree][lc261]                                      |                                        |
|     |     | 🔴 Hard   | [127. Word Ladder][lc127]                                           |                                        |

[lc200]: https://leetcode.com/problems/number-of-islands/
[lc200py]: ../number-of-islands.py
[lc133]: https://leetcode.com/problems/clone-graph/
[lc695]: https://leetcode.com/problems/max-area-of-island/
[lc695py]: ../max-area-of-island.py
[lc417]: https://leetcode.com/problems/pacific-atlantic-water-flow/
[lc130]: https://leetcode.com/problems/surrounded-regions/
[lc994]: https://leetcode.com/problems/rotting-oranges/
[lc286]: https://leetcode.com/problems/walls-and-gates/
[lc207]: https://leetcode.com/problems/course-schedule/
[lc210]: https://leetcode.com/problems/course-schedule-ii/
[lc684]: https://leetcode.com/problems/redundant-connection/
[lc323]: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
[lc261]: https://leetcode.com/problems/graph-valid-tree/
[lc127]: https://leetcode.com/problems/word-ladder/

## Advanced Graphs

|     | B75 | Level     | Problem                                        | Solutions |
| :-: | --- | --------- | ---------------------------------------------- | --------- |
|     |     | 🔴 Hard   | [332. Reconstruct Itinerary][lc332]            |           |
|     |     | 🟠 Medium | [1584. Min Cost to Connect All Points][lc1584] |           |
|     |     | 🟠 Medium | [743. Network Delay Time][lc743]               |           |
|     |     | 🔴 Hard   | [778. Swim in Rising Water][lc778]             |           |
|     | ⭐  | 🔴 Hard   | [269. Alien Dictionary][lc269]                 |           |
|     |     | 🟠 Medium | [787. Cheapest Flights Within K Stops][lc787]  |           |

[lc332]: https://leetcode.com/problems/reconstruct-itinerary/
[lc1584]: https://leetcode.com/problems/min-cost-to-connect-all-points/
[lc743]: https://leetcode.com/problems/network-delay-time/
[lc778]: https://leetcode.com/problems/swim-in-rising-water/
[lc269]: https://leetcode.com/problems/alien-dictionary/
[lc787]: https://leetcode.com/problems/cheapest-flights-within-k-stops/

## 1-D Dynamic Programming

|     | B75 | Level     | Problem                                      | Solutions                              |
| :-: | --- | --------- | -------------------------------------------- | -------------------------------------- |
| ✅  | ⭐  | 🟢 Easy   | [70. Climbing Stairs][lc70]                  | [![python](../../res/py.png)][lc70py]  |
| ✅  |     | 🟢 Easy   | [746. Min Cost Climbing Stairs][lc746]       | [![python](../../res/py.png)][lc746py] |
| ✅  | ⭐  | 🟠 Medium | [198. House Robber][lc198]                   | [![python](../../res/py.png)][lc198py] |
| ✅  | ⭐  | 🟠 Medium | [213. House Robber II][lc213]                | [![python](../../res/py.png)][lc213py] |
| ✅  | ⭐  | 🟠 Medium | [5. Longest Palindromic Substring][lc5]      | [![python](../../res/py.png)][lc5py]   |
|     | ⭐  | 🟠 Medium | [647. Palindromic Substrings][lc647]         |                                        |
|     | ⭐  | 🟠 Medium | [91. Decode Ways][lc91]                      |                                        |
|     | ⭐  | 🟠 Medium | [322. Coin Change][lc322]                    |                                        |
|     | ⭐  | 🟠 Medium | [152. Maximum Product Subarray][lc152]       |                                        |
|     | ⭐  | 🟠 Medium | [139. Word Break][lc139]                     |                                        |
|     | ⭐  | 🟠 Medium | [300. Longest Increasing Subsequence][lc300] |                                        |
|     |     | 🟠 Medium | [416. Partition Equal Subset Sum][lc416]     |                                        |

[lc70]: https://leetcode.com/problems/climbing-stairs/
[lc70py]: ../climbing-stairs.py
[lc746]: https://leetcode.com/problems/min-cost-climbing-stairs/submissions/
[lc746py]: ../min-cost-climbing-stairs.py
[lc198]: https://leetcode.com/problems/house-robber/
[lc198py]: ../house-robber.py
[lc213]: https://leetcode.com/problems/house-robber-ii/
[lc213py]: ../house-robber-ii.py
[lc5]: https://leetcode.com/problems/longest-palindromic-substring/
[lc5py]: ../longest-palindromic-substring.py
[lc647]: https://leetcode.com/problems/palindromic-substrings/
[lc91]: https://leetcode.com/problems/decode-ways/
[lc322]: https://leetcode.com/problems/coin-change/
[lc152]: https://leetcode.com/problems/maximum-product-subarray/
[lc139]: https://leetcode.com/problems/word-break/
[lc300]: https://leetcode.com/problems/longest-increasing-subsequence/
[lc416]: https://leetcode.com/problems/partition-equal-subset-sum/

## 2-D Dynamic Programming

## Greedy

## Intervals

|     | B75 | Level     | Problem                                                | Solutions                             |
| :-: | --- | --------- | ------------------------------------------------------ | ------------------------------------- |
| ✅  | ⭐  | 🟠 Medium | [57. Insert Interval][lc57]                            | [![python](../../res/py.png)][lc57py] |
|     | ⭐  | 🟠 Medium | [56. Merge Intervals][lc56]                            |                                       |
|     | ⭐  | 🟠 Medium | [435. Non-overlapping Intervals][lc435]                |                                       |
|     | ⭐  | 🟢 Easy   | [252. Meeting Rooms][lc252]                            |                                       |
|     | ⭐  | 🟠 Medium | [253. Meeting Rooms II][lc253]                         |                                       |
|     |     | 🔴 Hard   | [1851. Minimum Interval to Include Each Query][lc1851] |                                       |

[lc57]: https://leetcode.com/problems/insert-interval/
[lc57py]: ../insert-interval.py
[lc56]: https://leetcode.com/problems/merge-intervals/
[lc435]: https://leetcode.com/problems/non-overlapping-intervals/
[lc252]: https://leetcode.com/problems/meeting-rooms/
[lintcode920]: https://www.lintcode.com/problem/920/
[lc253]: https://leetcode.com/problems/meeting-rooms-ii/
[lintcode921]: https://www.lintcode.com/problem/921/
[lc1851]: https://leetcode.com/problems/minimum-interval-to-include-each-query/

## Math & Geometry

|     | B75 | Level     | Problem                        | Solutions                              |
| :-: | --- | --------- | ------------------------------ | -------------------------------------- |
| ✅  | ⭐  | 🟠 Medium | [48. Rotate Image][lc48]       | [![python](../../res/py.png)][lc48py]  |
| ✅  | ⭐  | 🟠 Medium | [54. Spiral Matrix][lc54]      | [![python](../../res/py.png)][lc54py]  |
| ✅  | ⭐  | 🟠 Medium | [73. Set Matrix Zeroes][lc73]  | [![python](../../res/py.png)][lc73py]  |
| ✅  |     | 🟢 Easy   | [202. Happy Number][lc202]     | [![python](../../res/py.png)][lc202py] |
| ✅  |     | 🟢 Easy   | [66. Plus One][lc66]           | [![python](../../res/py.png)][lc66py]  |
|     |     | 🟠 Medium | [50. Pow(x, n)][lc50]          |                                        |
| ✅  |     | 🟠 Medium | [43. Multiply Strings][lc43]   | [![python](../../res/py.png)][lc43py]  |
|     |     | 🟠 Medium | [2013. Detect Squares][lc2013] |                                        |

[lc48]: https://leetcode.com/problems/rotate-image/
[lc48py]: ../rotate-image.py
[lc54]: https://leetcode.com/problems/spiral-matrix/
[lc54py]: ../spiral-matrix.py
[lc73]: https://leetcode.com/problems/set-matrix-zeroes/
[lc73py]: ../set-matrix-zeroes.py
[lc202]: https://leetcode.com/problems/happy-number/
[lc202py]: ../happy-number.py
[lc66]: https://leetcode.com/problems/plus-one/
[lc66py]: ../plus-one.py
[lc50]: https://leetcode.com/problems/powx-n/
[lc43]: https://leetcode.com/problems/multiply-strings/
[lc43py]: ../multiply-strings.py
[lc2013]: https://leetcode.com/problems/detect-squares/

## Bit Manipulation

|     | B75 | Level     | Problem                           | Solutions                              |
| :-: | --- | --------- | --------------------------------- | -------------------------------------- |
| ✅  |     | 🟢 Easy   | [136. Single Number][lc136]       | [![python](../../res/py.png)][lc136py] |
| ✅  | ⭐  | 🟢 Easy   | [191. Number of 1 Bits][lc191]    | [![python](../../res/py.png)][lc191py] |
| ✅  | ⭐  | 🟢 Easy   | [338. Counting Bits][lc338]       | [![python](../../res/py.png)][lc338py] |
| ✅  | ⭐  | 🟢 Easy   | [190. Reverse Bits][lc190]        | [![python](../../res/py.png)][lc190py] |
|     | ⭐  | 🟢 Easy   | [268. Missing Number][lc268]      |                                        |
|     | ⭐  | 🟠 Medium | [371. Sum of Two Integers][lc371] |                                        |
|     |     | 🟠 Medium | [7. Reverse Integer][lc7]         |                                        |

[lc136]: https://leetcode.com/problems/single-number/
[lc136py]: ../single-number.py
[lc191]: https://leetcode.com/problems/number-of-1-bits/
[lc191py]: ../number-of-1-bits.py
[lc338]: https://leetcode.com/problems/counting-bits/
[lc338py]: ../counting-bits.py
[lc190]: https://leetcode.com/problems/reverse-bits/
[lc190py]: ../reverse-bits.py
[lc268]: https://leetcode.com/problems/missing-number/
[lc371]: https://leetcode.com/problems/sum-of-two-integers/
[lc7]: https://leetcode.com/problems/reverse-integer/
[neetcode]: https://neetcode.io
