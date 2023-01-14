// 1061. Lexicographically Smallest Equivalent String
// 🟠 Medium
//
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
//
// Tags: String - Union Find

struct Solution;
impl Solution {
    // Use union find by rank where the rank is the reversed lexicographical
    // order of the characters to be joined.
    //
    // Time complexity: O(n) - Where n is the number of characters in the
    // input, we visit all characters in s1 and s2 to construct the union
    // find structure, then we visit all characters in base str to find their
    // lexicographically smallest equivalents, the find parent operation runs
    // in amortized O(1) because it uses path compression.
    // Space complexity: O(1) - The parents array has size 26.
    //
    // Runtime 1 ms Beats 100%
    // Memory 2 MB Beats 100%
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        // A nested function that finds the representative of a disjoint set,
        // in this problem the representative consists of the lexicographically
        // smallest member of the group.
        fn find_parent(parents: &mut Vec<usize>, a: usize) -> usize {
            if a == parents[a] {
                return a;
            }
            parents[a] = find_parent(parents, parents[a]);
            parents[a]
        }
        // Merge two disjoint sets into one with the lexicographically
        // smaller parent as the parent of the merged result.
        fn union(parents: &mut Vec<usize>, a: usize, b: usize) {
            let pa = find_parent(parents, a);
            let pb = find_parent(parents, b);
            // Join the set with the lexicographically greater parent into
            // the set with the lexicographically smaller parent.
            if pb < pa {
                parents[pa] = pb
            } else {
                parents[pb] = pa
            }
        }
        let chars_a = s1.chars().collect::<Vec<char>>();
        let chars_b = s2.chars().collect::<Vec<char>>();
        // Initialize an array of parents, each char points to itself.
        let mut parents: Vec<usize> = (0..26).into_iter().collect();
        // The base that we need to subtract to the index.
        let base = 'a' as u8;
        // Create all the disjoint group and find their representatives.
        for i in 0..chars_a.len() {
            union(
                &mut parents,
                (chars_a[i] as u8 - base) as usize,
                (chars_b[i] as u8 - base) as usize,
            );
        }
        // Use the disjoint groups to create the lexicographically lowest equivalent.
        let mut res = String::new();
        for c in base_str.chars() {
            res.push((find_parent(&mut parents, (c as u8 - base) as usize) as u8 + base) as char)
        }
        res
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::smallest_equivalent_string(
            String::from("parker"),
            String::from("morris"),
            String::from("parser")
        ),
        "makkek"
    );
    assert_eq!(
        Solution::smallest_equivalent_string(
            String::from("hello"),
            String::from("world"),
            String::from("hold")
        ),
        "hdld"
    );
    assert_eq!(
        Solution::smallest_equivalent_string(
            String::from("leetcode"),
            String::from("programs"),
            String::from("sourcecode")
        ),
        "aauaaaaada"
    );
    println!("All tests passed!")
}
