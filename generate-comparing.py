import random
import time
import threading

def generate_and_write_numbers_to_file(filename):
    with open(filename, 'w') as f:
        for i in range(1000000):
            num = random.randint(1, 100)
            f.write(str(num) + '\n')

def sequential():
    for i in range(10):
        filename = f'file_{i}.txt'
        generate_and_write_numbers_to_file(filename)

def multithreaded():
    threads = []
    for i in range(10):
        filename = f'file_{i}.txt'
        t = threading.Thread(target=generate_and_write_numbers_to_file, args=(filename,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    start_time = time.time()
    sequential()
    end_time = time.time()
    print(f'Sequential time: {end_time - start_time:.2f} seconds')

    start_time = time.time()
    multithreaded()
    end_time = time.time()
    print(f'Multithreaded time: {end_time - start_time:.2f} seconds')
