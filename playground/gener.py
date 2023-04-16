

def gen_wrapper():
    def gen_digits():
        # digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        yield from range(10)

    def gen_chars():
        chars = ["a", "b", "c", "d", "e"]
        yield from chars
    
    iter_d = gen_digits()
    iter_c = gen_chars()

    dq = [iter_d, iter_c]  # like dequeue
    while dq:
        # like popleft
        current = dq[0]
        dq = dq[1:]
        try:
            yield next(current)
        except StopIteration:
            continue
        # still not exhausted
        dq.append(current)
    

if __name__ == "__main__":
    iter = gen_wrapper()
    for i in iter:
        print(f"Got {i}")