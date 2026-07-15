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
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  for (const num of numbers) {
    product *= num;
    sum += num;

  }

  return {
    sum: sum,
    product: product,
  };
}

// The function has 2 loops, one for the sum and the other for the product.
// we actually don't need to loop twice, we can do both in a single loop.
// the time complexity now is 0(n) and the space complexity is O(1).