import hashlib
from concurrent.futures import ThreadPoolExecutor
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


def encrypt(data: str, algorithm: str = "md5"):
    assert algorithm in HASH_FUNCTIONS, "unsupported encryption algorithm"
    h = hashlib.new(algorithm)
    h.update(data.encode())
    digest = h.hexdigest()
    print(digest)
    return digest


def check(guess: str, target: str) -> bool:
    return encrypt(guess, algorithm="md5") == target

import itertools
import string
def crack():
    vocabulary = string.ascii_letters + string.digits

with ThreadPoolExecutor(max_workers=4) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())


if __name__ == "__main__":
    pass
