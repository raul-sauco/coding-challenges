// 1462. Course Schedule IV
// 🟠 Medium
//
// https://leetcode.com/problems/course-schedule-iv/
//
// Tags: Depth-First Search - Breadth-First Search - Graph - Topological Sort

struct Solution;
impl Solution {
    // We will use a hashmap of hash sets to store all the dependencies of each course,
    // both direct and indirect, first create an adjacency list that we will use to do
    // a dfs for each course starting by their direct dependencies and following the
    // dependency chain, using the adjacency list, to collect all the dependencies.
    // We will use the same hashmap as a memo object to avoid recomputing one course's
    // dependencies multiple times, once the course is present in the set, we know that
    // its dependencies have been computed. To create the result vector, we iterate over
    // the queries and simply check if the query first node is a dependency of the second
    // node, which can be done in O(1) using the hashmap created in the previous step.
    //
    // Time complexity: O(n^3 + p) - Where p is the number of prerequisites and n is the
    // number of courses, first we iterate over the prerequisites to create an adjacency
    // list, then we call dfs for all courses, dfs will visit all the courses neighbors
    // and, for each, it may need to copy n dependencies to its dependency hash set.
    // Space complexity: O(n^2) - The dependencies hashmap will have n entries, each entry
    // is a hash set that could have up to n entries.
    //
    // Runtime 65 ms Beats 33.33%
    // Memory 3 MB Beats 100%
    pub fn check_if_prerequisite(
        num_courses: i32,
        prerequisites: Vec<Vec<i32>>,
        queries: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        use std::collections::{HashMap, HashSet};
        let n = num_courses as usize;
        // Create an adjacency list.
        let mut adj = vec![vec![]; n];
        for pre in prerequisites.iter() {
            adj[pre[1] as usize].push(pre[0] as usize);
        }
        let mut dep = HashMap::<usize, HashSet<usize>>::new();
        // Define a DFS function that finds and returns all dependencies for a given course.
        fn dfs(adj: &Vec<Vec<usize>>, c: usize, dep: &mut HashMap<usize, HashSet<usize>>) {
            // Use dep as a memo, if the value has been computed, return.
            if dep.contains_key(&c) {
                return;
            }
            let mut deps = HashSet::new();
            for nei in adj[c as usize].iter() {
                // This neighbor is a dependency.
                deps.insert(*nei);
                // Collect the dependencies if not in the memo.
                dfs(&adj, *nei, dep);
                for val in dep.entry(*nei).or_default().iter() {
                    deps.insert(*val);
                }
            }
            dep.insert(c, deps);
        }
        // Collect the list of dependencies for each course.
        for i in 0..n {
            dfs(&adj, i, &mut dep);
        }
        (0..queries.len())
            .map(|i| {
                dep.entry(queries[i][1] as usize)
                    .or_default()
                    .contains(&(queries[i][0] as usize))
            })
            .collect()
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::check_if_prerequisite(2, vec![], vec![vec![1, 0], vec![0, 1]]),
        vec![false, false]
    );
    assert_eq!(
        Solution::check_if_prerequisite(2, vec![vec![1, 0]], vec![vec![0, 1], vec![1, 0]]),
        vec![false, true]
    );
    assert_eq!(
        Solution::check_if_prerequisite(
            3,
            vec![vec![1, 2], vec![1, 0], vec![2, 0]],
            vec![vec![1, 0], vec![1, 2]]
        ),
        vec![true, true]
    );
    assert_eq!(
        Solution::check_if_prerequisite(
            5,
            vec![vec![3, 4], vec![2, 3], vec![1, 2], vec![0, 1]],
            vec![vec![0, 4], vec![4, 0], vec![1, 3], vec![3, 0]]
        ),
        vec![true, false, true, false]
    );
    println!("All tests passed!")
}
