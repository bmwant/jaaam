import threading
import time

NUM_THREADS = 10_000
NUM_ITERATIONS = 1_000
# Create a lock object and a shared variable
lock = threading.Lock()
shared_variable = 0


def worker_proper(lock):
    # Acquire the lock before accessing the shared variable
    lock.acquire()
    try:
        # Modify the shared variable
        shared_variable += 1
    finally:
        # Release the lock when we're done
        lock.release()


def worker():
    global shared_variable
    time.sleep(0.1)
    for i in range(NUM_ITERATIONS):
        shared_variable += 1


# Create some worker threads
threads = [
    threading.Thread(target=worker)
    for _ in range(NUM_THREADS)
]

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the value of the shared variable
expected = NUM_THREADS * NUM_ITERATIONS
print(shared_variable)
assert shared_variable == expected, f"should be {expected}"