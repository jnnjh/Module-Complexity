/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n × m)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n + m)
 *
 * Analysis:
 * - The original implementation filters the first array while using
 *   secondArray.includes() for each element.
 * - The includes() method performs a linear search, making each lookup O(m).
 * - This results in O(n × m) time complexity.
 * - The complexity can be reduced by storing the second array in a Set,
 *   allowing O(1) average lookup time.
 *
 * Refactored Complexity:
 * - Time Complexity: O(n + m)
 * - Space Complexity: O(n)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);
  const commonItems = new Set();

  for (const item of firstArray) {
    if (secondSet.has(item)) {
      commonItems.add(item);
    }
  }

  return [...commonItems];
};