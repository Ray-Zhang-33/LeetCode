#include <stdio.h>  // For input and output
#include <stdlib.h> // For qsort function

// Answer starts

int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b); // Cast const void* to int* and compare
}

// Function to merge two arrays
void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    // Define the comparison function for qsort


    // Merge elements of nums2 into the end of nums1
    for (int i = 0; i < n; i++) {
        *(nums1 + m + i) = nums2[i];
    }

    // Sort nums1 using qsort
    qsort(nums1, nums1Size, sizeof(int), cmp);
}

// Answer ends

// Main function for testing
int main() {
    // Define test data
    int nums1[6] = {1, 2, 3, 0, 0, 0}; // Initial data for nums1
    int nums2[3] = {2, 5, 6};          // Data for nums2
    int m = 3;                         // Number of valid elements in nums1
    int n = 3;                         // Number of valid elements in nums2
    int nums1Size = m + n;             // Total size of nums1

    // Call the merge function
    merge(nums1, nums1Size, m, nums2, n, n);

    // Print the merged nums1 array
    printf("Merged array: ");
    for (int i = 0; i < nums1Size; i++) {
        printf("%d ", nums1[i]);
    }
    printf("\n");

    return 0;
}