-- Merge sort implementation in Haskell, created with the help of GPT-4o LLM.


import System.Environment (getArgs)
import System.IO (writeFile)

-- Merge function that merges two halves of a list
merge :: (Ord a) => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
  | x <= y    = x : merge xs (y:ys)
  | otherwise = y : merge (x:xs) ys

-- Merge sort function
mergeSort :: (Ord a) => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = merge (mergeSort left) (mergeSort right)
  where
    mid = length xs `div` 2
    left = take mid xs
    right = drop mid xs

-- Function to read data from a file
readDataFromFile :: FilePath -> IO [Int]
readDataFromFile filePath = do
    contents <- readFile filePath
    let arr = map read (lines contents) :: [Int]
    return arr

-- Function to write sorted data to a file
writeDataToFile :: FilePath -> [Int] -> IO ()
writeDataToFile filePath arr = do
    let content = unlines (map show arr)
    writeFile filePath content

-- Main function
main :: IO ()
main = do
    -- Get arguments from command line
    args <- getArgs
    let inputFile = head args
    let outputFile = args !! 1

    -- Read data from the input file
    arr <- readDataFromFile inputFile

    -- Perform merge sort
    let sortedArr = mergeSort arr

    -- Write sorted data to the output file
    writeDataToFile outputFile sortedArr

    putStrLn ("Merge Sort completed. Sorted data is saved to: " ++ outputFile)
