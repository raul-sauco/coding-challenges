// 1146. Snapshot Array
// 🟠 Medium
//
// https://leetcode.com/problems/snapshot-array/
//
// Tags: Array - Hash Table - Binary Search - Design

struct SnapshotArray {
    vals: Vec<Vec<(i32, i32)>>,
    next_snapshot: i32,
}

/// Use a vector of vectors of the given length to insert items, we store the
/// value of the last snapshot, when we insert an item, we do so by inserting
/// a tuple where the first value is the current snapshot index and the second
/// is the actual value, that results in each index of the SnapShot vals vector
/// containing a vector of all elements at that index indexed by their snapshot
/// value at the time of insertion. When we need to return a value at a given
/// index and snapshot, we can binary search the last value where snapshot idx
/// is less than or equal to the given snapshot idx.
///
/// Time complexity: O(m*log(n)) - Where m is the number of calls to the get
/// method and n is the number of items at the index that contains the most
/// elements, and it could also be equal to the number of calls to set. Given
/// an index, we binary search on the snapshot array[idx] of size n.
/// Space complexity: O(m) - Where m is the number of calls to set. We create
/// an entry for each call.
///
/// Runtime 91 ms Beats 84.21%
/// Memory 24.6 MB Beats 47.37%
impl SnapshotArray {
    fn new(length: i32) -> Self {
        let n = length as usize;
        let vals: Vec<Vec<(i32, i32)>> = (0..n).into_iter().map(|_| vec![(-1, 0)]).collect();
        let next_snapshot = 0;
        SnapshotArray {
            vals,
            next_snapshot,
        }
    }

    fn set(&mut self, index: i32, val: i32) {
        let idx = index as usize;
        let last_idx = self.vals[idx].len() - 1;
        if self.vals[idx][last_idx].0 == self.next_snapshot {
            self.vals[idx][last_idx].1 = val;
        } else {
            self.vals[index as usize].push((self.next_snapshot, val));
        }
    }

    fn snap(&mut self) -> i32 {
        self.next_snapshot += 1;
        self.next_snapshot - 1
    }

    fn get(&self, index: i32, snap_id: i32) -> i32 {
        let arr = &self.vals[index as usize];
        let (mut l, mut r) = (0, arr.len() - 1);
        let mut mid: usize;
        while l <= r {
            mid = (l + r) / 2;
            if arr[mid].0 <= snap_id {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        arr[l - 1].1
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */

// Tests.
fn main() {
    let mut sa = SnapshotArray::new(3);
    sa.set(0, 5);
    assert_eq!(sa.snap(), 0);
    sa.set(0, 6);
    assert_eq!(sa.get(0, 0), 5);

    let mut sa2 = SnapshotArray::new(1);
    sa2.set(0, 4);
    sa2.set(0, 16);
    sa2.set(0, 13);
    assert_eq!(sa2.snap(), 0);
    assert_eq!(sa2.get(0, 0), 13);
    assert_eq!(sa2.snap(), 1);
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
