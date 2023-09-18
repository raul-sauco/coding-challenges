// 1337. The K Weakest Rows in a Matrix
// 🟢 Easy
//
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
//
// Tags: Array - Binary Search - Sorting - Heap (Priority Queue) - Matrix

use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// Use a max priority queue to store the k weakest rows. Iterate over all
    /// rows using binary search to count the number of soldiers, push that
    /// count and the row index into the heap. If we have more than k elements
    /// in the heap, pop the top one, that one will be the "strongest" according
    /// to the problem description. Once we visit all rows, use the elements in
    /// the heap to construct a vector sorted from the weakest to the strongest
    /// and return that.
    ///
    /// Time complexity: O(m*(n+log(k))) - We iterate over m rows, for each row,
    /// we visit n columns and possibly push and pop into a heap of size k.
    /// Space complexity: O(k) - The heap of size k uses extra memory.
    ///
    /// Runtime 2 ms Beats 75%
    /// Memory 2.34 MB Beats 10%
    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut weakest: BinaryHeap<(usize, usize)> = BinaryHeap::with_capacity(k + 1);
        fn get_row_soldier_count(row: &Vec<i32>) -> usize {
            if row[0] == 0 {
                return 0;
            } else if row[row.len() - 1] == 1 {
                return row.len();
            }
            let (mut l, mut r) = (0, row.len());
            let mut mid;
            while r - l > 1 {
                mid = (l + r) / 2;
                if row[mid] == 0 {
                    r = mid;
                } else {
                    l = mid;
                }
            }
            r
        }
        let mut soldier_count;
        for row_idx in 0..mat.len() {
            soldier_count = get_row_soldier_count(&mat[row_idx]);
            weakest.push((soldier_count, row_idx));
            if weakest.len() > k {
                // The max heap will pop the element with the most soldiers, if
                // two elements have the same number of soldiers, it will pop
                // the one with the highest index.
                weakest.pop();
            }
        }
        let mut res = (0..k)
            .map(|_| weakest.pop().unwrap().1 as i32)
            .collect::<Vec<_>>();
        res.reverse();
        res
    }

    /// Create a new vector of tuples, the first element in the tuple is a
    /// reference to a row in the input, the second is the index. Sort this new
    /// vector of tuples, then return the index of the first k elements.
    ///
    /// Time complexity: O(m*n*log(m*n)) - Sorting the elements has the highest
    /// time complexity.
    /// Space complexity: O(m*n) - The sorted vector uses extra memory.
    ///
    /// Runtime 2 ms Beats 70%
    /// Memory 2.28 MB Beats 20%
    pub fn k_weakest_rows_2(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut sortable: Vec<(&Vec<i32>, usize)> = (0..mat.len()).map(|i| (&mat[i], i)).collect();
        sortable.sort_unstable();
        (0..k as usize).map(|i| sortable[i].1 as i32).collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![
                vec![1, 1, 0, 0, 0],
                vec![1, 1, 1, 1, 0],
                vec![1, 0, 0, 0, 0],
                vec![1, 1, 0, 0, 0],
                vec![1, 1, 1, 1, 1],
            ],
            3,
            vec![2, 0, 3],
        ),
        (
            vec![
                vec![1, 0, 0, 0],
                vec![1, 1, 1, 1],
                vec![1, 0, 0, 0],
                vec![1, 0, 0, 0],
            ],
            2,
            vec![0, 2],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::k_weakest_rows(t.0.clone(), t.1), t.2);
        assert_eq!(Solution::k_weakest_rows_2(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
