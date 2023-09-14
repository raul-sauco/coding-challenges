// 332. Reconstruct Itinerary
// 🔴 Hard
//
// https://leetcode.com/problems/reconstruct-itinerary/
//
// Tags: Depth-First Search - Graph - Eulerian Circuit

use std::{
    cmp::Reverse,
    collections::{BinaryHeap, HashMap},
};

struct Solution;
impl Solution {
    /// Create a dictionary of source: sorted_destinations, starting from JFK
    /// try visiting the possible destinations in lexicographical order until
    /// an itinerary that visits all the edges, or uses all the given tickets,
    /// is found, when we find that itinerary, return it. Anytime we arrive
    /// at a dead-end on the branch that we are exploring, we backtrack to
    /// the latest point where we made a decision and choose the next option
    /// until all the options on that branch have been exhausted, then we try
    /// another branch from higher in the recursion tree.
    ///
    /// Time complexity: O(v*e) - At most we will explore all combinations of v
    /// vertex and e edges.
    /// Space complexity: O(v+e) - The dictionary can grow to have v+e entries,
    /// the call stack will have a max height of v+1.
    ///
    /// Runtime 11 ms Beats 8.33%
    /// Memory 2.53 MB Beats 8.33%
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        let n = tickets.len();
        let mut dest = HashMap::new();
        for ticket in tickets {
            dest.entry(ticket[0].clone())
                .or_insert(vec![])
                .push(ticket[1].clone());
        }
        for (_key, value) in dest.iter_mut() {
            value.sort_unstable();
        }
        let mut res = vec!["JFK".to_string()];
        fn bt(dest: &mut HashMap<String, Vec<String>>, res: &mut Vec<String>, n: usize) -> bool {
            let origin = res[res.len() - 1].clone();
            // Base case, no destinations left from this origin.
            if !dest.contains_key(&origin) || dest.get(&origin).unwrap().is_empty() {
                return res.len() == n + 1;
            }
            let possible_destinations = dest.get(&origin).unwrap().clone();
            for i in 0..possible_destinations.len() {
                let d = possible_destinations[i].to_owned();
                res.push(d);
                let mut pd_copy = possible_destinations.clone();
                pd_copy.remove(i);
                dest.insert(origin.clone(), pd_copy);
                if bt(dest, res, n) {
                    return true;
                }
                // Backtrack if no route is found.
                if let Some(entry) = dest.get_mut(&origin) {
                    *entry = possible_destinations.clone();
                }
                res.pop();
            }
            false
        }
        bt(&mut dest, &mut res, n);
        res
    }

    /// A better solution that uses a stack and avoids making so many copies of
    /// memory data. Found here:
    /// https://leetcode.com/problems/reconstruct-itinerary/solutions/711550/rust-solution/
    ///
    /// Time complexity: O(v*e) - At most we will explore all combinations of v
    /// vertex and e edges.
    /// Space complexity: O(v+e) - The dictionary can grow to have v+e entries,
    /// the call stack will have a max height of v+1.
    ///
    /// Runtime 4 ms Beats 83.33%
    /// Memory 2.28 MB Beats 75%
    pub fn find_itinerary_2(tickets: Vec<Vec<String>>) -> Vec<String> {
        let mut graph: HashMap<&str, BinaryHeap<Reverse<&str>>> = HashMap::new();
        for ticket in tickets.iter() {
            graph
                .entry(&ticket[0])
                .or_insert_with(BinaryHeap::new)
                .push(Reverse(&ticket[1]));
        }
        let mut route = Vec::with_capacity(tickets.len() + 1);
        let mut stack = vec!["JFK"];
        while let Some(src) = stack.last() {
            if let Some(destinations) = graph.get_mut(src) {
                if !destinations.is_empty() {
                    if let Some(dest) = destinations.pop() {
                        stack.push(dest.0);
                    }
                    continue;
                }
            }
            if let Some(last) = stack.pop() {
                route.push(last.to_owned());
            }
        }
        route.reverse();
        route
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![
                vec!["JFK".to_string(), "KUL".to_string()],
                vec!["JFK".to_string(), "NRT".to_string()],
                vec!["NRT".to_string(), "JFK".to_string()],
            ],
            vec![
                "JFK".to_string(),
                "NRT".to_string(),
                "JFK".to_string(),
                "KUL".to_string(),
            ],
        ),
        (
            vec![
                vec!["MUC".to_string(), "LHR".to_string()],
                vec!["JFK".to_string(), "MUC".to_string()],
                vec!["SFO".to_string(), "SJC".to_string()],
                vec!["LHR".to_string(), "SFO".to_string()],
            ],
            vec![
                "JFK".to_string(),
                "MUC".to_string(),
                "LHR".to_string(),
                "SFO".to_string(),
                "SJC".to_string(),
            ],
        ),
        (
            vec![
                vec!["JFK".to_string(), "SFO".to_string()],
                vec!["JFK".to_string(), "ATL".to_string()],
                vec!["SFO".to_string(), "ATL".to_string()],
                vec!["ATL".to_string(), "JFK".to_string()],
                vec!["ATL".to_string(), "SFO".to_string()],
            ],
            vec![
                "JFK".to_string(),
                "ATL".to_string(),
                "JFK".to_string(),
                "SFO".to_string(),
                "ATL".to_string(),
                "SFO".to_string(),
            ],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::find_itinerary(t.0.clone()), t.1);
        assert_eq!(Solution::find_itinerary_2(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
