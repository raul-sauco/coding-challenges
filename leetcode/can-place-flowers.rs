// 605. Can Place Flowers
// 🟢 Easy
//
// https://leetcode.com/problems/can-place-flowers/
//
// Tags: Array - Greedy

struct Solution;
impl Solution {
    /**
     * Iterate over the indices in flower bed, if the element at the index does
     * not already have a flower itself, and neither of its neighbors has a
     * flower, place one flower there, return true if we can place all of them,
     * false otherwise.
     *
     * Time complexity: O(f) - We may iterate the entire flower bed.
     * Space complexity: O(1) - We use constant extra memory.
     *
     * Runtime 4 ms Beats 57.14%
     * Memory 2.2 MB Beats 85.71%
     */
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        let (mut i, mut count) = (0, n);
        while i < flowerbed.len() && count > 0 {
            if flowerbed[i] == 0
                && (i == 0 || flowerbed[i - 1] == 0)
                && (i == flowerbed.len() - 1 || flowerbed[i + 1] == 0)
            {
                count -= 1;
                i += 1;
            }
            i += 1;
        }
        count == 0
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], 0, true),
        (vec![1, 0, 0, 0, 1], 1, true),
        (vec![1, 0, 0, 0, 1], 2, false),
        (vec![1, 0, 0, 0, 0, 1], 2, false),
        (vec![0, 0, 0, 0, 0, 1, 0, 0], 0, true),
    ];
    for test in tests {
        assert_eq!(Solution::can_place_flowers(test.0, test.1), test.2);
    }
    println!("All tests passed!")
}
