struct Solution;
impl Solution {
    // Create a hash map of integers that we have seen mapped to their index.
    // For each element, try to find its complementary in the hashmap, if
    // found, we have the result and can return immediately, otherwise, add
    // the value to the hashmap for later checks.
    //
    // Time complexity: O(n) - We iterate over each value and, for each,
    // we do a O(1) check in a hashmap.
    // Space complexity: O(n) - The hashmap can grow to the same size
    // as the input.
    //
    // Runtime 2 ms Beats 81.86%
    // Memory 2.1 MB Beats 86.51%
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        let mut seen = HashMap::with_capacity(nums.len());
        for (idx, num) in nums.iter().enumerate() {
            match seen.get(&(target - *num)) {
                Some(&idx_b) => return vec![idx as i32, idx_b],
                None => seen.insert(*num, idx as i32),
            };
        }
        panic!()
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![1, 0]);
    assert_eq!(Solution::two_sum(vec![3, 2, 4], 6), vec![2, 1]);
    assert_eq!(Solution::two_sum(vec![3, 3], 6), vec![1, 0]);
    println!("All tests passed!")
}
