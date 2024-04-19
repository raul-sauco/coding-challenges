// 1095. Find in Mountain Array
// 🔴 Hard
//
// https://leetcode.com/problems/find-in-mountain-array/
//
// Tags: Array - Binary Search - Interactive

// This is the MountainArray's API interface.
// You should not implement it, or speculate about its implementation
struct MountainArray {
    v: Vec<i32>,
}
impl MountainArray {
    fn get(&self, index: i32) -> i32 {
        self.v[index as usize]
    }
    fn length(&self) -> i32 {
        self.v.len() as i32
    }
}

struct Solution;

impl Solution {
    /// The "input" array, or API array, consists of 2 sections of sorted array,
    /// if we start by finding the peak, or inflection point, we can binary
    /// search the ascending, then the descending sections of the mountain
    /// array as a full sorted array using binary search.
    ///
    /// Time complexity: O(log(n)) - We do 3 binary searches at most.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 1 ms Beats 83.33%
    /// Memory 2.24 MB Beats 50%
    pub fn find_in_mountain_array(target: i32, mountainArr: &MountainArray) -> i32 {
        let n = mountainArr.length();
        // Find the peak.
        let (mut l, mut r) = (1, n - 2);
        let mut m;
        let (mut left, mut mid, mut right);
        let mut peak = 0;
        while l <= r {
            m = (l + r) / 2;
            // Destructuring assignment does not work with the current Leetcode OJ
            // version. Update the code to have independent assignments there.
            (left, mid, right) = (
                mountainArr.get(m - 1),
                mountainArr.get(m),
                mountainArr.get(m + 1),
            );
            if left < mid && mid < right {
                l = m + 1;
            } else if left > mid && mid > right {
                r = m - 1;
            } else {
                peak = m;
                break;
            }
        }
        // Try to find target in the ascending side.
        (l, r) = (0, peak);
        while l <= r {
            m = (l + r) / 2;
            mid = mountainArr.get(m);
            if mid < target {
                l = m + 1;
            } else if mid > target {
                r = m - 1;
            } else {
                return m as i32;
            }
        }
        // If we couldn't find target on the ascending section, try the descending section.
        (l, r) = (peak, n - 1);
        while l <= r {
            m = (l + r) / 2;
            mid = mountainArr.get(m);
            if mid > target {
                l = m + 1;
            } else if mid < target {
                r = m - 1;
            } else {
                return m as i32;
            }
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 4, 5, 2], 4, 3),
        (vec![1, 2, 3, 4, 5, 3, 1], 3, 2),
        (vec![0, 1, 2, 4, 2, 1], 3, -1),
        (vec! [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 0], 6, 9),
    ];
    for t in tests {
        let mountain_array = MountainArray { v: t.0 };
        assert_eq!(Solution::find_in_mountain_array(t.1, &mountain_array), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
