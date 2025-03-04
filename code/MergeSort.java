import java.io.*;
import java.util.*;

public class MergeSort {
    
    // Merge function that merges two halves of an array
    static void merge(int arr[], int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        // Create temporary arrays
        int[] L = new int[n1];
        int[] R = new int[n2];

        // Copy data to temp arrays L[] and R[]
        for (int i = 0; i < n1; i++)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; j++)
            R[j] = arr[mid + 1 + j];

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Merge sort function
    static void mergeSort(int arr[], int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    // Function to read data from a file
    static int[] readDataFromFile(String filePath) throws IOException {
        List<Integer> list = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                list.add(Integer.parseInt(line.trim()));
            }
        }
        return list.stream().mapToInt(i -> i).toArray();
    }

    // Function to write sorted data to a file
    static void writeDataToFile(String filePath, int[] arr) throws IOException {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filePath))) {
            for (int num : arr) {
                bw.write(num + "\n");
            }
        }
    }

    // Main function with argument parsing
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java MergeSortFile <input_file> <output_file>");
            return;
        }
        
        String inputFile = args[0];
        String outputFile = args[1];
        
        try {
            int[] arr = readDataFromFile(inputFile);
            mergeSort(arr, 0, arr.length - 1);
            writeDataToFile(outputFile, arr);
            System.out.println("Merge Sort completed. Sorted data is saved to: " + outputFile);
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}