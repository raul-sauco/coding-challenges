// 2050. Parallel Courses III
// 🔴 Hard
//
// https://leetcode.com/problems/parallel-courses-iii/
//
// Tags: Array - Dynamic Programming - Graph - Topological Sort

use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// Use topographical sorting, push any courses for which we have completed
    /// the prerequisites into a minimum heap prioritized by complete_at time, that
    /// way we know that, when we complete a course's dependencies, the last
    /// course that we remove is the one that finished latests. Then we can push
    /// the newly available course starting at the completed_at time, and we know
    /// that it will finish at completed_at + time[i]. The result is the time
    /// at which we complete the last course that we finish.
    ///
    /// Time complexity: O(e+n*log(n)) - O(e) where e is the number of relations,
    /// to build the indegree and dependents vectors. Then we iterate over n nodes
    /// checking if we can push them into the heap. each node will be pushed and
    /// popped once n*log(n) and, for each node, we will visit all its relations.
    /// Space complexity: O(e+n) - The dependents matrix will have n vectors, but
    /// the total elements in between all these vectors will be e.
    ///
    /// Runtime 38 ms Beats 66.67%
    /// Memory 7.40 MB Beats 100%
    pub fn minimum_time(n: i32, relations: Vec<Vec<i32>>, time: Vec<i32>) -> i32 {
        let n = n as usize;
        let (mut prev, mut next);
        let mut dependents = vec![vec![]; n];
        let mut indegree = vec![0; n];
        for relation in relations {
            prev = relation[0] as usize - 1;
            next = relation[1] as usize - 1;
            dependents[prev].push(next);
            indegree[next] += 1;
        }
        let mut heap = BinaryHeap::<(i32, usize)>::new();
        // Push any courses that we can start immediately.
        for i in 0..n {
            if indegree[i] == 0 {
                heap.push((-time[i], i));
            }
        }
        let mut res = 0;
        while let Some((t, course)) = heap.pop() {
            let completed_at = -t;
            res = res.max(completed_at);
            for &dependent in &dependents[course] {
                indegree[dependent] -= 1;
                if indegree[dependent] == 0 {
                    // We have completed all this courses dependencies.
                    let will_complete_at = completed_at + time[dependent];
                    heap.push((-will_complete_at, dependent));
                }
            }
        }
        res
    }

    /// Use a memoized dfs, when we reach a node that has no dependencies,
    /// return the time it takes to complete the course. Otherwise return the
    /// max result of calling dfs on all its dependencies.
    ///
    /// Time complexity: O(e+n) - O(e) to build the graph, then n calls to dfs
    /// that we are memoizing.
    /// Space complexity: O(e+n) - The graph uses e+n extra memory.
    ///
    /// Runtime 41 ms Beats 33.33%
    /// Memory 10.78 MB Beats 16.67%
    pub fn minimum_time_2(n: i32, relations: Vec<Vec<i32>>, time: Vec<i32>) -> i32 {
        fn dfs(i: usize, graph: &Vec<Vec<usize>>, cache: &mut Vec<i32>, time: &Vec<i32>) -> i32 {
            if cache[i] == i32::MAX {
                if graph[i].is_empty() {
                    cache[i] = time[i];
                } else {
                    cache[i] = 0;
                    for &nei in &graph[i] {
                        cache[i] = cache[i].max(dfs(nei, graph, cache, time));
                    }
                    cache[i] += time[i];
                }
            }
            cache[i]
        }
        let n = n as usize;
        let mut cache = vec![i32::MAX; n];
        let mut graph = vec![vec![]; n];
        for r in relations {
            graph[r[0] as usize - 1].push(r[1] as usize - 1);
        }
        let mut res = 0;
        for i in 0..n {
            res = res.max(dfs(i, &graph, &mut cache, &time));
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (2, vec![], vec![1, 2], 2),
        (3, vec![], vec![3, 2, 5], 5),
        (5, vec![], vec![3, 2, 1, 5, 4], 5),
        (3, vec![vec![1, 2], vec![2, 3]], vec![1, 2, 3], 6),
        (3, vec![vec![1, 3], vec![2, 3]], vec![3, 2, 5], 8),
        (
            4,
            vec![vec![1, 2], vec![2, 3], vec![3, 4]],
            vec![1, 2, 3, 4],
            10,
        ),
        (
            5,
            vec![vec![1, 5], vec![2, 5], vec![3, 5], vec![3, 4], vec![4, 5]],
            vec![1, 2, 3, 4, 5],
            12,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::minimum_time(t.0, t.1.clone(), t.2.clone()), t.3);
        assert_eq!(Solution::minimum_time_2(t.0, t.1.clone(), t.2.clone()), t.3);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
