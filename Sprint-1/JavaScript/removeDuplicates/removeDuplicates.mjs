/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * Analysis:
 * - The original implementation uses nested loops.
 * - For each element in the input array, it searches through the
 *   uniqueItems array to check if it already exists.
 * - As the uniqueItems array grows, each lookup becomes more expensive,
 *   resulting in O(n²) time complexity.
 * - The complexity can be reduced by using a Set to track values that
 *   have already been seen. Set.has() provides O(1) average lookup time
 *   while preserving the order of first occurrence.
 *
 * Refactored Complexity:
 * - Time Complexity: O(n)
 * - Space Complexity: O(n)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
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