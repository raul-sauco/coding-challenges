use std::mem;

use bitvec::prelude::*;

advent_of_code::solution!(18);

const ITERATIONS: usize = if cfg!(test) { 4 } else { 100 };

#[derive(Debug)]
struct Grid {
    rows: Vec<BitVec>,
    num_rows: usize,
    num_cols: usize,
}

impl Grid {
    fn from_str(input: &str) -> Grid {
        let rows: Vec<BitVec> = input
            .lines()
            .map(|line| line.bytes().map(|b| matches!(b, b'#')).collect::<BitVec>())
            .collect();
        Grid {
            num_rows: rows.len(),
            num_cols: rows[0].len(),
            rows,
        }
    }

    // Creates a new grid with the given size and all its cells initialized to false
    fn with_size(num_rows: usize, num_cols: usize) -> Grid {
        Grid {
            rows: vec![bitvec![0; num_cols]; num_rows],
            num_rows,
            num_cols,
        }
    }

    fn render_next_grid(&self, next: &mut Grid) {
        let mut on_nei;
        for r in 0..self.num_rows {
            for c in 0..self.num_cols {
                on_nei = self.count_on_neighbors(r, c);
                next.rows[r].set(
                    c,
                    match self.rows[r][c] {
                        true => on_nei == 2 || on_nei == 3,
                        false => on_nei == 3,
                    },
                );
            }
        }
    }

    fn count_on_neighbors(&self, r: usize, c: usize) -> u8 {
        let mut res = 0;
        if r > 0 {
            if c > 0 && self.rows[r - 1][c - 1] {
                res += 1;
            }
            if self.rows[r - 1][c] {
                res += 1;
            }
            if c < self.num_cols - 1 && self.rows[r - 1][c + 1] {
                res += 1;
            }
        }
        if c > 0 && self.rows[r][c - 1] {
            res += 1;
        }
        if c < self.num_cols - 1 && self.rows[r][c + 1] {
            res += 1;
        }
        if r < self.num_rows - 1 {
            if c > 0 && self.rows[r + 1][c - 1] {
                res += 1;
            }
            if self.rows[r + 1][c] {
                res += 1;
            }
            if c < self.num_cols - 1 && self.rows[r + 1][c + 1] {
                res += 1;
            }
        }
        res
    }

    fn on_count(&self) -> usize {
        self.rows.iter().map(|row| row.count_ones()).sum()
    }

    #[allow(dead_code)]
    fn to_str(&self) -> String {
        let mut res = String::with_capacity(self.num_rows * self.num_cols);
        for row in self.rows.iter() {
            for b in row.iter().by_vals() {
                res.push(if b { '#' } else { '.' });
            }
            res.push('\n');
        }
        res
    }

    fn corners_on(&mut self) {
        self.rows[0].set(0, true);
        self.rows[0].set(self.num_cols - 1, true);
        self.rows[self.num_rows - 1].set(0, true);
        self.rows[self.num_rows - 1].set(self.num_cols - 1, true);
    }
}

pub fn part_one(input: &str) -> Option<u64> {
    let mut current = Grid::from_str(input);
    let mut next = Grid::with_size(current.num_rows, current.num_cols);
    for _ in 0..ITERATIONS {
        current.render_next_grid(&mut next);
        mem::swap(&mut current, &mut next);
    }
    Some(current.on_count() as u64)
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut current = Grid::from_str(input);
    let mut next = Grid::with_size(current.num_rows, current.num_cols);
    for _ in 0..ITERATIONS {
        current.corners_on();
        current.render_next_grid(&mut next);
        mem::swap(&mut current, &mut next);
    }
    current.corners_on();
    Some(current.on_count() as u64)
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4));
    }

    #[rstest]
    #[case(
        "##.#.#
...##.
#....#
..#...
#.#..#
####.#",
        14 // 17 after 5 iterations but 14 after 4
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_two(input), Some(expected));
    }
}
