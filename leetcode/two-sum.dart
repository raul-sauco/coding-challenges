/// 1. Two Sum
/// 🟢 Easy
///
/// https://leetcode.com/problems/two-sum/
///
/// Tags: Array - Hash Table

/// Create a hashmap that stores numbers that we have seen already as keys
/// and their indices as values, then iterate over the numbers in the
/// input, for each number, check if the set contains a number that we can
/// add to this one to add up to the target, if found, return their indices,
/// the description guarantees that each test case will have at most one
/// solution.
///
/// Time complexity; O(n) - We visit each element of the input once, for
/// each, we check if another element is in the set at O(1) cost.
/// Space complexity: O(n) - The set can grow to size n.
///
/// Runtime: 437 ms, faster than 85.66%
/// Memory Usage: 143 MB, less than 82.85%
class Solution {
  List<int> twoSum(List<int> nums, int target) {
    Map<int, int> map = Map<int, int>();
    for (int i = 0; i < nums.length; i++) {
      var num = nums[i];
      var complement = target - num;
      if (map.containsKey(complement)) {
        return [map[complement] as int, i];
      }
      map[num] = i;
    }
    return [];
  }
}

void main() {
  final stopwatch = Stopwatch()..start();
  bool testFailed = false;
  const tests = [
    [
      [2, 7, 11, 15],
      9,
      [0, 1]
    ],
    [
      [3, 2, 4],
      6,
      [1, 2]
    ],
    [
      [3, 3],
      6,
      [0, 1]
    ],
  ];
  for (int i = 0; i < tests.length; i++) {
    var test = tests[i];
    var nums = test[0] as List<int>;
    var target = test[1] as int;
    var expected = test[2] as List<int>;
    var actual = Solution().twoSum(nums, target);
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
