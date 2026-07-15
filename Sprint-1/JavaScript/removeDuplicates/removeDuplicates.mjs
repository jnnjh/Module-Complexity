/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array} items - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
	const seen = new Set();
    const uniqueItems = [];

    for (const value of inputSequence) {
        if (!seen.has(value)) {
            seen.add(value);
            uniqueItems.push(value);
        }
	}

    return uniqueItems;
}