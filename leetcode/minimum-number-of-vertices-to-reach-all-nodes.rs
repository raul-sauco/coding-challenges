// 1557. Minimum Number of Vertices to Reach All Nodes
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
//
// Tags: Graph

struct Solution {}

/// Create a vector of boolean values of size n initialized to false. Iterate
/// over the edges marking each destination vertex as reachable, then use a
/// second loop to iterate over the visited vector keeping only the values that
/// we did not visit, these correspond to vertices that have an indegree of 0,
/// we can return a vector with these vertices as the result.
///
/// Time complexity: O(e+n) - We first iterate all edges e, then all vertices n
/// to find the ones that have an indegree of 0.
/// Space complexity: O(n) - We use a vector of extra memory that has size n.
///
/// Runtime 34 ms Beats 52.94%
/// Memory 8.8 MB Beats 100%
impl Solution {
    pub fn find_smallest_set_of_vertices(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let mut visited = vec![false; n as usize];
        for edge in edges {
            visited[edge[1] as usize] = true;
        }
        visited
            .into_iter()
            .enumerate()
            .filter(|(_, x)| !*x)
            .map(|(idx, _)| idx as i32)
            .collect::<Vec<i32>>()
    }
}

// Tests.
fn main() {
    let tests = vec![
        (
            6,
            vec![vec![0, 1], vec![0, 2], vec![2, 5], vec![3, 4], vec![4, 2]],
            vec![0, 3],
        ),
        (
            5,
            vec![vec![0, 1], vec![2, 1], vec![3, 1], vec![1, 4], vec![2, 4]],
            vec![0, 2, 3],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::find_smallest_set_of_vertices(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
