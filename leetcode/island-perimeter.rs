// 463. Island Perimeter
// 🟢 Easy
//
// https://leetcode.com/problems/island-perimeter/
//
// Tags: Array - Depth-First Search - Breadth-First Search - Matrix

struct Dir {
    x: i32,
    y: i32,
}

impl Dir {
    fn get_neighbors(&self) -> [Dir; 4] {
        [
            Dir {
                x: self.x + 1,
                y: self.y,
            },
            Dir {
                x: self.x - 1,
                y: self.y,
            },
            Dir {
                x: self.x,
                y: self.y + 1,
            },
            Dir {
                x: self.x,
                y: self.y - 1,
            },
        ]
    }

    fn is_land(&self, grid: &Vec<Vec<i32>>) -> bool {
        self.x >= 0
            && (self.x as usize) < grid[0].len()
            && self.y >= 0
            && (self.y as usize) < grid.len()
            && grid[self.y as usize][self.x as usize] == 1
    }

    fn get_outer_perimeter_length(&self, grid: &Vec<Vec<i32>>) -> i32 {
        let mut total = 4;
        for nei in self.get_neighbors() {
            if nei.is_land(grid) {
                total -= 1;
            }
        }
        total
    }
}

struct Solution;
impl Solution {
    /// Iterate the grid, for every land cell we land on, add any non-land neighbors to the
    /// perimeter count.
    ///
    /// Time complexity: O(m*n) - We visit every cell in the grid, for each land cell, we check
    /// four neighbors.
    /// Space complexity: O(1) - We only store the perimeter and the for loop counters.
    ///
    /// Runtime 12 ms Beats 16%
    /// Memory 2.26 MB Beats 66%
    #[allow(dead_code)]
    pub fn island_perimeter_with_structs(grid: Vec<Vec<i32>>) -> i32 {
        let mut perimeter = 0;
        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                if grid[r][c] == 1 {
                    perimeter += (Dir {
                        x: c as i32,
                        y: r as i32,
                    })
                    .get_outer_perimeter_length(&grid);
                }
            }
        }
        perimeter
    }

    /// Same solution but without the Dir struct.
    ///
    /// Time complexity: O(m*n) - We visit every cell in the grid, for each land cell, we check
    /// four neighbors.
    /// Space complexity: O(1) - We only store the perimeter and the for loop counters.
    ///
    /// Runtime 6 ms Beats 79%
    /// Memory 2.21 MB Beats 66%
    pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
        let (num_rows, num_cols) = (grid.len(), grid[0].len());
        let mut perimeter = 0;
        for r in 0..num_rows {
            for c in 0..num_cols {
                if grid[r][c] == 1 {
                    perimeter += 4;
                    if r > 0 {
                        perimeter -= grid[r - 1][c];
                    }
                    if r < num_rows - 1 {
                        perimeter -= grid[r + 1][c];
                    }
                    if c > 0 {
                        perimeter -= grid[r][c - 1];
                    }
                    if c < num_cols - 1 {
                        perimeter -= grid[r][c + 1];
                    }
                }
            }
        }
        perimeter
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1]], 4),
        (vec![vec![1, 0]], 4),
        (
            vec![
                vec![0, 1, 0, 0],
                vec![1, 1, 1, 0],
                vec![0, 1, 0, 0],
                vec![1, 1, 0, 0],
            ],
            16,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::island_perimeter(t.0.clone());
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
