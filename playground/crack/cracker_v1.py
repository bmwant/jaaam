"""
Simple approach with thread pool executor
"""

import hashlib
import time
import functools
from concurrent import futures
from crack.data import DATABASE, HASH_FUNCTIONS


MAX_WORKERS = 20
import itertools
import string
from dataclasses import dataclass


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
    tasks = []
    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        options = list(itertools.product(vocabulary, repeat=4))[:10_000_000]
        for product in options:
            guess = "".join(product)
            task = executor.submit(check, guess, target_hash)
            tasks.append(task)

        for future in futures.as_completed(tasks):
            result: Result = future.result()
            if result.match is True:
                print(f"\nFound match! {result}")
                executor.shutdown(wait=False, cancel_futures=True)
                break


if __name__ == "__main__":
    crack("e8fdedf5163af505f15438bd233b61ab62eb0824ea1c5aa0702f6f8169d40cdc")

"""
thread pool executor, 20 workers, funnybouncy1350
10_000: 0.909120 s
100_000: 1.567167 s
1_000_000: 10.040773 s
10_000_000: 175.312619 s
"""
