// 2709. Greatest Common Divisor Traversal
// 🔴 Hard
//
// https://leetcode.com/problems/greatest-common-divisor-traversal/
//
// Tags: Array - Math - Union Find - Number Theory

use std::collections::{HashMap, HashSet};

struct UnionFind {
    parents: Vec<usize>,
    rank: Vec<usize>,
    components: usize,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            parents: (0..n).collect(),
            rank: vec![1; n],
            components: n,
        }
    }

    fn find_parent(&mut self, a: usize) -> usize {
        if a != self.parents[a] {
            self.parents[a] = self.find_parent(self.parents[a]);
        }
        self.parents[a]
    }

    fn union(&mut self, a: usize, b: usize) {
        let (pa, pb) = (self.find_parent(a), self.find_parent(b));
        if pa == pb {
            return;
        }
        if self.rank[pb] > self.rank[pa] {
            return self.union(b, a);
        }
        self.parents[pb] = pa;
        self.rank[pa] += self.rank[pb];
        self.components -= 1;
    }
}

struct Solution;
impl Solution {
    /// A really interesting problem, combining elements of graphs with some math. The numbers in
    /// the input can be seen as nodes in a graph, the edges can be computed factorizing the
    /// numbers, any two values that share a common factor are connected, the graph is undirected,
    /// the problem asks us to determine if the graph is connected. The simplest way to compute the
    /// number of disjoint components in a graph is to use Union Find, if the graph has one
    /// component, it is connected, otherwise it isn't. We can initialize a union find structure,
    /// and a hashmap that keeps factors as keys and the index of a representative of that factor
    /// groups as the value, for each factor in a number, if we have seen that factor previously,
    /// we union the current index to that set, if we haven't we initialize a new set and use the
    /// current index as the representative. Since we know that the values are limited to 100000,
    /// we can optimize the computation of factors using an array of hardcoded primes, this array
    /// contains the 64 primes found between 2 and sqr(100000), any prime that is a factor of an
    /// input value we will obtain as the remainder of having removed all the prime factors up to,
    /// and including, 311. For example, the next prime 317, will need to be combined with a prime
    /// <= 311, because 317^2 = 100489.
    ///
    /// Time complexity: O(n) - Filtering duplicates is O(n), then iterating over the input is O(n)
    /// as well, because in the inner loop we iterate a fixed number of times, 64, calling the
    /// union operation in the union find structure is amortized O(1).
    /// Space complexity: O(n) - The union-find structure, and the representatives hashmap both can
    /// grow to size n. The representatives hashmap is more likely going to be closer to size 64,
    /// but that is not guaranteed, for example, every element in the input could be a prime > 311,
    /// each would result in an entry in the representatives set.
    ///
    /// Runtime 55 ms Beats 100%
    /// Memory 4.34 MB Beats 100%
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        if nums.len() == 1 {
            return true;
        }
        // No point in keeping duplicate values around.
        let nums = nums
            .into_iter()
            .collect::<HashSet<_>>()
            .into_iter()
            .collect::<Vec<_>>();
        let n = nums.len();
        let mut uf = UnionFind::new(n);
        let primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
            89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
            181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271,
            277, 281, 283, 293, 307, 311,
        ];
        // A hashmap, given a factor, points to the index of a value in that component.
        let mut representatives: HashMap<i32, usize> = HashMap::new();
        let mut val;
        for (idx, num) in nums.iter().enumerate() {
            val = *num;
            if val == 1 {
                return false;
            }
            for &prime in primes.iter() {
                if val % prime == 0 {
                    if let Some(&i) = representatives.get(&prime) {
                        uf.union(idx, i);
                    } else {
                        representatives.insert(prime, idx);
                    }
                }
                while val % prime == 0 {
                    val /= prime;
                }
            }
            if val != 1 {
                // The remainder is also a prime, it could be a factor in some other value.
                if let Some(&i) = representatives.get(&val) {
                    uf.union(idx, i);
                } else {
                    representatives.insert(val, idx);
                }
            }
        }
        uf.components == 1
    }

    /// Same logic as the previous solution but it runs faster because it stops checking primes
    /// once the square of the current prime is greater than the value being factorized.
    ///
    /// Time complexity: O(n) - Same as before.
    /// Space complexity: O(n) - Same as before.
    ///
    /// Runtime 30 ms Beats 100%
    /// Memory 4.54 MB Beats 100%
    #[allow(dead_code)]
    pub fn can_traverse_all_pairs_quad(nums: Vec<i32>) -> bool {
        if nums.len() == 1 {
            return true;
        }
        // No point in keeping duplicate values around.
        let nums = nums
            .into_iter()
            .collect::<HashSet<_>>()
            .into_iter()
            .collect::<Vec<_>>();
        let n = nums.len();
        let mut uf = UnionFind::new(n);
        let primes = [
            (2, 4),
            (3, 9),
            (5, 25),
            (7, 49),
            (11, 121),
            (13, 169),
            (17, 289),
            (19, 361),
            (23, 529),
            (29, 841),
            (31, 961),
            (37, 1369),
            (41, 1681),
            (43, 1849),
            (47, 2209),
            (53, 2809),
            (59, 3481),
            (61, 3721),
            (67, 4489),
            (71, 5041),
            (73, 5329),
            (79, 6241),
            (83, 6889),
            (89, 7921),
            (97, 9409),
            (101, 10201),
            (103, 10609),
            (107, 11449),
            (109, 11881),
            (113, 12769),
            (127, 16129),
            (131, 17161),
            (137, 18769),
            (139, 19321),
            (149, 22201),
            (151, 22801),
            (157, 24649),
            (163, 26569),
            (167, 27889),
            (173, 29929),
            (179, 32041),
            (181, 32761),
            (191, 36481),
            (193, 37249),
            (197, 38809),
            (199, 39601),
            (211, 44521),
            (223, 49729),
            (227, 51529),
            (229, 52441),
            (233, 54289),
            (239, 57121),
            (241, 58081),
            (251, 63001),
            (257, 66049),
            (263, 69169),
            (269, 72361),
            (271, 73441),
            (277, 76729),
            (281, 78961),
            (283, 80089),
            (293, 85849),
            (307, 94249),
            (311, 96721),
        ];
        // A hashmap, given a factor, points to the index of a value in that component.
        let mut representatives: HashMap<i32, usize> = HashMap::new();
        let mut val;
        for (idx, num) in nums.iter().enumerate() {
            val = *num;
            if val == 1 {
                return false;
            }
            for &(prime, quad) in primes.iter() {
                if quad > val {
                    break;
                }
                if val % prime == 0 {
                    if let Some(&i) = representatives.get(&prime) {
                        uf.union(idx, i);
                    } else {
                        representatives.insert(prime, idx);
                    }
                }
                while val % prime == 0 {
                    val /= prime;
                }
            }
            if val != 1 {
                // The remainder is also a prime, it could be a factor in some other value.
                if let Some(&i) = representatives.get(&val) {
                    uf.union(idx, i);
                } else {
                    representatives.insert(val, idx);
                }
            }
        }
        uf.components == 1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], true),
        (vec![1, 1], false),
        (vec![2, 3, 6], true),
        (vec![3, 9, 5], false),
        (vec![4, 3, 12, 8], true),
        (vec![10007, 20014], true),
        (
            vec![
                42, 40, 45, 42, 50, 33, 30, 45, 33, 45, 30, 36, 44, 1, 21, 10, 40, 42, 42,
            ],
            false,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::can_traverse_all_pairs(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.1, res
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
