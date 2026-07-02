/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity:O(n^2)
 * Space Complexity:O(n)
 * Optimal Time Complexity:O(n)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  return [...new Set(inputSequence)];
}

console.log(removeDuplicates([3, 3, 5, 6, 3, 7]));
