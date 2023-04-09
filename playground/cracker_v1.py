import hashlib
import time
import functools
from concurrent import futures
# hashlib.algorithms_available
"""
bluegreen5419, md5, 1234
jollybouncy3231, md5, asdf
mellowhappy6721, md5, wxyz

greenyellow3214, sha256, aa11
crazyorange3831, sha256, a9b0
funnybouncy1350, sha256, abCD

sunnymellow2812, blake2s, 777i
redblue4632, blake2s, QqQ3

happyjolly9477, ripemd160, x7Y8
sunnyred1888, ripemd160, pQ93
"""
DATABASE = {
    "bluegreen5419": "81dc9bdb52d04dc20036dbd8313ed055",
    "jollybouncy3231": "912ec803b2ce49e4a541068d495ab570",
    "mellowhappy6721": "a7c3c2aa70d99921f9fb23ac87382997",
    "greenyellow3214": "a9e6f36035dbb98ca558ab151fd95e7f082d44f045f8eac36ace83374e96d333",
    "crazyorange3831": "8b9bde99aff5184f2ceceed8575ac59a6677165bc705f35a0a6055fc480f50d6",
    "funnybouncy1350": "e8fdedf5163af505f15438bd233b61ab62eb0824ea1c5aa0702f6f8169d40cdc",
    "sunnymellow2812": "3c79361da342ebde0edd64c484e8b0660e1a2b8607a2ebc32ea5c22e500e5a99",
    "redblue4632": "750295fd51d093d127b351d1a0a75f9ca3cc19a10ab5477546e605c32d155084",
    "happyjolly9477": "76a89a503fd5726b055622cd26d4882457d048ea",
    "sunnyred1888": "10d6521cb70f4a5dfcd997fcc4f66f136dc90dce",
}


HASH_FUNCTIONS = [
    "md5",
    "sha256",
    "blake2s",
    "ripemd160",
]


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
