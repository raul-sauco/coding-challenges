// 5. Longest Palindromic Substring
// 🟠 Medium
//
// https://leetcode.com/problems/longest-palindromic-substring/
//
// Tags: String - Dynamic Programming

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Palindromes are symmetrical around their center, iterate over both single
    /// characters and pairs of characters, starting at each character and pair,
    /// expanding both right and left while in bounds and the characters match.
    ///
    /// Time complexity: O(n^2) - We are expanding each palindrome around its center.
    /// Space complexity: O(n) - The vector of characters.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.09 MB Beats 83.54%
    pub fn longest_palindrome(s: String) -> String {
        let n = s.len();
        let sc = s.chars().collect::<Vec<char>>();
        let mut indexes = (0, 1);
        let mut max_length = 1;
        let (mut l, mut r);
        for i in 0..n {
            for j in [i, i + 1] {
                (l, r) = (i + 1, j);
                while l > 0 && r < n && sc[l - 1] == sc[r] {
                    l -= 1;
                    r += 1;
                }
                let current_length = r - l;
                if current_length > max_length {
                    max_length = current_length;
                    indexes = (l, r);
                }
            }
        }
        s[indexes.0..indexes.1].to_string()
    }

    /// Manacher's Algorithm.
    ///
    /// https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(n)
    ///
    /// Runtime 2 ms Beats 90.54%
    /// Memory 2.16 MB Beats 54.29%
    pub fn manacher(s: String) -> String {
        let ss = s
            .chars()
            .flat_map(|c| vec!['.', c])
            .chain(vec!['.'].into_iter())
            .collect::<Vec<char>>();
        let n = ss.len();
        let mut palindrome_radii = vec![0; n];
        let (mut center, mut radius) = (0, 0);
        let (mut old_center, mut old_radius);
        while center < n {
            while center >= radius + 1
                && center + radius + 1 < n
                && ss[center - (radius + 1)] == ss[center + radius + 1]
            {
                radius += 1;
            }
            palindrome_radii[center] = radius;
            old_center = center;
            old_radius = radius;
            center += 1;
            radius = 0;
            while center <= old_center + old_radius {
                let mirrowed_center = old_center - (center - old_center);
                let max_mirrowed_radius = old_center + old_radius - center;
                if palindrome_radii[mirrowed_center] < max_mirrowed_radius {
                    palindrome_radii[center] = palindrome_radii[mirrowed_center];
                    center += 1;
                } else if palindrome_radii[mirrowed_center] > max_mirrowed_radius {
                    palindrome_radii[center] = max_mirrowed_radius;
                    center += 1;
                } else {
                    radius = max_mirrowed_radius;
                    break;
                }
            }
        }
        let (max_length, max_idx) =
            palindrome_radii
                .iter()
                .enumerate()
                .fold((0, 0), |(max_val, max_idx), (idx, &val)| {
                    if val > max_val {
                        (val, idx)
                    } else {
                        (max_val, max_idx)
                    }
                });
        let start = (max_idx - max_length) / 2;
        let end = start + max_length;
        s[start..end].to_string()
    }
}

// Tests.
fn main() {
    let tests = [
        (
            "babad".to_string(),
            HashSet::from(["bab".to_string(), "aba".to_string()]),
        ),
        ("cbbd".to_owned(), HashSet::from(["bb".to_string()])),
        (
            "abbcccbbbcaaccbababcbcabca".to_string(),
            HashSet::from(["cbababc".to_string(), "bbcccbb".to_string()]),
        ),
        (
            "iopsajhffgvrnyitusobwcxgwlwniqchfnssqttdrnqqcsrigjsxkzcmuoiyxze".to_string()
                + "rakhmexuyeuhjfobrmkoqdljrlojjjysfdslyvckxhuleagmxnzvikfitmkfh"
                + "evfesnwltekstsueefbrddxrmxokpaxsenwlgytdaexgfwtneurhxvjvpslie"
                + "pgvspdchmhggybwupiqaqlhjjrildjuewkdxbcpsbjtsevkppvgilrlspejqv"
                + "zpfeorjmrbdppovvpzxcytscycgwsbnmspihzldjdgilnrlmhaswqaqbecmao"
                + "cesnpqaotamwofyyfsbmxidowusogmylhlhxftnrmhtnnljjhhcfvywsqimqx"
                + "qobfsageysonuoagmmviozeouutsiecitrmkypwknorjjiaasxfhsftypspwh"
                + "vqovmwkjuehujofiabznpipidhfxpoustquzyfurkcgmioxacleqdxgrxbldc"
                + "uxzgbcazgfismcgmgtjuwchymkzoiqhzaqrtiykdkydgvuaqkllbsactntexc"
                + "ybbjaxlfhyvbxieelstduqzfkoceqzgncvexklahxjnvtyqcjtbfanzgpdmuc"
                + "jlqpiolklmjxnscjcyiybdkgitxnuvtmoypcdldrvalxcxalpwumfxmhtnnlj"
                + "jhhcfvywsqimqxqobfsageysonmhtnnljjhhcfvywsqimqx",
            HashSet::from(["ykdky".to_string()]),
        ),
    ];

    for t in tests {
        assert!(t.1.contains(&Solution::longest_palindrome(t.0.clone())));
        assert!(t.1.contains(&Solution::manacher(t.0.clone())));
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
