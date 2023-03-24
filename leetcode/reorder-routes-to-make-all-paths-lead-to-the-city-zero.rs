// 1466. Reorder Routes to Make All Paths Lead to the City Zero
// 🟠 Medium
//
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
//
// Tags: Depth-First Search - Breadth-First Search - Graph

use std::collections::HashSet;

struct Solution;
impl Solution {
    /**
     * Since we have n-1 roads and we are guaranteed that we will be able to
     * reach the root from all nodes after reversing some, or none, roads,
     * that means that there is one road between any two nodes. We can use
     * two structures, a set of nodes that we have visited, and a stack, or
     * queue, or nodes that are able to get to the root node, as well as a
     * counter of the number of connections that we need to reverse. We start
     * by visiting 0 and checking all the roads that are connected to it, any
     * road that leads away from 0, will need to be reversed, we do it, and
     * add the node at the end of that road to the stack to be processed
     * because that node now can access the root node, when the road leads to
     * the node that we are visiting, we add the source node to the stack to
     * be processed.
     *
     * Time complexity: O(n) - Even though we have nested loops, the inner
     * loop will run only a total of 2*(n-1) times, which is the number of
     * connections that we have in our "roads" structure .
     * Space complexity: O(n) - The roads structure will have 2*(n-1)
     * elements, the stack could grow to size n and the set will grow to size
     * n because we will visit all nodes.
     *
     * Runtime 63 ms Beats 65%
     * Memory 8.5 MB Beats 95%
     */
    pub fn min_reorder(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut c: Vec<Vec<(usize, usize)>> = vec![vec![]; n];
        for connection in connections {
            let (a, b) = (connection[0] as usize, connection[1] as usize);
            c[a].push((a, b));
            c[b].push((a, b));
        }
        let mut needs_reversing = 0;
        let mut stack = vec![0];
        let mut seen = HashSet::<usize>::new();
        seen.insert(0);
        while !stack.is_empty() {
            match stack.pop() {
                Some(current) => {
                    for (a, b) in &c[current] {
                        if *a == current {
                            if !seen.contains(&b) {
                                seen.insert(*b);
                                needs_reversing += 1;
                                stack.push(*b);
                            }
                        } else if !seen.contains(a) {
                            seen.insert(*a);
                            stack.push(*a);
                        }
                    }
                }
                None => unreachable!(),
            }
        }
        needs_reversing
    }
}

// Tests.
fn main() {
    let tests = [
        (3, vec![vec![1, 0], vec![2, 0]], 0),
        (5, vec![vec![1, 0], vec![1, 2], vec![3, 2], vec![3, 4]], 2),
        (
            6,
            vec![vec![0, 1], vec![1, 3], vec![2, 3], vec![4, 0], vec![4, 5]],
            3,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::min_reorder(t.0, t.1), t.2);
    }
    println!("All tests passed!")
}
