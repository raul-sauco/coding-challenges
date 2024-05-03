// 165. Compare Version Numbers
// 🟠 Medium
//
// https://leetcode.com/problems/compare-version-numbers/
//
// Tags: Two Pointers - String

use std::cmp::Ordering;

#[derive(Eq, Debug)]
struct Version {
    pub revisions: Vec<u32>,
}

impl Version {
    fn from_string(input: String) -> Self {
        Self {
            revisions: input
                .split('.')
                .map(|x| x.parse::<u32>().unwrap())
                .collect::<Vec<u32>>(),
        }
    }

    fn get_revision(&self, idx: usize) -> u32 {
        *self.revisions.get(idx).unwrap_or(&0)
    }
}

impl Ord for Version {
    fn cmp(&self, other: &Self) -> Ordering {
        let mut i = 0;
        while i < self.revisions.len() || i < other.revisions.len() {
            match self.get_revision(i).cmp(&other.get_revision(i)) {
                Ordering::Less => {
                    return Ordering::Less;
                }
                Ordering::Equal => {
                    i += 1;
                }
                Ordering::Greater => {
                    return Ordering::Greater;
                }
            }
        }
        Ordering::Equal
    }
}

impl PartialOrd for Version {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Version {
    fn eq(&self, other: &Self) -> bool {
        self.revisions == other.revisions
    }
}

struct Solution;
impl Solution {
    /// We can create a clean solution using Rust type system, use the definitions in the problem
    /// description to create a Version with a property consisting of a vec of revisions. Implement
    /// cmp by comparing revisions taking care of providing a default 0 value when trying to get an
    /// empty revision.
    ///
    /// Time complexity: O(n+m) - We iterate over all the revisions in both input strings.
    /// Space complexity: O(n+m) - We create a "Version" out of each input string.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.15 MB Beats 71%
    #[allow(dead_code)]
    pub fn compare_version_struct(version1: String, version2: String) -> i32 {
        match Version::from_string(version1).cmp(&Version::from_string(version2)) {
            Ordering::Less => -1,
            Ordering::Equal => 0,
            Ordering::Greater => 1,
        }
    }

    /// Clean solution with a very different approach. Found @: 2912748. Interesting way to use the
    /// match arms to provide default values when one of them is none.
    ///
    /// Time complexity: O(max(m,n)) - We may stop iterating at the first revision if they are
    /// different, but we could iterate over all the way to the end of the longest version string
    /// if the revisions keep matching.
    /// Space complexity: O(1) - We use iterators.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.08 MB Beats 71%
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let mut it1 = version1.split('.').map(|r| r.parse().unwrap());
        let mut it2 = version2.split('.').map(|r| r.parse().unwrap());
        loop {
            match (it1.next(), it2.next()) {
                // Match when r2 is some and greater than r1 or 0 if r1 is None.
                (r1, Some(r2)) if r2 > r1.unwrap_or(0) => return -1,
                // Match when r1 is some and greater than r2 or 0 if r2 is None.
                (Some(r1), r2) if r1 > r2.unwrap_or(0) => return 1,
                (None, None) => return 0,
                // Continue when none of the other branches match, for example one is None and the
                // other 0.
                _ => continue,
            }
        }
    }
}

// Tests.
fn main() {
    let tests = [
        ("1.01", "1.001", 0),
        ("1.0", "1.0.0", 0),
        ("0.1", "1.1", -1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::compare_version(t.0.to_string(), t.1.to_string());
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
