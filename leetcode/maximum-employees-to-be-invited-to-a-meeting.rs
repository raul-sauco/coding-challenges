// 2127. Maximum Employees to Be Invited to a Meeting
// 🔴 Hard
//
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/
//
// Tags: Depth-First Search - Graph - Topological Sort

use std::collections::{HashMap, HashSet};

struct Solution;
impl Solution {
    /// There is two ways to arrange people, use the longest cycle or start on
    /// all pairs of people that like each other, append the longest chains of
    /// people at both ends starting from them. Returns the one that lets us
    /// sit more people.
    ///
    /// Time complexity: O(n) - Both functions run in linear time.
    /// Space complexity: O(n) - Both functions use a linear amount of space.
    ///
    /// Runtime 91 ms Beats 66.67%
    /// Memory 15.2 MB Beats 66.67%
    pub fn maximum_invitations(favorite: Vec<i32>) -> i32 {
        // The result is the best option between arranging the employees in
        // a circle vs pairs plus people that like them next to them.
        Solution::maximum_invitations_as_cycle(&favorite)
            .max(Solution::maximum_invitations_pairs(&favorite))
    }
    /// A function that computes the maximum number of people that we can invite
    /// when they form don't form a cycle, i.e. two people "like" each other.
    ///
    /// Time O(n) - Space O(n)
    pub fn maximum_invitations_pairs(favorite: &Vec<i32>) -> i32 {
        let n = favorite.len();
        // Find all the pairs that like each other.
        let mut pairs = HashSet::<usize>::new();
        // A hashmap of people liked by others.
        let mut liked_by = vec![vec![]; n];
        for i in 0..n {
            // Skip the second elements of pairs.
            if pairs.contains(&i) {
                continue;
            }
            if (favorite[favorite[i] as usize]) as usize == i {
                pairs.insert(i);
                pairs.insert(favorite[i] as usize);
            } else {
                // A hashmap of all employees that like i and are not part of a
                // reciprocal pair.
                liked_by[favorite[i] as usize].push(i);
            }
        }
        // The number of people we can invite this way is the pairs plus anyone
        // that likes one of the people in the pair because they can seat next
        // to them.
        let mut invitees = pairs.len();
        for i in pairs {
            invitees += Solution::maximum_likes_chain(i, &liked_by);
        }
        invitees as i32
    }

    /// A helper function that computes the longest chain of people that likes
    /// "liked". This function expects the liked_by vector to not contain the
    /// partner of liked if this one is part of a reciprocal pair.
    pub fn maximum_likes_chain(liked: usize, liked_by: &Vec<Vec<usize>>) -> usize {
        let mut length = 0;
        for i in liked_by[liked].iter() {
            length = length.max(Solution::maximum_likes_chain(*i, liked_by) + 1);
        }
        length
    }

    /// A function that computes the maximum number of people that we can invite
    /// when they form a cycle, i.e. there are not reciprocal pairs.
    ///
    /// Time O(n) - Space O(n)
    pub fn maximum_invitations_as_cycle(favorite: &Vec<i32>) -> i32 {
        let n = favorite.len();
        let mut visited = vec![false; n];
        let mut res = 0;
        // A function that explores a path starting at a given node.
        fn dfs(
            node: usize,
            pos: usize,
            visited: &mut Vec<bool>,
            path: &mut HashMap<usize, usize>,
            favorites: &Vec<i32>,
        ) -> usize {
            if path.contains_key(&node) {
                return pos - path.get(&node).unwrap();
            }
            if visited[node] {
                return 0;
            }
            path.insert(node, pos);
            visited[node] = true;
            if favorites[node] != -1 {
                return dfs(favorites[node] as usize, pos + 1, visited, path, favorites);
            }
            0
        }
        let mut path: HashMap<usize, usize>;
        for employee in favorite.iter() {
            let i = *employee as usize;
            if !visited[i] {
                path = HashMap::new();
                res = res.max(dfs(i, 0, &mut visited, &mut path, &favorite));
            }
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8], 6),
        (vec![1, 2, 0], 3),
        (vec![2, 2, 1, 2], 3),
        (vec![3, 0, 1, 4, 1], 4),
    ];
    for t in tests {
        assert_eq!(Solution::maximum_invitations(t.0), t.1);
    }
    println!("All tests passed!")
}
