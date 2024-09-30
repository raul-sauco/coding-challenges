// 1381. Design a Stack With Increment Operation
// 🟠 Medium
//
// https://leetcode.com/problems/design-a-stack-with-increment-operation/
//
// Tags: Array - Stack - Design

/// Simple stack, add a check of max size before pushing and the increment method.
///
/// Space complexity: O(k) - We can hold a max of max_size elements.
///
/// Runtime 6 ms Beats 25%
/// Memory 3.05 MB Beats 87%
struct CustomStack {
    stack: Vec<i32>,
    size: usize,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CustomStack {
    /// Time complexity: O(1)
    fn new(max_size: i32) -> Self {
        Self {
            stack: Vec::with_capacity(max_size as usize),
            size: max_size as usize,
        }
    }

    /// Time complexity: O(1)
    fn push(&mut self, x: i32) {
        if self.stack.len() < self.size {
            self.stack.push(x);
        }
    }

    /// Time complexity: O(1)
    fn pop(&mut self) -> i32 {
        match self.stack.pop() {
            Some(x) => x,
            None => -1,
        }
    }

    /// Time complexity: O(k)
    fn increment(&mut self, k: i32, val: i32) {
        for i in 0..(k as usize).min(self.stack.len()) {
            self.stack[i] += val;
        }
    }
}

// Tests.
fn main() {
    let mut stack = CustomStack::new(3);
    println!("\n\x1b[92m» Running tests...\x1b[0m");
    let (mut success, mut failed) = (0, 0);
    let (mut res, mut expected);
    stack.push(1);
    stack.push(2);
    expected = 2;
    res = stack.pop();
    if res == expected {
        success += 1;
        println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", success + failed);
    } else {
        failed += 1;
        println!(
            "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
            success + failed,
            expected,
            res
        );
    }
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.increment(5, 100);
    stack.increment(2, 100);
    expected = 103;
    res = stack.pop();
    if res == expected {
        success += 1;
        println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", success + failed);
    } else {
        failed += 1;
        println!(
            "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
            success + failed,
            expected,
            res
        );
    }
    expected = 202;
    res = stack.pop();
    if res == expected {
        success += 1;
        println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", success + failed);
    } else {
        failed += 1;
        println!(
            "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
            success + failed,
            expected,
            res
        );
    }
    expected = 201;
    res = stack.pop();
    if res == expected {
        success += 1;
        println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", success + failed);
    } else {
        failed += 1;
        println!(
            "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
            success + failed,
            expected,
            res
        );
    }
    expected = -1;
    res = stack.pop();
    if res == expected {
        success += 1;
        println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", success + failed);
    } else {
        failed += 1;
        println!(
            "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
            success + failed,
            expected,
            res
        );
    }
    println!();
    if failed == 0 {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!("\x1b[31mx\x1b[95m {} tests failed!\x1b[0m", failed)
    }
}
