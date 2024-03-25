// 407. Trapping Rain Water II
// 🔴 Hard
//
// https://leetcode.com/problems/trapping-rain-water-ii/
//
// Tags: Array - Breadth-First Search - Heap (Priority Queue) - Matrix

use serde::{Deserialize, Serialize};
use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};
use std::fs::File;
use std::io::Read;

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord, Hash)]
struct Cell {
    height: i32,
    x: i32,
    y: i32,
}

struct Dir {
    x: i32,
    y: i32,
}

struct Solution;
impl Solution {
    /// Similar concept to the first trapping rain water problem, the difference is that we need to
    /// keep track of the entire perimeter of the 3D matrix, where the 3rd dimension is the height,
    /// instead of only needing to keep track of the two ends. To determine where we can bring the
    /// perimeter in, we will use a min heap, implemented using a priority queue with the heights
    /// reversed. We start by adding the cells in the outer perimeter given that they cannot hold
    /// any water, then we iterate over the cell in the heap with the minimum height, pop it and
    /// check if it would hold any water, by checking its height against the previous min height of
    /// the current perimeter. If the cell height is less than the previous min height of the
    /// current perimeter cells, it would hold current min height - cell height water, if it is
    /// taller, then this is the new minimum height of the outer perimeter. Next we add any
    /// neighbors that we haven't visited yet to the min heap, marking them "seen" when we do.
    ///
    /// Time complexity: O(nmlog(nm)) - We will visit all cells and push-pop them from a heap of
    /// size m*n. We also iterate before that step to find the perimeter at m+n, but that gets
    /// trumped by the complexity of the while loop.
    /// Space complexity: O(mn) - Both the hashset and the priority queue can grow to the size of
    /// the matrix, depending on shape.
    ///
    /// Runtime 31 ms Beats 7%
    /// Memory 3.22 MB Beats 7%
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        let (num_rows, num_cols) = (height_map.len(), height_map[0].len());
        let mut seen: HashSet<(i32, i32)> = HashSet::new();
        for row in 0..num_rows {
            seen.insert((0, row as i32));
            seen.insert((num_cols as i32 - 1, row as i32));
        }
        for col in 0..num_cols {
            seen.insert((col as i32, 0));
            seen.insert((col as i32, num_rows as i32 - 1));
        }
        let mut pq: BinaryHeap<Reverse<Cell>> = seen
            .iter()
            .map(|c| {
                Reverse(Cell {
                    height: height_map[c.1 as usize][c.0 as usize],
                    x: c.0,
                    y: c.1,
                })
            })
            .collect();
        let mut water_collected = 0;
        // We start at the lowest height, we know the boundary cannot collect water.
        let mut current_height = 0;
        let mut cell_ref;
        let dirs = [
            Dir { x: 0, y: -1 },
            Dir { x: 0, y: 1 },
            Dir { x: -1, y: 0 },
            Dir { x: 1, y: 0 },
        ];
        let (mut x, mut y);
        while let Some(rev) = pq.pop() {
            cell_ref = rev.0;
            if cell_ref.height < current_height {
                water_collected += current_height - cell_ref.height;
            } else if cell_ref.height > current_height {
                current_height = cell_ref.height;
            }
            // Get the neighbors that we need to visit, could extract to a function.
            for dir in dirs.iter() {
                x = cell_ref.x + dir.x;
                y = cell_ref.y + dir.y;
                if x >= 0
                    && (x as usize) < num_cols
                    && y >= 0
                    && (y as usize) < num_rows
                    && !seen.contains(&(x, y))
                {
                    let cell = Cell {
                        height: height_map[y as usize][x as usize],
                        x,
                        y,
                    };
                    seen.insert((x, y));
                    pq.push(Reverse(cell));
                }
            }
        }
        water_collected
    }
}

// A struct representing the tests parsed from the JSON file.
#[derive(Debug, Serialize, Deserialize)]
struct Test {
    heights: Vec<Vec<i32>>,
    expected: i32,
}

// Tests.
fn main() {
    let file = File::open("trapping-rain-water-ii.json").expect("Unable to open file");
    let mut content = String::new();
    file.take(u64::MAX)
        .read_to_string(&mut content)
        .expect("Unable to read file");
    let tests: Vec<Test> = serde_json::from_str(&content).expect("Unable to parse JSON");
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::trap_rain_water(t.heights.clone());
        if res == t.expected {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.expected, res
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
