// 1232. Check If It Is a Straight Line
// 🟢 Easy
//
// https://leetcode.com/problems/check-if-it-is-a-straight-line/
//
// Tags: Array - Math - Geometry

struct Solution;
impl Solution {
    /// For all the points to be in the same line, they have to satisfy the
    /// same linear equation y = mx+b, compute m and b using two points and
    /// check if the rest of the points satisfy the condition.
    ///
    /// Time complexity: O(n) - We compute m and b in linear time, then iterate
    /// over all the points to check if they satisfy the equation.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 2 ms Beats 90%
    /// Memory 2 MB Beats 90%
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        if coordinates.len() < 3 {
            return true;
        }
        let (ax, ay) = (coordinates[0][0] as f32, coordinates[0][1] as f32);
        let (bx, by) = (coordinates[1][0] as f32, coordinates[1][1] as f32);
        let m = if ax == bx {
            f32::MAX
        } else {
            (ay - by) / (ax - bx)
        };
        let b = ay - m * ax;
        for point in coordinates {
            let (x, y) = (point[0] as f32, point[1] as f32);
            if m == f32::MAX {
                if x != ax {
                    return false;
                }
            } else if y != m * x + b {
                return false;
            }
        }
        true
    }

    /// The slope between any two points needs to be the same, fix one point
    /// and make sure that the slope between that point and any other remains
    /// constant.
    ///
    /// Time complexity: O(n) - We do one check per point.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 90%
    pub fn check_straight_line_2(coordinates: Vec<Vec<i32>>) -> bool {
        let (ax, ay) = (coordinates[0][0], coordinates[0][1]);
        let (bx, by) = (coordinates[1][0], coordinates[1][1]);
        for point in coordinates {
            let (x, y) = (point[0], point[1]);
            if (bx - ax) * (y - by) != (x - bx) * (by - ay) {
                return false;
            }
        }
        true
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![0, 0], vec![0, 1], vec![0, -1]], true),
        (
            vec![
                vec![1, 2],
                vec![2, 3],
                vec![3, 4],
                vec![4, 5],
                vec![5, 6],
                vec![6, 7],
            ],
            true,
        ),
        (
            vec![
                vec![1, 1],
                vec![2, 2],
                vec![3, 4],
                vec![4, 5],
                vec![5, 6],
                vec![7, 7],
            ],
            false,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::check_straight_line(t.0.clone()), t.1);
        assert_eq!(Solution::check_straight_line_2(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
