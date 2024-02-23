// 787. Cheapest Flights Within K Stops
// 🟠 Medium
//
// https://leetcode.com/problems/cheapest-flights-within-k-stops/
//
// Tags: Dynamic Programming - Depth-First Search - Breadth-First Search - Graph - Heap (Priority Queue) - Shortest Path

use std::{cmp::Reverse, collections::BinaryHeap};

struct Solution;
impl Solution {
    // We can travel one node at a time, and at most k + 1 nodes from the
    // source, also, once we get to the destination, we have a ceiling in
    // how much an itinerary can cost before we decide that it is not worth
    // pursuing it any longer. All that means that we can use BFS to explore
    // one level at a time, we start by flying from the source to all
    // available destinations, then, from all of them to all the ones that
    // we can reach from there and so on, if the price to get to a destination
    // is greater than a price that we have seen before, with least stops, we
    // discard that branch, if the price of a trip becomes greater than the
    // cheapest way to get to dst found so far, we discard it as well, we
    // run the BFS algorithm k+1 times, then return the solution or -1.
    //
    // Time complexity: O(n*k) - The outer loop runs k times, the inner loop
    // will average n items maximum because we only enqueue elements when we
    // find a cheaper path in a later iteration.
    // Space complexity: O(f) - Where f is the number of flights, we save all
    // flight information in the adjacency list.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.7 MB Beats 45.83%
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let mut prices = vec![usize::MAX; n as usize];
        prices[src as usize] = 0;
        for _ in 0..k + 1 {
            let mut tmp = prices.clone();
            for flight in &flights {
                let source = flight[0] as usize;
                let dest = flight[1] as usize;
                let price = flight[2] as usize;
                if prices[source] != usize::MAX {
                    tmp[dest as usize] = tmp[dest].min(prices[source] + price);
                }
            }
            prices = tmp;
        }
        if prices[dst as usize] == usize::MAX {
            -1
        } else {
            prices[dst as usize] as i32
        }
    }

    /// Use Dijkstra with two modifications, allow visiting the same airport more than one time, as
    /// long as the next stops have a smaller number of stops.
    ///
    /// Time complexity: O(f*log(f)) - We may push and pop f flights in and out of a heap that
    /// could grow to size f.
    /// Space complexity: O(f+n) - The adj vector will have n entries, but their subentries will
    /// add up to f. The heap can grow to size f. The visited vector has size n.
    ///
    /// Runtime 2 ms Beats 100%
    /// Memory 2.46 MB Beats 74.07%
    #[allow(dead_code)]
    pub fn find_cheapest_price_(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let n = n as usize;
        let dst = dst as usize;
        let mut adj = vec![vec![]; n];
        let mut visited = vec![(i32::MAX, k + 1); n];
        for flight in flights {
            let (src, dest, cost) = (flight[0] as usize, flight[1] as usize, flight[2]);
            adj[src].push((cost, dest));
        }
        let mut queue = BinaryHeap::new();
        queue.push((Reverse(0), src as usize, 0));
        while let Some((Reverse(local_cost), airport, stops)) = queue.pop() {
            if airport == dst {
                // Using Dijkstra this would be the cheapest way to get here.
                return local_cost;
            }
            if stops <= k {
                for &(cost, dest) in adj[airport].iter() {
                    let cost_to_dest = local_cost + cost;
                    let stops_to_dest = stops + 1;
                    // This prunes cycles that cannot result in a cheaper route.
                    if cost_to_dest < visited[dest].0 || stops_to_dest < visited[dest].1 {
                        queue.push((Reverse(cost_to_dest), dest, stops_to_dest));
                        visited[dest] = (cost_to_dest, stops_to_dest);
                    }
                }
            }
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (3, vec![[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        (3, vec![[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
        (
            4,
            vec![
                [0, 1, 100],
                [1, 2, 100],
                [2, 0, 100],
                [1, 3, 600],
                [2, 3, 200],
            ],
            0,
            3,
            1,
            700,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_cheapest_price(
            t.0,
            t.1.clone().iter().map(|arr| arr.to_vec()).collect(),
            t.2,
            t.3,
            t.4,
        );
        if res == t.5 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.5, res
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
