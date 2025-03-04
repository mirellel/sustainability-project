import argparse

# Merge sort implementation in Python, adapted from https://www.geeksforgeeks.org/

# Merge function that merges two halves of an array
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Merge sort function
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Function to read data from a file
def read_data_from_file(file_path):
    arr = []
    with open(file_path, 'r') as file:
        for line in file:
            arr.append(int(line.strip()))
    return arr

# Function to write sorted data to a file
def write_data_to_file(file_path, arr):
    with open(file_path, 'w') as file:
        for item in arr:
            file.write(f"{item}\n")

# Main function with argument parsing
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Merge Sort with file input and output.")
    parser.add_argument('-data', required=True, help="Input file with unsorted data.")
    parser.add_argument('-output', required=True, help="Output file to write sorted data.")

    # Parse arguments
    args = parser.parse_args()

    # Read data from the input file
    arr = read_data_from_file(args.data)

    # Perform merge sort
    merge_sort(arr, 0, len(arr) - 1)

    # Write sorted data to the output file
    write_data_to_file(args.output, arr)

    print("Merge Sort completed. Sorted data is saved to:", args.output)

# Entry point
if __name__ == "__main__":
    main()
