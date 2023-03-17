import random
import threading

# actually I'm not sure what am I doing. 
def write_to_file(filename, lock):
    for i in range(10):
        num = random.randint(1, 10)
        with lock:
            with open(filename, "a") as f:
                f.write(str(num) + "\n")
        if i == 9:
            with lock:
                with open(filename, "r") as f:
                    numbers = [int(line) for line in f]
                sum_of_numbers = sum(numbers)
                print(f"Sum of numbers: {sum_of_numbers}")
            with lock:
                open(filename, "w").close()

def read_from_file(filename, lock):
    while True:
        with lock:
            with open(filename, "r") as f:
                lines = f.readlines()
            if len(lines) == 10:
                numbers = [int(line.strip()) for line in lines]
                sum_of_numbers = sum(numbers)
                print(f"Sum of numbers: {sum_of_numbers}")
                with lock:
                    open(filename, "w").close()


if __name__ == "__main__":
    filename = "numbers.txt"
    lock = threading.Lock()

    writer_thread = threading.Thread(target=write_to_file, args=(filename, lock))
    reader_thread = threading.Thread(target=read_from_file, args=(filename, lock))

    writer_thread.start()
    reader_thread.start()

    writer_thread.join()
    reader_thread.join()