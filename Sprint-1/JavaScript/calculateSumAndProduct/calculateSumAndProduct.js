/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * Analysis:
 * - The original implementation loops through the array twice:
 *   one loop calculates the sum and another calculates the product.
 * - Two separate linear loops are still O(n) because Big O ignores
 *   constant factors (2n simplifies to O(n)).
 * - The implementation can be improved by combining both calculations
 *   into a single loop. The Big O does not change, but the number of
 *   iterations is reduced, making the code more efficient.
 *
 * Refactored Complexity:
 * - Time Complexity: O(n)
 * - Space Complexity: O(1)
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
    sum,
    product,
  };
}