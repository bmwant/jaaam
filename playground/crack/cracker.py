"""
Stop search as soon as correct solution is found.
Use threading.Event for synchronization
"""
import hashlib
import time
import functools
import itertools
import string
from threading import Event
from dataclasses import dataclass
from concurrent import futures

from crack.data import HASH_FUNCTIONS

# hashlib.algorithms_available

MAX_WORKERS = 10
FOUND = Event()


@dataclass
class Result:
    guess: str
    target_hash: str
    match: bool = False
    algorithm: str = "md5"


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


def check(guess: str, target: str, algorithm: str = "md5") -> Result:
    # print(".", end="")
    match = encrypt(guess, algorithm=algorithm) == target
    return Result(
        guess=guess,
        target_hash=target,
        match=match,
        algorithm=algorithm,
    )


def done_callback(future):
    try:
        result: Result = future.result()
    except futures.CancelledError:
        # Solution was found, pending tasks are cancelled
        return

    if result.match is True:
        FOUND.set()
        print(f"\nFound match! {result}")


@timeit
def crack(target_hash: str):
    vocabulary = string.ascii_letters + string.digits

    tasks = []
    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        options = list(itertools.product(vocabulary, repeat=4))
        for product in options:
            if FOUND.is_set():
                executor.shutdown(wait=False, cancel_futures=True)
                return
            guess = "".join(product)
            task = executor.submit(check, guess, target_hash)
            task.add_done_callback(done_callback)
            tasks.append(task)
        
    if not FOUND.is_set():
        print("\nNo solution was found")
     

"""
thread pool executor, 10 workers, funnybouncy1350
10_000: 0.89s
100_000: 0.87s
1_000_000: 0.87s
10_000_000: 1.05s
ALL: 0.96s
"""
