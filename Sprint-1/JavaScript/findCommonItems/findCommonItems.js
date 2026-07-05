/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n + m)
 *
 * Original complexity:
 * The original solution used filter() and includes().
 * filter() loops through every item in firstArray.
 * For each item, includes() may need to search the entire
 * secondArray. This results in O(n × m) time, which is
 * O(n²) when both arrays are similar in size.
 *
 * Refactor:
 * Convert secondArray into a Set. Set.has() provides
 * constant-time lookups, so we only loop through each
 * array once. This reduces the time complexity to O(n + m).
 *
 * Space Complexity:
 * We store secondArray in a Set, which requires extra
 * memory proportional to the size of secondArray.
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);

  return [...new Set(firstArray.filter((item) => secondSet.has(item)))];
};