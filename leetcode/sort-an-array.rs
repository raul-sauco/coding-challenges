// 912. Sort an Array
// 🟠 Medium
//
// https://leetcode.com/problems/sort-an-array/
//
// Tags: Array - Divide and Conquer - Sorting - Heap (Priority Queue)
// - Merge Sort - Bucket Sort - Radix Sort - Counting Sort

struct Solution;
impl Solution {
    // Given the conditions of the problem description, merge sort seems to
    // be a good option, it won't use any extra memory and it guarantees
    // O(n*log(n)) time complexity.
    //
    // Time complexity: O(n*log(n))
    // Space complexity: O(n) - We use one copy of the input array to
    // alternately move elements from one to the other. The call stack will
    // be of height log(n), that is an extra O(log(n)).
    //
    // Runtime 46 ms Beats 90.32%
    // Memory 2.9 MB Beats 54.84%
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        // Define an internal function that sorts a section of the input array, this
        // avoids passing copies of the array between calls.
        fn merge_sort(a: &mut Vec<i32>, b: &mut Vec<i32>, l: usize, r: usize) {
            if l == r {
                return;
            }
            let mid = l + ((r - l) / 2);
            // Swap the source and destination arrays in each call.
            merge_sort(b, a, l, mid);
            merge_sort(b, a, mid + 1, r);
            merge(a, b, l, mid, r);
        }

        // A function that merges two sorted halves.
        fn merge(dest: &mut Vec<i32>, source: &mut Vec<i32>, l: usize, mid: usize, r: usize) {
            // The halves from l to mid and mid to r are sorted in the "source" array, we can
            // use elements from the sorted halves to update the elements in dest and end with
            // a completely sorted slice between l and r.
            let mut i = l;
            let mut j = mid + 1;
            let mut ins = l;
            while i <= mid && j <= r {
                if source[j] < source[i] {
                    dest[ins] = source[j];
                    j += 1;
                } else {
                    dest[ins] = source[i];
                    i += 1;
                }
                ins += 1;
            }
            // Use up any remaining elements from either half.
            while i <= mid {
                dest[ins] = source[i];
                i += 1;
                ins += 1;
            }
            while j <= r {
                dest[ins] = source[j];
                j += 1;
                ins += 1;
            }
        }
        // Use two mutable copies of the input array to avoid copying at each call level.
        let mut a = nums.clone();
        let mut b = nums.clone();
        merge_sort(&mut b, &mut a, 0, nums.len() - 1);
        b
    }

    // TODO add bucket sort solution. In Rust it could be more performant.

    // Use the built in sort function.
    //
    // Runtime 28 ms Beats 100%
    // Memory 2.8 MB Beats 67.74%
    pub fn _sort_array_built_in(nums: Vec<i32>) -> Vec<i32> {
        let mut n = nums.clone();
        n.sort_unstable();
        n
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0], vec![0]),
        (vec![1, 0], vec![0, 1]),
        (vec![5, 2, 1], vec![1, 2, 5]),
        (vec![5, 2, 3, 1], vec![1, 2, 3, 5]),
        (vec![5, 1, 1, 2, 0, 0], vec![0, 0, 1, 1, 2, 5]),
    ];
    for test in tests {
        assert_eq!(Solution::sort_array(test.0), test.1);
    }
    println!("All tests passed!")
}
