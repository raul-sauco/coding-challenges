// 752. Open the Lock
// 🟠 Medium
//
// https://leetcode.com/problems/open-the-lock/
//
// Tags: Array - Hash Table - String - Breadth-First Search

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};
use std::mem::swap;

#[derive(Debug, Eq, PartialEq, Hash, Ord, PartialOrd, Clone)]
struct Combination {
    a: char,
    b: char,
    c: char,
    d: char,
}

impl Combination {
    fn from_string(s: String) -> Self {
        let v = s.chars().collect::<Vec<_>>();
        if v.len() != 4 {
            panic!("Strings should only have len 4 and be ASCII");
        }
        Self {
            a: v[0],
            b: v[1],
            c: v[2],
            d: v[3],
        }
    }

    fn get_neighbors(self) -> [Self; 8] {
        [
            Self {
                a: Combination::get_digit_up(self.a),
                ..self
            },
            Self {
                a: Combination::get_digit_down(self.a),
                ..self
            },
            Self {
                b: Combination::get_digit_up(self.b),
                ..self
            },
            Self {
                b: Combination::get_digit_down(self.b),
                ..self
            },
            Self {
                c: Combination::get_digit_up(self.c),
                ..self
            },
            Self {
                c: Combination::get_digit_down(self.c),
                ..self
            },
            Self {
                d: Combination::get_digit_up(self.d),
                ..self
            },
            Self {
                d: Combination::get_digit_down(self.d),
                ..self
            },
        ]
    }

    fn get_digit_up(c: char) -> char {
        match c {
            '0' => '1',
            '1' => '2',
            '2' => '3',
            '3' => '4',
            '4' => '5',
            '5' => '6',
            '6' => '7',
            '7' => '8',
            '8' => '9',
            '9' => '0',
            _ => panic!("Unrecognized combo digit {}", c),
        }
    }

    fn get_digit_down(c: char) -> char {
        match c {
            '0' => '9',
            '1' => '0',
            '2' => '1',
            '3' => '2',
            '4' => '3',
            '5' => '4',
            '6' => '5',
            '7' => '6',
            '8' => '7',
            '9' => '8',
            _ => panic!("Unrecognized combo digit {}", c),
        }
    }

    fn get_levenshtein_distance(&self, other: &Combination) -> u32 {
        fn get_digit_distance(from: u32, to: u32) -> u32 {
            if from > to {
                return get_digit_distance(to, from);
            }
            if from == to {
                return 0;
            }
            let val = to - from;
            if val > 5 {
                10 - val
            } else {
                val
            }
        }
        get_digit_distance(self.a as u32, other.a as u32)
            + get_digit_distance(self.b as u32, other.b as u32)
            + get_digit_distance(self.c as u32, other.c as u32)
            + get_digit_distance(self.d as u32, other.d as u32)
    }

    fn to_string(&self) -> String {
        [self.a, self.b, self.c, self.d].iter().collect()
    }
}

struct Solution;
impl Solution {
    /// Use a variation of the A* algorithm that uses the absolute difference between each digit in
    /// a value and the target as the heuristic and visits first values that are "closer".
    ///
    /// Time complexity: O(n*log(n)) - Where n is the number of different combinations and it peaks
    /// at 10000. We could end up visiting each combination and pushing/popping them all from the
    /// heap at log(n) per push/pop.
    /// Space complexity: O(n) - The seen/deadends hashset and the heap can both grow to that size.
    ///
    /// Runtime 77 ms Beats 46%
    /// Memory 3.18 MB Beats 30%
    #[allow(dead_code)]
    pub fn open_lock_astar(deadends: Vec<String>, target: String) -> i32 {
        if target == "0000" {
            return 0;
        }
        let target = Combination::from_string(target);
        let start = Combination::from_string("0000".to_string());
        let mut heap = BinaryHeap::from([(
            Reverse(0),
            Reverse(target.get_levenshtein_distance(&start)),
            start,
        )]);
        // Deadends doubles up as "seen" hashset.
        let mut deadends = deadends.into_iter().collect::<HashSet<_>>();
        if deadends.contains("0000") {
            return -1;
        }
        while let Some((moves, _dist, node)) = heap.pop() {
            for nei in node.get_neighbors() {
                if nei == target {
                    return moves.0 + 1;
                }
                // Avoid pushing deadends into the heap instead of pushing then discarding.
                if !deadends.contains(&nei.to_string()) {
                    deadends.insert(nei.to_string());
                    heap.push((
                        Reverse(moves.0 + 1),
                        Reverse(target.get_levenshtein_distance(&nei)),
                        nei,
                    ));
                }
            }
        }
        -1
    }

    /// Since using an heuristic and the binary heap didn't work as well as I expected, I tried
    /// with a simple BFS but the result was not that good either.
    ///
    /// Time complexity: O(n) - Where n is the number of different combinations and it peaks
    /// at 10000. We could end up visiting each combination and pushing/popping them all from the
    /// queue at O(1) per push/pop.
    /// Space complexity: O(n) - The seen/deadends hashset can both grow to 10000, the queue and
    /// next can grow to the size of a level which grows exponentially and I believe can be a max
    /// of n/2 because it will be 1 => 8 => 64 ... but it cannot include nodes seen previously.
    ///
    /// Runtime 75 ms Beats 46%
    /// Memory 3.02 MB Beats 46%
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        if target == "0000" {
            return 0;
        }
        let target = Combination::from_string(target);
        let start = Combination::from_string("0000".to_string());
        let mut queue = vec![start];
        // Deadends doubles up as "seen" hashset.
        let mut deadends = deadends.into_iter().collect::<HashSet<_>>();
        if deadends.contains("0000") {
            return -1;
        }
        let mut moves = 0;
        let mut next = vec![];
        while !queue.is_empty() {
            for node in &queue {
                for nei in node.clone().get_neighbors() {
                    if nei == target {
                        return moves + 1;
                    }
                    // Avoid pushing deadends into the heap instead of pushing then discarding.
                    if !deadends.contains(&nei.to_string()) {
                        deadends.insert(nei.to_string());
                        next.push(nei);
                    }
                }
            }
            swap(&mut queue, &mut next);
            next.clear();
            moves += 1;
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["8888"], "0009", 1),
        (vec!["0000"], "8888", -1),
        (vec!["0201", "0101", "0102", "1212", "2002"], "0202", 6),
        (vec!["0201", "0101", "0102", "1212", "2002"], "0201", 3),
        (
            vec![
                "8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888",
            ],
            "8888",
            -1,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::open_lock(t.0.iter().map(|s| s.to_string()).collect(), t.1.to_string());
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
