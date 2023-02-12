// 2477. Minimum Fuel Cost to Report to the Capital
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Graph

struct Solution;
impl Solution {
    // We can use a postorder DFS, each node returns the number of people
    // traveling and the amount of gas consumed to get everyone there, the
    // parent looks at the number of people and computes the cost of getting
    // everyone from the child to itself, then adds up all the costs plus
    // the representative starting the journey there and returns that
    // information to the parent.
    //
    // Time complexity: O(n) - We visit each node twice, once in the
    // traversal and once when computing the results using the children's
    // returns.
    // Space complexity: O(n) - The call stack could grow to size n with a
    // skewed tree.
    //
    // Runtime 68 ms Beats 100%
    // Memory 24.5 MB Beats 45.45%
    pub fn minimum_fuel_cost(roads: Vec<Vec<i32>>, seats: i32) -> i64 {
        // Build an adjacency list.
        let mut adj: Vec<Vec<i32>> = vec![vec![]; roads.len() + 1];
        for road in roads {
            adj[road[0] as usize].push(road[1]);
            adj[road[1] as usize].push(road[0]);
        }
        // Define a recursive function that returns the number of people
        // traveling up-tree from a certain node and the amount of fuel
        // that they used to get there.
        fn dfs(node: &i32, parent: &i32, adj: &Vec<Vec<i32>>, seats: i64) -> Vec<i64> {
            let mut fuel = 0;
            let mut passengers = 1;
            for child in &adj[*node as usize] {
                if child == parent {
                    continue;
                }
                let res = dfs(child, node, &adj, seats);
                // Perform ceil(res[1] / seats). The cost of the passengers traveling from
                // the child to the current node.
                let edge_cost = if res[1] % seats == 0 {
                    res[1] / seats
                } else {
                    res[1] / seats + 1
                };
                // Fuel cost is the current fuel cost, plus the cost they incurred on
                // getting to the child node, plus the cost of traveling from the node
                // to this parent.
                fuel += res[0] + edge_cost;
                passengers += res[1];
            }
            vec![fuel, passengers]
        }
        dfs(&0, &-1, &adj, seats as i64)[0]
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::minimum_fuel_cost(vec![vec![0, 1], vec![0, 2], vec![0, 3]], 5),
        3
    );
    assert_eq!(
        Solution::minimum_fuel_cost(
            vec![
                vec![3, 1],
                vec![3, 2],
                vec![1, 0],
                vec![0, 4],
                vec![0, 5],
                vec![4, 6]
            ],
            2
        ),
        7
    );
    println!("All tests passed!")
}
