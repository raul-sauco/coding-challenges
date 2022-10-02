# List of Dynamic Programming Problems

A list of dynamic programming problems organized into the following categories:

- [List of Dynamic Programming Problems](#list-of-dynamic-programming-problems)
  - [1. Linear DP](#1-linear-dp)
  - [2. Knapsack](#2-knapsack)
  - [3. Multi Dimensions DP](#3-multi-dimensions-dp)
  - [4. Interval DP](#4-interval-dp)
  - [5. bit DP](#5-bit-dp)
  - [6. Digit DP](#6-digit-dp)
  - [7. DP on Trees](#7-dp-on-trees)
  - [8. String DP](#8-string-dp)
  - [9. Probability DP](#9-probability-dp)
  - [10. Classic DPs](#10-classic-dps)
    - [A. Kadane's Algorithm](#a-kadanes-algorithm)
    - [B. LCS](#b-lcs)
    - [C. LIS](#c-lis)
    - [D. 2D Grid Traversal](#d-2d-grid-traversal)
    - [E. Cumulative Sum](#e-cumulative-sum)
    - [F. Hashmap (SubArray)](#f-hashmap-subarray)
  - [11. DP + Alpha (Tricks/DS)](#11-dp--alpha-tricksds)
  - [12. Insertion DP](#12-insertion-dp)
  - [13. Graph DP](#13-graph-dp)
  - [14. Memoization](#14-memoization)
  - [15. Binary Lifting](#15-binary-lifting)
  - [16. Math](#16-math)
  - [Related reading](#related-reading)

If you clone the repository and want to track your own progress, use search
and replace to remove all the progress icons, like ✅ and ❌, and start
tracking your own progress.

## 1. Linear DP

|     | Level     | Name                                                                   | Solutions                              |
| :-: | --------- | ---------------------------------------------------------------------- | -------------------------------------- |
| ✅  | 🟢 Easy   | [70. Climbing Stairs][lc70]                                            | [![python](../../res/py.png)][lc70py]  |
| ✅  | 🟢 Easy   | [121. Best Time to Buy and Sell Stock][lc121]                          | [![python](../../res/py.png)][lc121py] |
| ✅  | 🟢 Easy   | [338. Counting Bits][lc338]                                            | [![python](../../res/py.png)][lc338py] |
| ✅  | 🟢 Easy   | [746. Min Cost Climbing Stairs][lc746]                                 | [![python](../../res/py.png)][lc746py] |
|     | 🟢 Easy   | [1025. Divisor Game][lc1025]                                           |                                        |
| ✅  | 🟠 Medium | [91. Decode Ways][lc91]                                                | [![python](../../res/py.png)][lc91py]  |
|     | 🟠 Medium | [96. Unique Binary Search Trees][lc96]                                 |                                        |
| ✅  | 🟠 Medium | [198. House Robber][lc198]                                             | [![python](../../res/py.png)][lc198py] |
|     | 🟠 Medium | [279. Perfect Squares][lc279]                                          |                                        |
|     | 🟠 Medium | [309. Best Time to Buy and Sell Stock with Cooldown][lc309]            |                                        |
| ✅  | 🟠 Medium | [322. Coin Change][lc322]                                              | [![python](../../res/py.png)][lc322py] |
|     | 🟠 Medium | [343. Integer Break][lc343]                                            |                                        |
|     | 🟠 Medium | [357. Count Numbers with Unique Digits][lc357]                         |                                        |
| ✅  | 🟠 Medium | [376. Wiggle Subsequence][lc376]                                       | [![python](../../res/py.png)][lc376py] |
| ✅  | 🟠 Medium | [416. Partition Equal Subset Sum][lc416]                               | [![python](../../res/py.png)][lc416py] |
|     | 🟠 Medium | [518. Coin Change 2][lc518]                                            |                                        |
|     | 🟠 Medium | [646. Maximum Length of Pair Chain][lc646]                             |                                        |
|     | 🟠 Medium | [714. Best Time to Buy and Sell Stock with Transaction Fee][lc714]     |                                        |
|     | 🟠 Medium | [740. Delete and Earn][lc740]                                          |                                        |
|     | 🟠 Medium | [790. Domino and Tromino Tiling][lc790]                                |                                        |
|     | 🟠 Medium | [935. Knight Dialer][lc935]                                            |                                        |
|     | 🟠 Medium | [983. Minimum Cost For Tickets][lc983]                                 |                                        |
|     | 🟠 Medium | [1043. Partition Array for Maximum Sum][lc1043]                        |                                        |
|     | 🟠 Medium | [1105. Filling Bookcase Shelves][lc1105]                               |                                        |
|     | 🟠 Medium | [1218. Longest Arithmetic Subsequence of Given Difference][lc1218]     |                                        |
|     | 🟠 Medium | [1262. Greatest Sum Divisible by Three][lc1262]                        |                                        |
|     | 🔴 Hard   | [123. Best Time to Buy and Sell Stock III][lc123]                      |                                        |
|     | 🔴 Hard   | [552. Student Attendance Record II][lc552]                             |                                        |
|     | 🔴 Hard   | [639. Decode Ways II][lc639]                                           |                                        |
|     | 🔴 Hard   | [982. Triples with Bitwise AND Equal To Zero][lc982]                   |                                        |
|     | 🔴 Hard   | [1235. Maximum Profit in Job Scheduling][lc1235]                       |                                        |
|     | 🔴 Hard   | [1326. Minimum Number of Taps to Open to Water a Garden][lc1326]       |                                        |
|     | 🔴 Hard   | [1359. Count All Valid Pickup and Delivery Options][lc1359]            |                                        |
|     | 🔴 Hard   | [1406. Stone Game III][lc1406]                                         |                                        |
|     | 🔴 Hard   | [1416. Restore The Array][lc1416]                                      |                                        |
|     | 🔴 Hard   | [1449. Form Largest Integer With Digits That Add up to Target][lc1449] |                                        |
|     | 🔴 Hard   | [1510. Stone Game IV][lc1510]                                          |                                        |

[lc70]: https://leetcode.com/problems/climbing-stairs/
[lc70py]: ../climbing-stairs.py
[lc121]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
[lc121py]: ../best-time-to-buy-and-sell-stock.py
[lc338]: https://leetcode.com/problems/counting-bits/
[lc338py]: ../counting-bits.py
[lc746]: https://leetcode.com/problems/min-cost-climbing-stairs/
[lc746py]: ../min-cost-climbing-stairs.py
[lc1025]: https://leetcode.com/problems/divisor-game/
[lc91]: https://leetcode.com/problems/decode-ways/
[lc91py]: ../decode-ways.py
[lc96]: https://leetcode.com/problems/unique-binary-search-trees/
[lc198]: https://leetcode.com/problems/house-robber/
[lc198py]: ../house-robber.py
[lc279]: https://leetcode.com/problems/perfect-squares/
[lc309]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
[lc322]: https://leetcode.com/problems/coin-change/
[lc322py]: ../coin-change.py
[lc343]: https://leetcode.com/problems/integer-break/
[lc357]: https://leetcode.com/problems/count-numbers-with-unique-digits/
[lc376]: https://leetcode.com/problems/wiggle-subsequence/
[lc376py]: ../wiggle-subsequence.py
[lc416]: https://leetcode.com/problems/partition-equal-subset-sum/
[lc416py]: ../partition-equal-subset-sum.py
[lc518]: https://leetcode.com/problems/coin-change-2/
[lc646]: https://leetcode.com/problems/maximum-length-of-pair-chain/
[lc714]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
[lc740]: https://leetcode.com/problems/delete-and-earn/
[lc790]: https://leetcode.com/problems/domino-and-tromino-tiling/
[lc935]: https://leetcode.com/problems/knight-dialer/
[lc983]: https://leetcode.com/problems/minimum-cost-for-tickets/
[lc1043]: https://leetcode.com/problems/partition-array-for-maximum-sum/
[lc1105]: https://leetcode.com/problems/filling-bookcase-shelves/
[lc1218]: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
[lc1262]: https://leetcode.com/problems/greatest-sum-divisible-by-three/
[lc123]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
[lc552]: https://leetcode.com/problems/student-attendance-record-ii/
[lc639]: https://leetcode.com/problems/decode-ways-ii/
[lc982]: https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
[lc1235]: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
[lc1326]: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
[lc1359]: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
[lc1406]: https://leetcode.com/problems/stone-game-iii/
[lc1416]: https://leetcode.com/problems/restore-the-array/
[lc1449]: https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/
[lc1510]: https://leetcode.com/problems/stone-game-iv/

## 2. Knapsack

|     | Level     | Name                                                     | Solutions                              |
| :-: | --------- | -------------------------------------------------------- | -------------------------------------- |
| ✅  | 🟠 Medium | [213. House Robber II][lc213]                            | [![python](../../res/py.png)][lc213py] |
|     | 🟠 Medium | [474. Ones and Zeroes][lc474]                            |                                        |
|     | 🟠 Medium | [494. Target Sum][lc494]                                 |                                        |
|     | 🟠 Medium | [638. Shopping Offers][lc638]                            |                                        |
|     | 🟠 Medium | [650. 2 Keys Keyboard][lc650]                            |                                        |
|     | 🟠 Medium | [1626. Best Team With No Conflicts][lc1626]              |                                        |
|     | 🔴 Hard   | [801. Minimum Swaps To Make Sequences Increasing][lc801] |                                        |
|     | 🔴 Hard   | [879. Profitable Schemes][lc879]                         |                                        |
|     | 🔴 Hard   | [956. Tallest Billboard][lc956]                          |                                        |
|     | 🔴 Hard   | [1388. Pizza With 3n Slices][lc1388]                     |                                        |
|     | 🔴 Hard   | [1402. Reducing Dishes][lc1402]                          |                                        |

[lc213]: https://leetcode.com/problems/house-robber-ii/
[lc213py]: ../house-robber-ii.py
[lc474]: https://leetcode.com/problems/ones-and-zeroes/
[lc494]: https://leetcode.com/problems/target-sum/
[lc638]: https://leetcode.com/problems/shopping-offers/
[lc650]: https://leetcode.com/problems/2-keys-keyboard/
[lc1626]: https://leetcode.com/problems/best-team-with-no-conflicts/
[lc801]: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
[lc879]: https://leetcode.com/problems/profitable-schemes/
[lc956]: https://leetcode.com/problems/tallest-billboard/
[lc1388]: https://leetcode.com/problems/pizza-with-3n-slices/
[lc1402]: https://leetcode.com/problems/reducing-dishes/

## 3. Multi Dimensions DP

|     | Level     | Name                                                                             | Solutions                               |
| :-: | --------- | -------------------------------------------------------------------------------- | --------------------------------------- |
| ✅  | 🟢 Easy   | [120. Triangle][lc120]                                                           | [![python](../../res/py.png)][lc120py]  |
| ✅  | 🟠 Medium | [377. Combination Sum IV][lc377]                                                 | [![python](../../res/py.png)][lc377py]  |
| ✅  | 🟠 Medium | [576. Out of Boundary Paths][lc576]                                              | [![python](../../res/py.png)][lc576py]  |
|     | 🟠 Medium | [688. Knight Probability in Chessboard][lc688]                                   |                                         |
|     | 🟠 Medium | [799. Champagne Tower][lc799]                                                    |                                         |
|     | 🟠 Medium | [813. Largest Sum of Averages][lc813]                                            |                                         |
|     | 🟠 Medium | [931. Minimum Falling Path Sum][lc931]                                           |                                         |
|     | 🟠 Medium | [1024. Video Stitching][lc1024]                                                  |                                         |
|     | 🟠 Medium | [1027. Longest Arithmetic Subsequence][lc1027]                                   |                                         |
|     | 🟠 Medium | [1140. Stone Game II][lc1140]                                                    |                                         |
| ✅  | 🟠 Medium | [1155. Number of Dice Rolls With Target Sum][lc1155]                             | [![python](../../res/py.png)][lc1155py] |
|     | 🟠 Medium | [1621. Number of Sets of K Non-Overlapping Line Segments][lc1621]                |                                         |
|     | 🔴 Hard   | [188. Best Time to Buy and Sell Stock IV][lc188]                                 |                                         |
|     | 🔴 Hard   | [321. Create Maximum Number][lc321]                                              |                                         |
|     | 🔴 Hard   | [403. Frog Jump][lc403]                                                          |                                         |
|     | 🔴 Hard   | [410. Split Array Largest Sum][lc410]                                            |                                         |
|     | 🔴 Hard   | [514. Freedom Trail][lc514]                                                      |                                         |
| ✅  | 🔴 Hard   | [871. Minimum Number of Refueling Stops][lc871]                                  | [![python](../../res/py.png)][lc871py]  |
|     | 🔴 Hard   | [920. Number of Music Playlists][lc920]                                          |                                         |
| ✅  | 🔴 Hard   | [1220. Count Vowels Permutation][lc1220]                                         | [![python](../../res/py.png)][lc1220py] |
|     | 🔴 Hard   | [1223. Dice Roll Simulation][lc1223]                                             |                                         |
|     | 🔴 Hard   | [1289. Minimum Falling Path Sum II][lc1289]                                      |                                         |
|     | 🔴 Hard   | [1320. Minimum Distance to Type a Word Using Two Fingers][lc1320]                |                                         |
|     | 🔴 Hard   | [1335. Minimum Difficulty of a Job Schedule][lc1335]                             |                                         |
|     | 🔴 Hard   | [1411. Number of Ways to Paint N × 3 Grid][lc1411]                               |                                         |
|     | 🔴 Hard   | [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons][lc1420] |                                         |
|     | 🔴 Hard   | [1444. Number of Ways of Cutting a Pizza][lc1444]                                |                                         |
| ✅  | 🔴 Hard   | [1473. Paint House III][lc1473]                                                  | [![python](../../res/py.png)][lc1473py] |
|     | 🔴 Hard   | [1575. Count All Possible Routes][lc1575]                                        |                                         |

[lc120]: https://leetcode.com/problems/triangle/
[lc120py]: ../triangle.py
[lc377]: https://leetcode.com/problems/combination-sum-iv/
[lc377py]: ../combination-sum-iv.py
[lc576]: https://leetcode.com/problems/out-of-boundary-paths/
[lc576py]: ../out-of-boundary-paths.py
[lc688]: https://leetcode.com/problems/knight-probability-in-chessboard/
[lc799]: https://leetcode.com/problems/champagne-tower/
[lc813]: https://leetcode.com/problems/largest-sum-of-averages/
[lc931]: https://leetcode.com/problems/minimum-falling-path-sum/
[lc1024]: https://leetcode.com/problems/video-stitching/
[lc1027]: https://leetcode.com/problems/longest-arithmetic-subsequence/
[lc1140]: https://leetcode.com/problems/stone-game-ii/
[lc1155]: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
[lc1155py]: ../number-of-dice-rolls-with-target-sum.py
[lc1621]: https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
[lc188]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
[lc321]: https://leetcode.com/problems/create-maximum-number/
[lc403]: https://leetcode.com/problems/frog-jump/
[lc410]: https://leetcode.com/problems/split-array-largest-sum/
[lc514]: https://leetcode.com/problems/freedom-trail/
[lc871]: https://leetcode.com/problems/minimum-number-of-refueling-stops/
[lc871py]: ../minimum-number-of-refueling-stops.py
[lc920]: https://leetcode.com/problems/number-of-music-playlists/
[lc1220]: https://leetcode.com/problems/count-vowels-permutation/
[lc1220py]: ../count-vowels-permutation.py
[lc1223]: https://leetcode.com/problems/dice-roll-simulation/
[lc1289]: https://leetcode.com/problems/minimum-falling-path-sum-ii/
[lc1320]: https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
[lc1335]: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
[lc1411]: https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
[lc1420]: https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
[lc1444]: https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
[lc1473]: https://leetcode.com/problems/paint-house-iii/
[lc1473py]: ../paint-house-iii.py
[lc1575]: https://leetcode.com/problems/count-all-possible-routes/

## 4. Interval DP

|     | Level     | Name                                                   | Solutions |
| :-: | --------- | ------------------------------------------------------ | --------- |
|     | 🟠 Medium | [375. Guess Number Higher or Lower II][lc375]          |           |
|     | 🟠 Medium | [413. Arithmetic Slices][lc413]                        |           |
|     | 🟠 Medium | [486. Predict the Winner][lc486]                       |           |
|     | 🟠 Medium | [647. Palindromic Substrings][lc647]                   |           |
|     | 🟠 Medium | [877. Stone Game][lc877]                               |           |
|     | 🟠 Medium | [1039. Minimum Score Triangulation of Polygon][lc1039] |           |
|     | 🟠 Medium | [1049. Last Stone Weight II][lc1049]                   |           |
|     | 🟠 Medium | [1130. Minimum Cost Tree From Leaf Values][lc1130]     |           |
|     | 🟠 Medium | [1690. Stone Game VII][lc1690]                         |           |
|     | 🔴 Hard   | [312. Burst Balloons][lc312]                           |           |
|     | 🔴 Hard   | [546. Remove Boxes][lc546]                             |           |
|     | 🔴 Hard   | [664. Strange Printer][lc664]                          |           |
|     | 🔴 Hard   | [903. Valid Permutations for DI Sequence][lc903]       |           |
|     | 🔴 Hard   | [1000. Minimum Cost to Merge Stones][lc1000]           |           |
|     | 🔴 Hard   | [1478. Allocate Mailboxes][lc1478]                     |           |
|     | 🔴 Hard   | [1547. Minimum Cost to Cut a Stick][lc1547]            |           |
|     | 🔴 Hard   | [1563. Stone Game V][lc1563]                           |           |

[lc375]: https://leetcode.com/problems/guess-number-higher-or-lower-ii/
[lc413]: https://leetcode.com/problems/arithmetic-slices/
[lc486]: https://leetcode.com/problems/predict-the-winner/
[lc647]: https://leetcode.com/problems/palindromic-substrings/
[lc877]: https://leetcode.com/problems/stone-game/
[lc1039]: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
[lc1049]: https://leetcode.com/problems/last-stone-weight-ii/
[lc1130]: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
[lc1690]: https://leetcode.com/problems/stone-game-vii/
[lc312]: https://leetcode.com/problems/burst-balloons/
[lc546]: https://leetcode.com/problems/remove-boxes/
[lc664]: https://leetcode.com/problems/strange-printer/
[lc903]: https://leetcode.com/problems/valid-permutations-for-di-sequence/
[lc1000]: https://leetcode.com/problems/minimum-cost-to-merge-stones/
[lc1478]: https://leetcode.com/problems/allocate-mailboxes/
[lc1547]: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
[lc1563]: https://leetcode.com/problems/stone-game-v/

## 5. bit DP

|     | Level     | Name                                                                | Solutions |
| :-: | --------- | ------------------------------------------------------------------- | --------- |
|     | 🟠 Medium | [464. Can I Win][lc464]                                             |           |
|     | 🟠 Medium | [698. Partition to K Equal Sum Subsets][lc698]                      |           |
|     | 🔴 Hard   | [691. Stickers to Spell Word][lc691]                                |           |
|     | 🔴 Hard   | [847. Shortest Path Visiting All Nodes][lc847]                      |           |
|     | 🔴 Hard   | [1125. Smallest Sufficient Team][lc1125]                            |           |
|     | 🔴 Hard   | [1349. Maximum Students Taking Exam][lc1349]                        |           |
|     | 🔴 Hard   | [1434. Number of Ways to Wear Different Hats to Each Other][lc1434] |           |
|     | 🔴 Hard   | [1595. Minimum Cost to Connect Two Groups of Points][lc1595]        |           |
|     | 🔴 Hard   | [1601. Maximum Number of Achievable Transfer Requests][lc1601]      |           |
|     | 🔴 Hard   | [1655. Distribute Repeating Integers][lc1655]                       |           |
|     | 🔴 Hard   | [1659. Maximize Grid Happiness][lc1659]                             |           |
|     | 🔴 Hard   | [1723. Find Minimum Time to Finish All Jobs][lc1723]                |           |

[lc464]: https://leetcode.com/problems/can-i-win/
[lc698]: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
[lc691]: https://leetcode.com/problems/stickers-to-spell-word/
[lc847]: https://leetcode.com/problems/shortest-path-visiting-all-nodes/
[lc1125]: https://leetcode.com/problems/smallest-sufficient-team/
[lc1349]: https://leetcode.com/problems/maximum-students-taking-exam/
[lc1434]: https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/
[lc1595]: https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/
[lc1601]: https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
[lc1655]: https://leetcode.com/problems/distribute-repeating-integers/
[lc1659]: https://leetcode.com/problems/maximize-grid-happiness/
[lc1723]: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

## 6. Digit DP

|     | Level   | Name                                                         | Solutions |
| :-: | ------- | ------------------------------------------------------------ | --------- |
|     | 🔴 Hard | [600. Non-negative Integers without Consecutive Ones][lc600] |           |
|     | 🔴 Hard | [902. Numbers At Most N Given Digit Set][lc902]              |           |
|     | 🔴 Hard | [1012. Numbers With Repeated Digits][lc1012]                 |           |
|     | 🔴 Hard | [2376. Count Special Integers][lc2376]                       |           |

[lc600]: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
[lc902]: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
[lc1012]: https://leetcode.com/problems/numbers-with-repeated-digits/
[lc2376]: https://leetcode.com/problems/count-special-integers/

## 7. DP on Trees

|     | Level     | Name                                                            | Solutions                              |
| :-: | --------- | --------------------------------------------------------------- | -------------------------------------- |
|     | 🟠 Medium | [95. Unique Binary Search Trees II][lc95]                       |                                        |
| ✅  | 🟠 Medium | [337. House Robber III][lc337]                                  | [![python](../../res/py.png)][lc337py] |
|     | 🟠 Medium | [1339. Maximum Product of Splitted Binary Tree][lc1339]         |                                        |
|     | 🟠 Medium | [1367. Linked List in Binary Tree][lc1367]                      |                                        |
|     | 🟠 Medium | [1372. Longest ZigZag Path in a Binary Tree][lc1372]            |                                        |
| ✅  | 🔴 Hard   | [968. Binary Tree Cameras][lc968]                               | [![python](../../res/py.png)][lc968py] |
|     | 🔴 Hard   | [1373. Maximum Sum BST in Binary Tree][lc1373]                  |                                        |
|     | 🔴 Hard   | [1569. Number of Ways to Reorder Array to Get Same BST][lc1569] |                                        |

[lc95]: https://leetcode.com/problems/unique-binary-search-trees-ii/
[lc337]: https://leetcode.com/problems/house-robber-iii/
[lc337py]: ../house-robber-iii.py
[lc1339]: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
[lc1367]: https://leetcode.com/problems/linked-list-in-binary-tree/
[lc1372]: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
[lc968]: https://leetcode.com/problems/binary-tree-cameras/
[lc968py]: ../binary-tree-cameras.py
[lc1373]: https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
[lc1569]: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

## 8. String DP

|     | Level     | Name                                                                      | Solutions                               |
| :-: | --------- | ------------------------------------------------------------------------- | --------------------------------------- |
| ✅  | 🟢 Easy   | [392. Is Subsequence][lc392]                                              | [![python](../../res/py.png)][lc392py]  |
|     | 🟠 Medium | [131. Palindrome Partitioning][lc131]                                     |                                         |
|     | 🟠 Medium | [139. Word Break][lc139]                                                  |                                         |
|     | 🟠 Medium | [467. Unique Substrings in Wraparound String][lc467]                      |                                         |
|     | 🟠 Medium | [712. Minimum ASCII Delete Sum for Two Strings][lc712]                    |                                         |
| ✅  | 🟠 Medium | [1048. Longest String Chain][lc1048]                                      | [![python](../../res/py.png)][lc1048py] |
|     | 🟠 Medium | [1405. Longest Happy String][lc1405]                                      |                                         |
|     | 🔴 Hard   | [32. Longest Valid Parentheses][lc32]                                     |                                         |
|     | 🔴 Hard   | [115. Distinct Subsequences][lc115]                                       |                                         |
|     | 🔴 Hard   | [132. Palindrome Partitioning II][lc132]                                  |                                         |
|     | 🔴 Hard   | [140. Word Break II][lc140]                                               |                                         |
|     | 🔴 Hard   | [466. Count The Repetitions][lc466]                                       |                                         |
|     | 🔴 Hard   | [472. Concatenated Words][lc472]                                          |                                         |
|     | 🔴 Hard   | [730. Count Different Palindromic Subsequences][lc730]                    |                                         |
|     | 🔴 Hard   | [940. Distinct Subsequences II][lc940]                                    |                                         |
|     | 🔴 Hard   | [1147. Longest Chunked Palindrome Decomposition][lc1147]                  |                                         |
|     | 🔴 Hard   | [1278. Palindrome Partitioning III][lc1278]                               |                                         |
|     | 🔴 Hard   | [1397. Find All Good Strings][lc1397]                                     |                                         |
|     | 🔴 Hard   | [1531. String Compression II][lc1531]                                     |                                         |
|     | 🔴 Hard   | [1639. Number of Ways to Form a Target String Given a Dictionary][lc1639] |                                         |

[lc392]: https://leetcode.com/problems/is-subsequence/
[lc392py]: ../is-subsequence.py
[lc131]: https://leetcode.com/problems/palindrome-partitioning/
[lc139]: https://leetcode.com/problems/word-break/
[lc467]: https://leetcode.com/problems/unique-substrings-in-wraparound-string/
[lc712]: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
[lc1048]: https://leetcode.com/problems/longest-string-chain/
[lc1048py]: ../longest-string-chain.py
[lc1405]: https://leetcode.com/problems/longest-happy-string/
[lc32]: https://leetcode.com/problems/longest-valid-parentheses/
[lc115]: https://leetcode.com/problems/distinct-subsequences/
[lc132]: https://leetcode.com/problems/palindrome-partitioning-ii/
[lc140]: https://leetcode.com/problems/word-break-ii/
[lc466]: https://leetcode.com/problems/count-the-repetitions/
[lc472]: https://leetcode.com/problems/concatenated-words/
[lc730]: https://leetcode.com/problems/count-different-palindromic-subsequences/
[lc940]: https://leetcode.com/problems/distinct-subsequences-ii/
[lc1147]: https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
[lc1278]: https://leetcode.com/problems/palindrome-partitioning-iii/
[lc1397]: https://leetcode.com/problems/find-all-good-strings/
[lc1531]: https://leetcode.com/problems/string-compression-ii/
[lc1639]: https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

## 9. Probability DP

|     | Level     | Name                                                 | Solutions |
| :-: | --------- | ---------------------------------------------------- | --------- |
|     | 🟠 Medium | [808. Soup Servings][lc808]                          |           |
|     | 🟠 Medium | [837. New 21 Game][lc837]                            |           |
|     | 🟠 Medium | [1227. Airplane Seat Assignment Probability][lc1227] |           |

[lc808]: https://leetcode.com/problems/soup-servings/
[lc837]: https://leetcode.com/problems/new-21-game/
[lc1227]: https://leetcode.com/problems/airplane-seat-assignment-probability/

## 10. Classic DPs

### A. Kadane's Algorithm

|     | Level     | Name                                                   | Solutions                              |
| :-: | --------- | ------------------------------------------------------ | -------------------------------------- |
| ✅  | 🟠 Medium | [53. Maximum Subarray][lc53]                           | [![python](../../res/py.png)][lc53py]  |
| ✅  | 🟠 Medium | [152. Maximum Product Subarray][lc152]                 | [![python](../../res/py.png)][lc152py] |
|     | 🟠 Medium | [368. Largest Divisible Subset][lc368]                 |                                        |
|     | 🟠 Medium | [873. Length of Longest Fibonacci Subsequence][lc873]  |                                        |
|     | 🟠 Medium | [898. Bitwise ORs of Subarrays][lc898]                 |                                        |
|     | 🟠 Medium | [978. Longest Turbulent Subarray][lc978]               |                                        |
|     | 🟠 Medium | [1186. Maximum Subarray Sum with One Deletion][lc1186] |                                        |
|     | 🟠 Medium | [1191. K-Concatenation Maximum Sum][lc1191]            |                                        |

[lc53]: https://leetcode.com/problems/maximum-subarray/
[lc53py]: ../maximum-subarray.py
[lc152]: https://leetcode.com/problems/maximum-product-subarray/
[lc152py]: ../maximum-product-subarray.py
[lc368]: https://leetcode.com/problems/largest-divisible-subset/
[lc873]: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
[lc898]: https://leetcode.com/problems/bitwise-ors-of-subarrays/
[lc978]: https://leetcode.com/problems/longest-turbulent-subarray/
[lc1186]: https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
[lc1191]: https://leetcode.com/problems/k-concatenation-maximum-sum/

### B. LCS

|     | Level     | Name                                                                | Solutions                               |
| :-: | --------- | ------------------------------------------------------------------- | --------------------------------------- |
| ✅  | 🟠 Medium | [5. Longest Palindromic Substring][lc5]                             | [![python](../../res/py.png)][lc5py]    |
|     | 🟠 Medium | [97. Interleaving String][lc97]                                     |                                         |
|     | 🟠 Medium | [516. Longest Palindromic Subsequence][lc516]                       |                                         |
| ✅  | 🟠 Medium | [718. Maximum Length of Repeated Subarray][lc718]                   | ![python](../../res/py.png)][lc718py]   |
| ✅  | 🟠 Medium | [1143. Longest Common Subsequence][lc1143]                          | [![python](../../res/py.png)][lc1143py] |
|     | 🔴 Hard   | [10. Regular Expression Matching][lc10]                             |                                         |
|     | 🔴 Hard   | [44. Wildcard Matching][lc44]                                       |                                         |
|     | 🔴 Hard   | [72. Edit Distance][lc72]                                           |                                         |
|     | 🔴 Hard   | [1092. Shortest Common Supersequence][lc1092]                       |                                         |
|     | 🔴 Hard   | [1312. Minimum Insertion Steps to Make a String Palindrome][lc1312] |                                         |
|     | 🔴 Hard   | [1458. Max Dot Product of Two Subsequences][lc1458]                 |                                         |

[lc5]: https://leetcode.com/problems/longest-palindromic-substring/
[lc5py]: ../longest-palindromic-substring.py
[lc97]: https://leetcode.com/problems/interleaving-string/
[lc516]: https://leetcode.com/problems/longest-palindromic-subsequence/
[lc718]: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
[lc718py]: ../maximum-length-of-repeated-subarray.py
[lc1143]: https://leetcode.com/problems/longest-common-subsequence/
[lc1143py]: ../longest-common-subsequence.py
[lc10]: https://leetcode.com/problems/regular-expression-matching/
[lc44]: https://leetcode.com/problems/wildcard-matching/
[lc72]: https://leetcode.com/problems/edit-distance/
[lc1092]: https://leetcode.com/problems/shortest-common-supersequence/
[lc1312]: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
[lc1458]: https://leetcode.com/problems/max-dot-product-of-two-subsequences/

### C. LIS

|     | Level     | Name                                                              | Solutions                              |
| :-: | --------- | ----------------------------------------------------------------- | -------------------------------------- |
| ✅  | 🟠 Medium | [300. Longest Increasing Subsequence][lc300]                      | [![python](../../res/py.png)][lc300py] |
|     | 🟠 Medium | [673. Number of Longest Increasing Subsequence][lc673]            |                                        |
|     | 🔴 Hard   | [354. Russian Doll Envelopes][lc354]                              |                                        |
|     | 🔴 Hard   | [960. Delete Columns to Make Sorted III][lc960]                   |                                        |
|     | 🔴 Hard   | [1187. Make Array Strictly Increasing][lc1187]                    |                                        |
|     | 🔴 Hard   | [1671. Minimum Number of Removals to Make Mountain Array][lc1671] |                                        |
|     | 🔴 Hard   | [1691. Maximum Height by Stacking Cuboids][lc1691]                |                                        |

[lc300]: https://leetcode.com/problems/longest-increasing-subsequence/
[lc300py]: ../longest-increasing-subsequence.py
[lc673]: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
[lc354]: https://leetcode.com/problems/russian-doll-envelopes/
[lc960]: https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
[lc1187]: https://leetcode.com/problems/make-array-strictly-increasing/
[lc1671]: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
[lc1691]: https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

### D. 2D Grid Traversal

|     | Level     | Name                                                     | Solutions                               |
| :-: | --------- | -------------------------------------------------------- | --------------------------------------- |
| ✅  | 🟠 Medium | [62. Unique Paths][lc62]                                 | [![python](../../res/py.png)][lc62py]   |
|     | 🟠 Medium | [63. Unique Paths II][lc63]                              |                                         |
|     | 🟠 Medium | [64. Minimum Path Sum][lc64]                             |                                         |
|     | 🟠 Medium | [1594. Maximum Non Negative Product in a Matrix][lc1594] |                                         |
| ✅  | 🟠 Medium | [1706. Where Will the Ball Fall][lc1706]                 | [![python](../../res/py.png)][lc1706py] |
|     | 🔴 Hard   | [174. Dungeon Game][lc174]                               |                                         |
|     | 🔴 Hard   | [741. Cherry Pickup][lc741]                              |                                         |
|     | 🔴 Hard   | [1301. Number of Paths with Max Score][lc1301]           |                                         |
|     | 🔴 Hard   | [1463. Cherry Pickup II][lc1463]                         |                                         |
|     | 🔴 Hard   | [1643. Kth Smallest Instructions][lc1643]                |                                         |

[lc62]: https://leetcode.com/problems/unique-paths/
[lc62py]: ../unique-paths.py
[lc63]: https://leetcode.com/problems/unique-paths-ii/
[lc64]: https://leetcode.com/problems/minimum-path-sum/
[lc1594]: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
[lc1706]: https://leetcode.com/problems/where-will-the-ball-fall/
[lc1706py]: ../where-will-the-ball-fall.py
[lc174]: https://leetcode.com/problems/dungeon-game/
[lc741]: https://leetcode.com/problems/cherry-pickup/
[lc1301]: https://leetcode.com/problems/number-of-paths-with-max-score/
[lc1463]: https://leetcode.com/problems/cherry-pickup-ii/
[lc1643]: https://leetcode.com/problems/kth-smallest-instructions/

### E. Cumulative Sum

|     | Level     | Name                                                     | Solutions                               |
| :-: | --------- | -------------------------------------------------------- | --------------------------------------- |
| ✅  | 🟢 Easy   | [303. Range Sum Query - Immutable][lc303]                | [![python](../../res/py.png)][lc303py]  |
|     | 🟠 Medium | [221. Maximal Square][lc221]                             |                                         |
| ✅  | 🟠 Medium | [304. Range Sum Query 2D - Immutable][lc304]             | [![python](../../res/py.png)][lc304py]  |
|     | 🟠 Medium | [764. Largest Plus Sign][lc764]                          |                                         |
| ✅  | 🟠 Medium | [838. Push Dominoes][lc838]                              | [![python](../../res/py.png)][lc838py]  |
|     | 🟠 Medium | [1139. Largest 1-Bordered Square][lc1139]                |                                         |
|     | 🟠 Medium | [1277. Count Square Submatrices with All Ones][lc1277]   |                                         |
|     | 🟠 Medium | [1314. Matrix Block Sum][lc1314]                         |                                         |
| ✅  | 🟠 Medium | [1423. Maximum Points You Can Obtain from Cards][lc1423] | [![python](../../res/py.png)][lc1423py] |
|     | 🟠 Medium | [1504. Count Submatrices With All Ones][lc1504]          |                                         |
|     | 🟠 Medium | [1664. Ways to Make a Fair Array][lc1664]                |                                         |
|     | 🔴 Hard   | [85. Maximal Rectangle][lc85]                            |                                         |
| ✅  | 🔴 Hard   | [363. Max Sum of Rectangle No Larger Than K][lc363]      | [![python](../../res/py.png)][lc363py]  |
|     | 🔴 Hard   | [517. Super Washing Machines][lc517]                     |                                         |
|     | 🔴 Hard   | [689. Maximum Sum of 3 Non-Overlapping Subarrays][lc689] |                                         |
| ❤️  | 🔴 Hard   | [1074. Number of Submatrices That Sum to Target][lc1074] | [![python](../../res/py.png)][lc1074py] |
|     | 🔴 Hard   | [1537. Get the Maximum Score][lc1537]                    |                                         |

[lc303]: https://leetcode.com/problems/range-sum-query-immutable/
[lc303py]: ../range-sum-query-immutable.py
[lc221]: https://leetcode.com/problems/maximal-square/
[lc304]: https://leetcode.com/problems/range-sum-query-2d-immutable/
[lc304py]: ../range-sum-query-2d-immutable.py
[lc764]: https://leetcode.com/problems/largest-plus-sign/
[lc838]: https://leetcode.com/problems/push-dominoes/
[lc838py]: ../push-dominoes.py
[lc1139]: https://leetcode.com/problems/largest-1-bordered-square/
[lc1277]: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
[lc1314]: https://leetcode.com/problems/matrix-block-sum/
[lc1423]: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
[lc1423py]: ../maximum-points-you-can-obtain-from-cards.py
[lc1504]: https://leetcode.com/problems/count-submatrices-with-all-ones/
[lc1664]: https://leetcode.com/problems/ways-to-make-a-fair-array/
[lc85]: https://leetcode.com/problems/maximal-rectangle/
[lc363]: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
[lc363py]: ../max-sum-of-rectangle-no-larger-than-k.py
[lc517]: https://leetcode.com/problems/super-washing-machines/
[lc689]: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
[lc1074]: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
[lc1074py]: ../number-of-submatrices-that-sum-to-target.py
[lc1537]: https://leetcode.com/problems/get-the-maximum-score/

### F. Hashmap (SubArray)

|     | Level     | Name                                                                               | Solutions |
| :-: | --------- | ---------------------------------------------------------------------------------- | --------- |
|     | 🟠 Medium | [523. Continuous Subarray Sum][lc523]                                              |           |
|     | 🟠 Medium | [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum][lc1477]           |           |
|     | 🟠 Medium | [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target][lc1546] |           |

[lc523]: https://leetcode.com/problems/continuous-subarray-sum/
[lc1477]: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
[lc1546]: https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

## 11. DP + Alpha (Tricks/DS)

|     | Level   | Name                                                   | Solutions |
| :-: | ------- | ------------------------------------------------------ | --------- |
|     | 🔴 Hard | [446. Arithmetic Slices II - Subsequence][lc446]       |           |
|     | 🔴 Hard | [975. Odd Even Jump][lc975]                            |           |
|     | 🔴 Hard | [1425. Constrained Subsequence Sum][lc1425]            |           |
|     | 🔴 Hard | [1687. Delivering Boxes from Storage to Ports][lc1687] |           |

[lc446]: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
[lc975]: https://leetcode.com/problems/odd-even-jump/
[lc1425]: https://leetcode.com/problems/constrained-subsequence-sum/
[lc1687]: https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

## 12. Insertion DP

|     | Level   | Name                                | Solutions                              |
| :-: | ------- | ----------------------------------- | -------------------------------------- |
| ✅  | 🔴 Hard | [629. K Inverse Pairs Array][lc629] | [![python](../../res/py.png)][lc629py] |

[lc629]: https://leetcode.com/problems/k-inverse-pairs-array/
[lc629py]: ../k-inverse-pairs-array.py

## 13. Graph DP

|     | Level   | Name                                          | Solutions |
| :-: | ------- | --------------------------------------------- | --------- |
|     | 🔴 Hard | [787. Cheapest Flights Within K Stops][lc787] |           |

[lc787]: https://leetcode.com/problems/cheapest-flights-within-k-stops/

## 14. Memoization

|     | Level     | Name                                                                      | Solutions |
| :-: | --------- | ------------------------------------------------------------------------- | --------- |
|     | 🟠 Medium | [1654. Minimum Jumps to Reach Home][lc1654]                               |           |
|     | 🔴 Hard   | [87. Scramble String][lc87]                                               |           |
|     | 🔴 Hard   | [1240. Tiling a Rectangle with the Fewest Squares][lc1240]                |           |
|     | 🔴 Hard   | [1269. Number of Ways to Stay in the Same Place After Some Steps][lc1269] |           |
|     | 🔴 Hard   | [1340. Jump Game V][lc1340]                                               |           |
|     | 🔴 Hard   | [1553. Minimum Number of Days to Eat N Oranges][lc1553]                   |           |

[lc1654]: https://leetcode.com/problems/minimum-jumps-to-reach-home/
[lc87]: https://leetcode.com/problems/scramble-string/
[lc1240]: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
[lc1269]: https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
[lc1340]: https://leetcode.com/problems/jump-game-v/
[lc1553]: https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

## 15. Binary Lifting

|     | Level   | Name                                        | Solutions |
| :-: | ------- | ------------------------------------------- | --------- |
|     | 🔴 Hard | [1483. Kth Ancestor of a Tree Node][lc1483] |           |

[lc1483]: https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

## 16. Math

|     | Level     | Name                                                             | Solutions |
| :-: | --------- | ---------------------------------------------------------------- | --------- |
|     | 🟠 Medium | [264. Ugly Number II][lc264]                                     |           |
|     | 🟠 Medium | [1641. Count Sorted Vowel Strings][lc1641]                       |           |
|     | 🔴 Hard   | [818. Race Car][lc818]                                           |           |
|     | 🔴 Hard   | [887. Super Egg Drop][lc887]                                     |           |
|     | 🔴 Hard   | [964. Least Operators to Express Number][lc964]                  |           |
|     | 🔴 Hard   | [1363. Largest Multiple of Three][lc1363]                        |           |
|     | 🔴 Hard   | [1611. Minimum One Bit Operations to Make Integers Zero][lc1611] |           |

[lc264]: https://leetcode.com/problems/ugly-number-ii/
[lc1641]: https://leetcode.com/problems/count-sorted-vowel-strings/
[lc818]: https://leetcode.com/problems/race-car/
[lc887]: https://leetcode.com/problems/super-egg-drop/
[lc964]: https://leetcode.com/problems/least-operators-to-express-number/
[lc1363]: https://leetcode.com/problems/largest-multiple-of-three/
[lc1611]: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

## Related reading

Blog article in Dynamic Programming Patterns [link](https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns)
