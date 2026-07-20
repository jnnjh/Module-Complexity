/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * Analysis:
 * - The original implementation uses nested loops to compare every
 *   possible pair of numbers.
 * - This results in O(n²) time complexity because each element is
 *   compared with every other element.
 * - The complexity can be reduced by using a Set to store numbers
 *   already seen. For each number, calculate its complement
 *   (target - number) and check whether it has already been seen.
 *
 * Refactored Complexity:
 * - Time Complexity: O(n)
 * - Space Complexity: O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const num of numbers) {
    const complement = target - num;

    if (seen.has(complement)) {
      return true;
    }

    seen.add(num);
  }

  return false;
}