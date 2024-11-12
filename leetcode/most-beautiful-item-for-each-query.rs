// 2070. Most Beautiful Item for Each Query
// 🟠 Medium
//
// https://leetcode.com/problems/most-beautiful-item-for-each-query/
//
// Tags: Array - Binary Search - Sorting

struct Solution;
impl Solution {
    /// Sort the items vector and remove redundant items, only keep items that maximize the beauty
    /// for the given price, we could do the same with a prefix "max" vector, but we can also just
    /// remove items that we will never want to pick. After that, use binary search to find the
    /// item with the highest price we can afford, given the filtering, that is guaranteed to also
    /// have the highest beauty.
    ///
    /// Time complexity: O(m*log(n)+n*log(n)) - First we sort the items vector with n items. Then
    /// we filter them in O(n), then we iterate over m queries, for each, we search the query
    /// result using binary search in log(n).
    /// Space complexity: O(n) - The sorted then filtered items vector.
    ///
    /// Runtime 12 ms Beats 100%
    /// Memory 9.73 MB Beats 100%
    pub fn maximum_beauty(mut items: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        // Sort by price, then beauty.
        items.sort_unstable();
        let mut filtered: Vec<Vec<i32>> = Vec::with_capacity(items.len());
        for item in items {
            while let Some(last) = filtered.last() {
                if last[0] == item[0] && last[1] <= item[1] {
                    filtered.pop();
                } else {
                    if last[1] < item[1] {
                        filtered.push(item.clone());
                    }
                    break;
                }
            }
            if filtered.is_empty() {
                filtered.push(item);
            }
        }
        // println!("{:?}", filtered);
        queries
            .into_iter()
            .map(|q| match filtered.partition_point(|x| q + 1 > x[0]) {
                0 => 0i32,
                idx => filtered[idx - 1][1],
            })
            .collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]],
            vec![1, 2, 3, 4, 5, 6],
            vec![2, 4, 5, 5, 6, 6],
        ),
        (vec![[1, 2], [1, 2], [1, 3], [1, 4]], vec![1], vec![4]),
        (vec![[10, 100]], vec![5], vec![0]),
        (
            vec![
                [193, 732],
                [781, 962],
                [864, 954],
                [749, 627],
                [136, 746],
                [478, 548],
                [640, 908],
                [210, 799],
                [567, 715],
                [914, 388],
                [487, 853],
                [533, 554],
                [247, 919],
                [958, 150],
                [193, 523],
                [176, 656],
                [395, 469],
                [763, 821],
                [542, 946],
                [701, 676],
            ],
            vec![
                885, 1445, 1580, 1309, 205, 1788, 1214, 1404, 572, 1170, 989, 265, 153, 151, 1479,
                1180, 875, 276, 1584,
            ],
            vec![
                962, 962, 962, 962, 746, 962, 962, 962, 946, 962, 962, 919, 746, 746, 962, 962,
                962, 919, 962,
            ],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_beauty(t.0.iter().map(|a| a.to_vec()).collect(), t.1.clone());
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.2, res
            );
        }
    }
    println!();
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
