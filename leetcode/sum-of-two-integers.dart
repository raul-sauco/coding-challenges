/// 371. Sum of Two Integers
/// 🟠 Medium
///
/// https://leetcode.com/problems/sum-of-two-integers/
///
/// Tags: Math - Bit Manipulation

/// Use bitwise XOR to sum the two number's bits, then use the result of bitwise
/// AND shifted 1 bit to the left to represent the sum's carry. Keep computing
/// while we have a carry to add to the sum.
///
/// Time complexity: O(1) - Input is bounded -1000 <= a, b <= 1000
/// Space complexity: O(1)
///
/// Runtime: 431 ms, faster than 58.62%
// Memory Usage: 139.4 MB, less than 100.00%
class Solution {
  int getSum(int a, int b) {
    while (b != 0) {
      int tmp = (a & b) << 1;
      a = a ^ b;
      b = tmp;
    }
    return a;
  }
}

void main() {
  final stopwatch = Stopwatch()..start();
  bool testFailed = false;
  const tests = [
    [0, 0, 0],
    [1, 2, 3],
    [2, 3, 5],
    [2, -2, 0],
    [-2, 2, 0],
    [3, -3, 0],
    [16, -14, 2],
    [-2, -2, -4],
    [-11, 0, -11],
    [-12, -8, -20],
  ];
  for (int i = 0; i < tests.length; i++) {
    var test = tests[i];
    var a = test[0] as int;
    var b = test[1] as int;
    var expected = test[2] as int;
    var actual = Solution().getSum(a, b);
    if (actual.toString() != expected.toString()) {
      testFailed = true;
      print('\x1B[91m» Test $i: FAILED!!\x1B[0m');
    }
  }
  stopwatch.stop();
  final used = stopwatch.elapsed.toString().substring(6);
  if (testFailed) {
    print('\x1B[91m» Some tests FAILED in $used seconds\x1B[0m');
  } else {
    print('\x1B[92m» All tests PASSED in $used seconds\x1B[0m');
  }
}
