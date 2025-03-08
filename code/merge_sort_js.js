// Merge sort implementation in JavaScript, adapted from https://www.geeksforgeeks.org/merge-sort/

const fs = require('fs')

// Merge function to merge two halves of an array
function merge(arr, left, mid, right) {
  const n1 = mid - left + 1
  const n2 = right - mid

  // Create temporary arrays
  const L = new Array(n1)
  const R = new Array(n2)

  // Copy data to temp arrays L[] and R[]
  for (let i = 0; i < n1; i++) L[i] = arr[left + i]
  for (let j = 0; j < n2; j++) R[j] = arr[mid + 1 + j]

  let i = 0,
    j = 0,
    k = left

  // Merge the temp arrays back into arr[left..right]
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i]
      i++
    } else {
      arr[k] = R[j]
      j++
    }
    k++
  }

  // Copy remaining elements of L[]
  while (i < n1) {
    arr[k] = L[i]
    i++
    k++
  }

  // Copy remaining elements of R[]
  while (j < n2) {
    arr[k] = R[j]
    j++
    k++
  }
}

// Merge Sort function
function mergeSort(arr, left, right) {
  if (left < right) {
    const mid = Math.floor(left + (right - left) / 2)
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)
  }
}

// Helper functions to read and write data to files created using the GPT-4o LLM.

// Function to read data from a file
function readDataFromFile(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf-8').trim()
    return data.split('\n').map(Number)
  } catch (error) {
    console.error('Error reading file:', error)
    process.exit(1)
  }
}

// Function to write sorted data to a file
function writeDataToFile(filePath, arr) {
  try {
    fs.writeFileSync(filePath, arr.join('\n') + '\n', 'utf-8')
  } catch (error) {
    console.error('Error writing file:', error)
    process.exit(1)
  }
}

// Main function to handle command-line arguments
function main() {
  if (process.argv.length !== 4) {
    console.error('Usage: node merge_sort.js <input_file> <output_file>')
    process.exit(1)
  }

  const inputFile = process.argv[2]
  const outputFile = process.argv[3]

  // Read, sort, and write output
  const arr = readDataFromFile(inputFile)
  mergeSort(arr, 0, arr.length - 1)
  writeDataToFile(outputFile, arr)

  console.log(`Merge Sort completed. Sorted data is saved to: ${outputFile}`)
}

// Run main function if executed from command line
if (require.main === module) {
  main()
}
