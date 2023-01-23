// 997. Find the Town Judge
// 🟢 Easy
//
// https://leetcode.com/problems/find-the-town-judge/
//
// Tags: Array - Hash Table - Graph

struct Solution;
impl Solution {
    // We can solve this problem using topological sorting, count the
    // elements that are trusted by the current one and elements that the
    // current one trusts, return the element that does not trust any others
    // and is trusted by n-1 others.
    //
    // Time complexity: O(n+t) - Where n is n and t is the number of items
    // in the trust array. We iterate over all the elements in trust to
    // create the topological sorting, then iterate over a max of n elements
    // to find the one that matches the given conditions.
    //
    // Runtime 14 ms Beats 100%
    // Memory 2.8 MB Beats 36%
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let mut trusted_by = vec![0; (n as usize) + 1];
        let mut trusts = vec![0; (n as usize) + 1];
        for t in trust {
            trusts[t[0] as usize] += 1;
            trusted_by[t[1] as usize] += 1;
        }
        for i in 1..=(n as usize) {
            if trusted_by[i] == (n as usize) - 1 && trusts[i] == 0 {
                return i as i32;
            }
        }
        -1
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::find_judge(1, vec![]), 1);
    assert_eq!(Solution::find_judge(2, vec![vec![1, 2]]), 2);
    assert_eq!(Solution::find_judge(3, vec![vec![1, 3], vec![2, 3]]), 3);
    assert_eq!(
        Solution::find_judge(3, vec![vec![1, 3], vec![2, 3], vec![3, 1]]),
        -1
    );
    println!("All tests passed!")
}
