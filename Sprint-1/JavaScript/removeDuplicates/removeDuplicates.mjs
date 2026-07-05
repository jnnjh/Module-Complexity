/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * Original complexity:
 * The original solution uses nested loops. For each item in
 * the input sequence, it searches through the uniqueItems
 * array to check whether the value already exists. This
 * results in O(n²) time complexity in the worst case.
 *
 * Refactor:
 * Use a Set to keep track of values that have already been
 * seen. Set.has() and Set.add() are O(1) operations, allowing
 * us to process the sequence in a single loop.
 *
 * Refactored Complexity:
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
export function removeDuplicates(inputSequence) {
  const seen = new Set();
  const uniqueItems = [];

  for (const item of inputSequence) {
    if (!seen.has(item)) {
      seen.add(item);
      uniqueItems.push(item);
    }
  }

  return uniqueItems;
}