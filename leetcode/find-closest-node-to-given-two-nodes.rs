// 2359. Find Closest Node to Given Two Nodes
// 🟠 Medium
//
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
//
// Tags: Depth-First Search - Breadth-First Search - Graph

struct Solution;
impl Solution {
    // We can compute the distance between the start nodes and all other
    // nodes using BFS, since the nodes have, at most, one outgoing edge, we
    // don't need to use a queue or stack and can simply keep a pointer to
    // the next node. Compute all distances from one of the start nodes, then
    // compute the distances from the other node while checking if the
    // current node has the minimum maximal distance to either node1 or node2.
    //
    // Time complexity: O(n) - We iterate twice over a max of all the nodes
    // in the input.
    // Space complexity: O(n) - We keep two arrays of size n and a few
    // pointers.
    //
    // Runtime 18 ms Beats 100%
    // Memory 4.6 MB Beats 50%
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        let n = edges.len();
        // Make our own infinity value to avoid different types, quicker than calling
        // usize::MAX at every point.
        let inf = usize::MAX;
        let mut res = (inf, inf);
        let mut d1 = vec![inf; n];
        let mut d2 = vec![inf; n];
        let mut steps = 0;
        let mut current = node1 as usize;
        while current != inf && d1[current] == inf {
            d1[current] = steps;
            steps += 1;
            current = edges[current] as usize;
        }
        steps = 0;
        current = node2 as usize;
        while current != inf && d2[current] == inf {
            d2[current] = steps;
            let dist = steps.max(d1[current]);
            if dist < res.0 || (dist != inf && dist == res.0 && current < res.1) {
                res = (dist, current);
            }
            steps += 1;
            current = edges[current] as usize;
        }
        res.1 as i32
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::closest_meeting_node(vec![1, 2, -1], 0, 2), 2);
    assert_eq!(Solution::closest_meeting_node(vec![2, 2, 3, -1], 0, 1), 2);
    assert_eq!(
        Solution::closest_meeting_node(vec![4, 4, 4, 5, 1, 2, 2], 1, 1),
        1
    );
    assert_eq!(
        Solution::closest_meeting_node(vec![4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6),
        1
    );
    assert_eq!(
        Solution::closest_meeting_node(
            vec![-1, 7, 15, 15, -1, 4, 16, 2, 16, 7, 11, 6, 10, 4, 9, 1, 14, -1],
            1,
            6
        ),
        7
    );
    println!("All tests passed!")
}
