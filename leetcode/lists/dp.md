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
    - [A. Cadane's Algorithm](#a-cadanes-algorithm)
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

If you clone the repository and want to track your own progress, use search and replace to remove all the progress icons, like ✅ and ❌, and start tracking your own progress.

## 1. Linear DP

|     | Level     | Name                                                                   | Solutions                              |
| :-: | --------- | ---------------------------------------------------------------------- | -------------------------------------- |
| ✅  | 🟢 Easy   | [70. Climbing Stairs][lc70]                                            | [![python](../../res/py.png)][lc70py]  |
| ✅  | 🟢 Easy   | [121. Best Time to Buy and Sell Stock][lc121]                          | [![python](../../res/py.png)][lc121py] |
| ✅  | 🟢 Easy   | [338. Counting Bits][lc338]                                            | [![python](../../res/py.png)][lc338py] |
| ✅  | 🟢 Easy   | [746. Min Cost Climbing Stairs][lc746]                                 | [![python](../../res/py.png)][lc746py] |
|     | 🟢 Easy   | [1025. Divisor Game][lc1025]                                           |                                        |
|     | 🟠 Medium | [91. Decode Ways][lc91]                                                |                                        |
|     | 🟠 Medium | [96. Unique Binary Search Trees][lc96]                                 |                                        |
|     | 🟠 Medium | [198. House Robber][lc198]                                             |                                        |
|     | 🟠 Medium | [279. Perfect Squares][lc279]                                          |                                        |
|     | 🟠 Medium | [309. Best Time to Buy and Sell Stock with Cooldown][lc309]            |                                        |
|     | 🟠 Medium | [322. Coin Change][lc322]                                              |                                        |
|     | 🟠 Medium | [343. Integer Break][lc343]                                            |                                        |
|     | 🟠 Medium | [357. Count Numbers with Unique Digits][lc357]                         |                                        |
| ✅  | 🟠 Medium | [376. Wiggle Subsequence][lc376]                                       | [![python](../../res/py.png)][lc376py] |
|     | 🟠 Medium | [416. Partition Equal Subset Sum][lc416]                               |                                        |
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
[lc96]: https://leetcode.com/problems/unique-binary-search-trees/
[lc198]: https://leetcode.com/problems/house-robber/
[lc279]: https://leetcode.com/problems/perfect-squares/
[lc309]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
[lc322]: https://leetcode.com/problems/coin-change/
[lc343]: https://leetcode.com/problems/integer-break/
[lc357]: https://leetcode.com/problems/count-numbers-with-unique-digits/
[lc376]: https://leetcode.com/problems/wiggle-subsequence/
[lc376py]: ../wiggle-subsequence.py
[lc416]: https://leetcode.com/problems/partition-equal-subset-sum/
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

|     | Level     | Name                                                     | Solutions |
| :-: | --------- | -------------------------------------------------------- | --------- |
|     | 🟠 Medium | [213. House Robber II][lc213]                            |           |
|     | 🟠 Medium | [474. Ones and Zeroes][lc474]                            |           |
|     | 🟠 Medium | [494. Target Sum][lc494]                                 |           |
|     | 🟠 Medium | [638. Shopping Offers][lc638]                            |           |
|     | 🟠 Medium | [650. 2 Keys Keyboard][lc650]                            |           |
|     | 🟠 Medium | [1626. Best Team With No Conflicts][lc1626]              |           |
|     | 🔴 Hard   | [801. Minimum Swaps To Make Sequences Increasing][lc801] |           |
|     | 🔴 Hard   | [879. Profitable Schemes][lc879]                         |           |
|     | 🔴 Hard   | [956. Tallest Billboard][lc956]                          |           |
|     | 🔴 Hard   | [1388. Pizza With 3n Slices][lc1388]                     |           |
|     | 🔴 Hard   | [1402. Reducing Dishes][lc1402]                          |           |

[lc213]: https://leetcode.com/problems/house-robber-ii/
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

|     | Level     | Name                                           | Solutions |
| :-: | --------- | ---------------------------------------------- | --------- |
| ✅  | 🟢 Easy   | [120. Triangle][lc120]                         |           |
|     | 🟠 Medium | [377. Combination Sum IV][lc377]               |           |
| ✅  | 🟠 Medium | [576. Out of Boundary Paths][lc576]            |           |
|     | 🟠 Medium | [688. Knight Probability in Chessboard][lc688] |           |
|     | 🟠 Medium | [799. Champagne Tower][lc799]                  |           |
|     | 🟠 Medium | [813. Largest Sum of Averages][lc813]          |           |
|     | 🟠 Medium | [931. Minimum Falling Path Sum][lc931]         |           |
|     | 🟠 Medium | [1024. Video Stitching][lc1024]                |           |
|     | 🟠 Medium | [1027. Longest Arithmetic Subsequence][lc1027] |           |
|     | 🟠 Medium | [1140. Stone Game II][lc1140]                  |           |
| ❌  | 🔴 Hard   | [1473. Paint House III][lc1473]                |           |
|     | 🔴 Hard   | [1575. Count All Possible Routes][lc1575]      |           |

[lc120]: https://leetcode.com/problems/triangle/
[lc377]: https://leetcode.com/problems/combination-sum-iv/
[lc576]: https://leetcode.com/problems/out-of-boundary-paths/
[lc688]: https://leetcode.com/problems/knight-probability-in-chessboard/
[lc799]: https://leetcode.com/problems/champagne-tower/
[lc813]: https://leetcode.com/problems/largest-sum-of-averages/
[lc931]: https://leetcode.com/problems/minimum-falling-path-sum/
[lc1024]: https://leetcode.com/problems/video-stitching/
[lc1027]: https://leetcode.com/problems/longest-arithmetic-subsequence/
[lc1140]: https://leetcode.com/problems/stone-game-ii/

https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
https://leetcode.com/problems/dice-roll-simulation/
https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
https://leetcode.com/problems/create-maximum-number/
https://leetcode.com/problems/frog-jump/
https://leetcode.com/problems/split-array-largest-sum/
https://leetcode.com/problems/freedom-trail/
https://leetcode.com/problems/minimum-number-of-refueling-stops/
https://leetcode.com/problems/number-of-music-playlists/
https://leetcode.com/problems/count-vowels-permutation/
https://leetcode.com/problems/minimum-falling-path-sum-ii/
https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

[lc1473]: https://leetcode.com/problems/paint-house-iii/
[lc1575]: https://leetcode.com/problems/count-all-possible-routes/

## 4. Interval DP

https://leetcode.com/problems/guess-number-higher-or-lower-ii/
https://leetcode.com/problems/arithmetic-slices/
https://leetcode.com/problems/predict-the-winner/
https://leetcode.com/problems/palindromic-substrings/
https://leetcode.com/problems/stone-game/
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
https://leetcode.com/problems/last-stone-weight-ii/
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
https://leetcode.com/problems/stone-game-vii/
https://leetcode.com/problems/burst-balloons/
https://leetcode.com/problems/remove-boxes/
https://leetcode.com/problems/strange-printer/
https://leetcode.com/problems/valid-permutations-for-di-sequence/
https://leetcode.com/problems/minimum-cost-to-merge-stones/
https://leetcode.com/problems/allocate-mailboxes/
https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
https://leetcode.com/problems/stone-game-v/

## 5. bit DP

https://leetcode.com/problems/can-i-win/
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
https://leetcode.com/problems/stickers-to-spell-word/
https://leetcode.com/problems/shortest-path-visiting-all-nodes/
https://leetcode.com/problems/smallest-sufficient-team/
https://leetcode.com/problems/maximum-students-taking-exam/
https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/
https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/
https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
https://leetcode.com/problems/distribute-repeating-integers/
https://leetcode.com/problems/maximize-grid-happiness/
https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

## 6. Digit DP

https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
https://leetcode.com/problems/numbers-with-repeated-digits/

## 7. DP on Trees

https://leetcode.com/problems/unique-binary-search-trees-ii/
https://leetcode.com/problems/house-robber-iii/
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
https://leetcode.com/problems/linked-list-in-binary-tree/
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
https://leetcode.com/problems/binary-tree-cameras/
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

## 8. String DP

https://leetcode.com/problems/is-subsequence/
https://leetcode.com/problems/palindrome-partitioning/
https://leetcode.com/problems/palindrome-partitioning-ii/
https://leetcode.com/problems/word-break/
https://leetcode.com/problems/unique-substrings-in-wraparound-string/
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
https://leetcode.com/problems/longest-string-chain/
https://leetcode.com/problems/longest-happy-string/
https://leetcode.com/problems/longest-valid-parentheses/
https://leetcode.com/problems/distinct-subsequences/
https://leetcode.com/problems/word-break-ii/
https://leetcode.com/problems/count-the-repetitions/
https://leetcode.com/problems/concatenated-words/
https://leetcode.com/problems/count-different-palindromic-subsequences/
https://leetcode.com/problems/distinct-subsequences-ii/
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
https://leetcode.com/problems/palindrome-partitioning-iii/
https://leetcode.com/problems/find-all-good-strings/
https://leetcode.com/problems/string-compression-ii/
https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

## 9. Probability DP

https://leetcode.com/problems/soup-servings/
https://leetcode.com/problems/new-21-game/
https://leetcode.com/problems/airplane-seat-assignment-probability/

## 10. Classic DPs

### A. Cadane's Algorithm

https://leetcode.com/problems/maximum-subarray/
https://leetcode.com/problems/maximum-product-subarray/
https://leetcode.com/problems/bitwise-ors-of-subarrays/
https://leetcode.com/problems/longest-turbulent-subarray/
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
https://leetcode.com/problems/k-concatenation-maximum-sum/
https://leetcode.com/problems/largest-divisible-subset/
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

### B. LCS

https://leetcode.com/problems/longest-palindromic-substring/
https://leetcode.com/problems/longest-palindromic-subsequence/
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
https://leetcode.com/problems/longest-common-subsequence/
https://leetcode.com/problems/regular-expression-matching/
https://leetcode.com/problems/wildcard-matching/
https://leetcode.com/problems/edit-distance/
https://leetcode.com/problems/interleaving-string/
https://leetcode.com/problems/shortest-common-supersequence/
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
https://leetcode.com/problems/max-dot-product-of-two-subsequences/

### C. LIS

https://leetcode.com/problems/longest-increasing-subsequence/
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
https://leetcode.com/problems/russian-doll-envelopes/
https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
https://leetcode.com/problems/make-array-strictly-increasing/

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
|     | 🟠 Medium | [838. Push Dominoes][lc838]                              |                                         |
|     | 🟠 Medium | [1139. Largest 1-Bordered Square][lc1139]                |                                         |
|     | 🟠 Medium | [1277. Count Square Submatrices with All Ones][lc1277]   |                                         |
|     | 🟠 Medium | [1314. Matrix Block Sum][lc1314]                         |                                         |
| ✅  | 🟠 Medium | [1423. Maximum Points You Can Obtain from Cards][lc1423] | [![python](../../res/py.png)][lc1423py] |
|     | 🟠 Medium | [1504. Count Submatrices With All Ones][lc1504]          |                                         |
|     | 🟠 Medium | [1664. Ways to Make a Fair Array][lc1664]                |                                         |
|     | 🔴 Hard   | [85. Maximal Rectangle][lc85]                            |                                         |
|     | 🔴 Hard   | [363. Max Sum of Rectangle No Larger Than K][lc363]      |                                         |
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
[lc1139]: https://leetcode.com/problems/largest-1-bordered-square/
[lc1277]: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
[lc1314]: https://leetcode.com/problems/matrix-block-sum/
[lc1423]: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
[lc1423py]: ../maximum-points-you-can-obtain-from-cards.py
[lc1504]: https://leetcode.com/problems/count-submatrices-with-all-ones/
[lc1664]: https://leetcode.com/problems/ways-to-make-a-fair-array/
[lc85]: https://leetcode.com/problems/maximal-rectangle/
[lc363]: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
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
