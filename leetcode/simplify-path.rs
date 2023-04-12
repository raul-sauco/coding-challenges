// 71. Simplify Path
// 🟠 Medium
//
// https://leetcode.com/problems/simplify-path/
//
// Tags: String - Stack

struct Solution;
impl Solution {
    /// Use a stack to collect the directories that form the path, iterate over
    /// the tokens in the input, skip "." and empty tokens, pop the last
    /// directory when we see ".." and push anything else. Use the contents of
    /// the stack to build the resulting simplified path.
    ///
    /// Time complexity: O(n) - We visit all characters in the input string and
    /// do O(1) work for each.
    /// Space complexity: O(n) - The stack grows in size linearly with the input.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.2 MB Beats 42.22%
    pub fn simplify_path(path: String) -> String {
        let mut dirs = vec![];
        for token in path.split('/') {
            match token {
                "." | "" => continue,
                ".." => {
                    dirs.pop();
                }
                _ => dirs.push(token),
            }
        }
        format!("{}{}", "/", dirs.join("/"))
    }

    /// Functional programming version of the solution, same logic as the
    /// previous solution but uses fold to build the result path.
    ///
    /// Time complexity: O(n) - We visit all characters in the input string and
    /// do O(1) work for each.
    /// Space complexity: O(n) - The stack grows in size linearly with the input.
    ///
    /// Runtime 2 ms Beats 44.44%
    /// Memory 2.2 MB Beats 73.33%
    pub fn simplify_path_2(path: String) -> String {
        format!(
            "{}{}",
            "/",
            path.split('/')
                .fold(vec![], |mut v, d| match d {
                    "." | "" => v,
                    ".." => {
                        v.pop();
                        v
                    }
                    _ => {
                        v.push(d);
                        v
                    }
                })
                .join("/")
        )
    }
}

// Tests.
fn main() {
    let tests = [
        ["/../", "/"],
        ["/a/..", "/"],
        ["/a/../", "/"],
        ["/home/", "/home"],
        ["/abc/...", "/abc/..."],
        ["/a/./b/../../c/", "/c"],
        ["/a/../.././../../", "/"],
        ["/../../../../../a", "/a"],
        ["/home//foo/", "/home/foo"],
        ["/a//b//c//////d", "/a/b/c/d"],
        ["/a/./b/./c/./d/", "/a/b/c/d"],
    ];
    for t in tests {
        assert_eq!(
            Solution::simplify_path(String::from(t[0])),
            String::from(t[1])
        );
        assert_eq!(
            Solution::simplify_path_2(String::from(t[0])),
            String::from(t[1])
        );
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
