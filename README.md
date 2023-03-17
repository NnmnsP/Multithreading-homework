# Multithreading-homework

- Generate 10 files, each containing 1 million random integers between 1 and 100
- Implement a sequential program and a multithreaded program to generate the files, and measure the execution time for both variants
- Create a multithreaded program where two types of threads exchange information using the file system
- One thread writes 10 random numbers to the file one by one and prints their sum, then overwrites the file and starts again
- Another thread reads all data from the file, prints the sum if it has 10 numbers, and repeats
- Use locks to prevent race conditions if needed
