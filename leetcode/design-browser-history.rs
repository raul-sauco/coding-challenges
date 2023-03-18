// 1472. Design Browser History
// 🟠 Medium
//
// https://leetcode.com/problems/design-browser-history/
//
// Tags: Array - Linked List - Stack - Design - Doubly-Linked List - Data Stream

struct BrowserHistory {
    hist: Vec<String>,
    current_idx: usize,
    can_move_forward: usize,
}

/**
* Use a single vector and two integers to make all the operations run in
* O(1), one integer marks the current index in the vector that we are
* located at currently, the other determines how many steps forward in
* the history we can move, if any.
*
* Time complexity: O(1) - All methods run in constant time.
* Space complexity: O(n) - Each call to visit will add one element to the
* vector.
*
* Runtime 38 ms Beats 54.55%
* Memory 4.6 Beats 63.64%
*/
impl BrowserHistory {
    fn new(homepage: String) -> Self {
        Self {
            hist: vec![homepage],
            current_idx: 0,
            can_move_forward: 0,
        }
    }

    fn visit(&mut self, url: String) {
        self.current_idx += 1;
        self.can_move_forward = 0;
        if self.current_idx == self.hist.len() {
            self.hist.push(url);
        } else {
            self.hist[self.current_idx] = url;
        }
    }

    fn back(&mut self, steps: i32) -> String {
        let real = (steps as usize).min(self.current_idx);
        self.current_idx -= real;
        self.can_move_forward += real;
        self.hist[self.current_idx].clone()
    }

    fn forward(&mut self, steps: i32) -> String {
        let real = (steps as usize).min(self.can_move_forward);
        self.current_idx += real;
        self.can_move_forward -= real;
        self.hist[self.current_idx].clone()
    }
}

// Tests.
fn main() {
    let mut bh = BrowserHistory::new(String::from("leetcode.com"));
    bh.visit(String::from("google.com"));
    bh.visit(String::from("facebook.com"));
    bh.visit(String::from("youtube.com"));
    assert_eq!(bh.back(1), String::from("facebook.com"));
    assert_eq!(bh.back(1), String::from("google.com"));
    assert_eq!(bh.forward(1), String::from("facebook.com"));
    bh.visit(String::from("linkedin.com"));
    assert_eq!(bh.forward(2), String::from("linkedin.com"));
    assert_eq!(bh.back(2), String::from("google.com"));
    assert_eq!(bh.back(7), String::from("leetcode.com"));
    println!("All tests passed!")
}
