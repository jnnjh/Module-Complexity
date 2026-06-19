/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  return [...new Set(inputSequence)];
}

// The previous code had a time complexity of O(n2) because it had 2 loops to check for duplicates.
// Set has time complexity of O(n) as it just deletes duplicates when needed and the time complexity depends on the input size.