/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * Original complexity:
 * The original solution uses nested loops. For each number,
 * it checks every remaining number in the array looking for
 * a pair whose sum equals the target. Since each number can
 * be compared with many other numbers, the time complexity
 * is O(n²).
 *
 * Refactor:
 * Use a Set to store numbers that have already been seen.
 * For each number, calculate the value needed to reach the
 * target and check whether it exists in the Set.
 * Set lookups are O(1), so we only need one pass through
 * the array.
 *
 * Refactored Complexity:
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const num of numbers) {
    const needed = target - num;

    if (seen.has(needed)) {
      return true;
    }

    seen.add(num);
  }

  return false;
}