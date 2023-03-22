// Java Deque
// 🟠 Medium
//
// https://www.hackerrank.com/challenges/java-dequeue
//
// Tags: Data Structures

import java.util.*;

public class Solution {

  /*
   * Use a queue to push in one end and pop from the other, when we push a
   * value we also add 1 to its count in the hashmap, when the queue has
   * more than m values, we pop a value, and remove one from its count
   * from the hash map, if the count gets to zero, we remove the entry.
   * After pushing and popping, we get the count of unique values in the
   * current subarray and check that against the current maximum.
   *
   * Time complexity: O(n) - We iterate over the n values, we push and
   * pop them from the deque and push/pop them from the hashmap, all
   * of them O(1) operations.
   * Space complexity: O(n) - Both the queue and the hashmap will grow
   * to the same size as the input.
   */
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    Deque<Integer> deque = new ArrayDeque<Integer>();
    int n = in.nextInt();
    int m = in.nextInt();
    // Use a hashmap to count the number of unique values in the subarray.
    HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
    int res = 0;
    for (int i = 0; i < n; i++) {
      int num = in.nextInt();
      deque.add(num);
      if (count.containsKey(num)) {
        count.put(num, count.get(num) + 1);
      } else {
        count.put(num, 1);
      }
      if (deque.size() > m) {
        int popped = deque.pop();
        count.put(popped, count.get(popped) - 1);
        if (count.get(popped) == 0) {
          count.remove(popped);
        }
      }
      if (count.size() > res) {
        res = count.size();
        if (res == m) {
          break;
        }
      }
    }
    System.out.println(res);
    in.close();
  }
}
