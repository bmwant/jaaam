"""
Measure time separately for generation and collection steps.
Use process poll executor for comparison.
"""
import hashlib
import time
import functools
import itertools
import string
from concurrent import futures
from dataclasses import dataclass

from crack.data import DATABASE, HASH_FUNCTIONS


MAX_WORKERS = 20

@dataclass
class Result:
    guess: str
    target_hash: str
    match: bool = False
    algorithm: str = "sha256"


def encrypt(data: str, algorithm: str = "md5"):
    assert algorithm in HASH_FUNCTIONS, "unsupported encryption algorithm"
    h = hashlib.new(algorithm)
    h.update(data.encode())
    digest = h.hexdigest()
    # print(digest)
    return digest


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        took = end_time - start_time
        print(f"{func.__name__} took {took:.6f} seconds")
        return result
    return wrapper


def check(guess: str, target: str) -> Result:
    # print(".", end="")
    match = encrypt(guess, algorithm="sha256") == target
    return Result(
        guess=guess,
        target_hash=target,
        match=match,
    )


@timeit
def crack(target_hash: str):
    vocabulary = string.ascii_letters + string.digits

    @timeit
    def generate_tasks(executor):
        tasks = []
        # NOTE: 70_000 DOES NOT WORK HERE!
        options = list(itertools.product(vocabulary, repeat=4))[:69_999]
        for product in options:
            guess = "".join(product)
            task = executor.submit(check, guess, target_hash)
            tasks.append(task)
        return tasks
    
    @timeit
    def collect_results(tasks, executor) -> bool:
        for future in futures.as_completed(tasks):
            result: Result = future.result()
            if result.match is True:
                print(f"\nFound match! {result}")
                executor.shutdown(wait=False, cancel_futures=True)
                return True
        print("\nNo match found :(")
        return False
    
    with futures.ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        tasks = generate_tasks(executor=executor)
        collect_results(tasks=tasks, executor=executor)
     

if __name__ == "__main__":
    crack("e8fdedf5163af505f15438bd233b61ab62eb0824ea1c5aa0702f6f8169d40cdc")

"""
thread pool executor, 10 workers, funnybouncy1350
generate / collect / crack
10_000: 0.89s / 0.01s / 0.91s
100_000: 1.44s / 0.10s / 1.59s
1_000_000: 8.57s / 1.46s / 10.37s
10_000_000: 123.29s / 40.80s / 169.39s

process pool executor, 10 workers, funnybouncy1350
generate / collect / crack
10_000: 0.94s / 0.48s / 1.47s
100_000: ???
1_000_000: ???
10_000_000: ???
"""
