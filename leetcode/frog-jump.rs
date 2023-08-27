// 403. Frog Jump
// 🔴 Hard
//
// https://leetcode.com/problems/frog-jump/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// We can use dynamic programming, have an internal function that, given
    /// an index and a jump value, determines if we can make that jump, the
    /// function uses the position at the current index and the jump value to
    /// compute the landing position, then binary search for it to the right
    /// of the current index in the input vector. If the landing position is
    /// found, we recursively try the 3 possible jumps from that position until
    /// we either cannot make the next jump or reach the end. Use a hashmap to
    /// store combinations of index and jump that we have already computed.
    ///
    /// Time complexity: O(n*log(n)) - We can try a maximum of 3 different
    /// jump values, k-1, k, k+1 from each position in the input vector, for
    /// each, we will binary search the landing position to the right of the
    /// current position.
    /// Space complexity: O(n^2) - The memo hashmap can have an entry for each
    /// possible combination of index and jump value.
    ///
    /// Runtime 12 ms Beats 71.43%
    /// Memory 4.80 MB Beats 71.43%
    pub fn can_cross(stones: Vec<i32>) -> bool {
        // let mut memo: HashMap<(usize, i32), bool> = HashMap::new();
        const N: usize = 2001;
        let mut memo: [[Option<bool>; N]; N] = [[None; N]; N];
        fn can_jump_k(
            stones: &Vec<i32>,
            current_idx: usize,
            k: i32,
            memo: &mut [[Option<bool>; N]; N],
        ) -> bool {
            if k == 0 || k as usize > N - 1 {
                return false;
            }
            if let Some(result) = memo[current_idx][k as usize] {
                return result;
            }
            let target = stones[current_idx] + k;
            match stones[current_idx..].binary_search(&target) {
                Ok(slice_index) => {
                    let idx = current_idx + slice_index;
                    let result = idx == stones.len() - 1
                        || can_jump_k(stones, idx, k - 1, memo)
                        || can_jump_k(stones, idx, k, memo)
                        || can_jump_k(stones, idx, k + 1, memo);
                    memo[current_idx][k as usize] = Some(result);
                    result
                }
                Err(_) => {
                    memo[current_idx][k as usize] = Some(false);
                    false
                }
            }
        }
        can_jump_k(&stones, 0, 1, &mut memo)
    }

    /// Similar to the previous solution but use a vector instead of a hashmap.
    /// It is also possible to use an array bounded to 2001 because that
    /// maximum is known at compile time, but, with the given tests, the
    /// memory usage is higher.
    ///
    /// Time complexity: O(n*log(n)) - We can try a maximum of 3 different
    /// jump values, k-1, k, k+1 from each position in the input vector, for
    /// each, we will binary search the landing position to the right of the
    /// current position.
    /// Space complexity: O(n^2) - The memo vector can have an entry for each
    /// possible combination of index and jump value, both of them bound to n.
    ///
    /// Runtime 3 ms Beats 100%
    /// Memory 5.90 MB Beats 71.43%
    pub fn can_cross_2(stones: Vec<i32>) -> bool {
        let n = stones.len();
        if n < 2 || stones[1] - stones[0] != 1 || stones[n - 1] as usize >= n * n / 2 {
            return false;
        }
        let mut memo: Vec<Vec<Option<bool>>> = vec![vec![None; n]; n];
        fn can_jump_k(
            stones: &Vec<i32>,
            current_idx: usize,
            k: i32,
            n: i32,
            memo: &mut Vec<Vec<Option<bool>>>,
        ) -> bool {
            if k == 0 || k > n - 1 {
                return false;
            }
            if let Some(result) = memo[current_idx][k as usize] {
                return result;
            }
            let target = stones[current_idx] + k;
            match stones[current_idx..].binary_search(&target) {
                Ok(slice_index) => {
                    let idx = current_idx + slice_index;
                    let result = idx == stones.len() - 1
                        || can_jump_k(stones, idx, k - 1, n, memo)
                        || can_jump_k(stones, idx, k, n, memo)
                        || can_jump_k(stones, idx, k + 1, n, memo);
                    memo[current_idx][k as usize] = Some(result);
                    result
                }
                Err(_) => {
                    memo[current_idx][k as usize] = Some(false);
                    false
                }
            }
        }
        can_jump_k(&stones, 0, 1, n as i32, &mut memo)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0, 2147483647], false),
        (vec![0, 1, 3, 5, 6, 8, 12, 17], true),
        (vec![0, 1, 2, 3, 4, 8, 9, 11], false),
    ];
    for t in tests {
        assert_eq!(Solution::can_cross(t.0.clone()), t.1);
        assert_eq!(Solution::can_cross_2(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
