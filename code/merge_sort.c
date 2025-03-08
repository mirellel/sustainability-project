// C program for Merge Sort, adapted from https://www.geeksforgeeks.org/merge-sort/

#include <stdio.h>
#include <stdlib.h>

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    // Create temp arrays
    int L[n1], R[n2];

    // Copy data to temp arrays L[] and R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Merge the temp arrays back into arr[l..r
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[],
    // if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[],
    // if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// l is for left index and r is right index of the
// sub-array of arr to be sorted
void mergeSort(int arr[], int l, int r)
{
    if (l < r) {
        int m = l + (r - l) / 2;

        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

// Helper functions to read and write data to files created using the GPT-4o LLM.

// Function to read data from file
int* readDataFromFile(const char *filename, int size) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Could not open file %s for reading.\n", filename);
        exit(1);
    }

    int* arr = (int*)malloc(size * sizeof(int));
    if (arr == NULL) {
        perror("Memory allocation failed");
        fclose(file);
        return NULL;
    }

    for (int i = 0; i < size; i++) {
        fscanf(file, "%d", &arr[i]);
    }

    fclose(file);
    return arr;
}

// Function to write sorted data to file
void writeDataToFile(const char *filename, int arr[], int size) {
    FILE *file = fopen(filename, "w");
    if (!file) {
        printf("Could not open file %s for writing.\n", filename);
        exit(1);
    }

    // Write the sorted array to file
    for (int i = 0; i < size; i++) {
        fprintf(file, "%d\n", arr[i]);
    }

    fclose(file);
}

int main(int argc, char *argv[]) {
    // Check if the right number of arguments are provided
    if (argc != 4) {
        printf("Usage: %s <input_file> <number_of_integers> <output_file>\n", argv[0]);
        return 1;
    }

    const char *input_filename = argv[1];
    int size = atoi(argv[2]);
    const char *output_filename = argv[3];

    // Read the dataset from the binary file
    int *arr = readDataFromFile(input_filename, size);
    if (arr == NULL) {
        return 1;
    }
    // Perform Merge Sort
    mergeSort(arr, 0, size-1);

    // Write the sorted data to output file
    writeDataToFile(argv[3], arr, size);

    // Free the allocated memory
    free(arr);

    printf("Merge Sort completed. Sorted data is saved to %s\n", argv[3]);
    return 0;
}
