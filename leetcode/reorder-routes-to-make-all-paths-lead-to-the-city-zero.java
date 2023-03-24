// 1466. Reorder Routes to Make All Paths Lead to the City Zero
// 🟠 Medium
//
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
//
// Tags: Depth-First Search - Breadth-First Search - Graph

import java.util.*;

public class Solution {

  /**
   * Since we have n-1 roads and we are guaranteed that we will be able to
   * reach the root from all nodes after reversing some, or none, roads,
   * that means that there is one road between any two nodes. We can use
   * two structures, a set of nodes that we have visited, and a stack, or
   * queue, or nodes that are able to get to the root node, as well as a
   * counter of the number of connections that we need to reverse. We start
   * by visiting 0 and checking all the roads that are connected to it, any
   * road that leads away from 0, will need to be reversed, we do it, and
   * add the node at the end of that road to the stack to be processed
   * because that node now can access the root node, when the road leads to
   * the node that we are visiting, we add the source node to the stack to
   * be processed.
   *
   * Time complexity: O(n) - Even though we have nested loops, the inner
   * loop will run only a total of 2*(n-1) times, which is the number of
   * connections that we have in our "roads" structure .
   * Space complexity: O(n) - The roads structure will have 2*(n-1)
   * elements, the stack could grow to size n and the set will grow to size
   * n because we will visit all nodes.
   *
   * Runtime 63 ms Beats 65%
   * Memory 8.5 MB Beats 95%
   */
  public int minReorder(int n, int[][] connections) {
    HashMap<Integer, ArrayList<int[]>> roads = new HashMap<Integer, ArrayList<int[]>>();
    for (int i = 0; i < n; i++) {
      roads.put(i, new ArrayList<int[]>());
    }
    for (int[] connection : connections) {
      roads.get(connection[0]).add(connection);
      roads.get(connection[1]).add(connection);
    }
    int needs_reversing = 0;
    Stack<Integer> stack = new Stack<Integer>();
    stack.add(0);
    HashSet<Integer> seen = new HashSet<Integer>();
    seen.add(0);
    while (!stack.isEmpty()) {
      int current = stack.pop();
      for (int[] road : roads.get(current)) {
        if (road[0] == current) {
          if (!seen.contains(road[1])) {
            seen.add(road[1]);
            needs_reversing += 1;
            stack.add(road[1]);
          }
        } else if (!seen.contains(road[0])) {
          seen.add(road[0]);
          stack.add(road[0]);
        }
      }
    }
    return needs_reversing;
  }
}
