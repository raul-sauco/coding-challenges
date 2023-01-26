// 787. Cheapest Flights Within K Stops
// 🟠 Medium
//
// https://leetcode.com/problems/cheapest-flights-within-k-stops/
//
// Tags: Dynamic Programming - Depth-First Search - Breadth-First Search
// Graph - Heap (Priority Queue) - Shortest Path

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
}

// Tests.
fn main() {
    assert_eq!(
        Solution::find_cheapest_price(
            3,
            vec![vec![0, 1, 100], vec![1, 2, 100], vec![0, 2, 500]],
            0,
            2,
            1
        ),
        200
    );
    assert_eq!(
        Solution::find_cheapest_price(
            3,
            vec![vec![0, 1, 100], vec![1, 2, 100], vec![0, 2, 500]],
            0,
            2,
            0
        ),
        500
    );
    println!("All tests passed!")
}
