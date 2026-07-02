/**
 * Finds common items between two arrays.
 *
 * Time Complexity:O(n*m)
 * Space Complexity:O(u)
 * Optimal Time Complexity:O(n+m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const allowedItems = new Set(secondArray);

  const uniqueValues = [
    ...new Set(firstArray.filter((item) => allowedItems.has(item))),
  ];
  return uniqueValues;
};

console.log(findCommonItems([2, 5, 7], [5, 6, 7]));
