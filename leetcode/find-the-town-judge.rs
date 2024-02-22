// 997. Find the Town Judge
// 🟢 Easy
//
// https://leetcode.com/problems/find-the-town-judge/
//
// Tags: Array - Hash Table - Graph

struct Solution;
impl Solution {
    /// For each entry, count the number of people that trust it and the number of people it trust,
    /// we can use one vector because the amount of people that trust the town judge minus the
    /// amount of people they trust is n-1.
    ///
    /// Time complexity: O(n+t) - We iterate over the t trust relations to get the counts, then we
    /// iterate over the n counts to get the result. In terms of a graph this would be v+e.
    /// Space complexity: O(n) - We store the results in one vector of size n.
    ///
    /// Runtime 14 ms Beats 100%
    /// Memory 2.74 MB Beats 78.26%
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let m = n as usize + 1;
        let mut counter = vec![0; m];
        for t in trust {
            counter[t[0] as usize] -= 1;
            counter[t[1] as usize] += 1;
        }
        for i in 1..m {
            if counter[i] == n - 1 {
                return i as i32;
            }
        }
        -1
    }

    // Same logic as the previous solution, but using two vectors, one for each, this solution
    // would be more adaptable to other conditions, like "the judge trusts a maximum of x people".
    //
    /// Time complexity: O(n+t) - We iterate over the t trust relations to get the counts, then we
    /// iterate over the n counts to get the result. In terms of a graph this would be v+e.
    /// Space complexity: O(n) - We store the results in one vector of size n.
    //
    // Runtime 14 ms Beats 100%
    // Memory 2.8 MB Beats 36%
    #[allow(dead_code)]
    pub fn find_judge_two_vectors(n: i32, trust: Vec<Vec<i32>>) -> i32 {
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
    let tests = [
        (1, vec![], 1),
        (2, vec![[1, 2]], 2),
        (3, vec![[1, 3], [2, 3]], 3),
        (3, vec![[1, 3], [2, 3], [3, 1]], -1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_judge(t.0, t.1.clone().iter().map(|arr| arr.to_vec()).collect());
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
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
