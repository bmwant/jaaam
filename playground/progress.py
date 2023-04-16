"""
Simple progress bar
"""
import time
import math

GREEN = "\033[32m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"


class Progress:
    def __init__(self, total: int = 100):
        self._current = 0
        self._total = total

    def __enter__(self):
        print(f"{CYAN}Working...{RESET}")
        self._redraw()
        return self
    
    def __exit__(self, *args, **kwargs):
        print(f"\n{MAGENTA}DONE!{RESET}")

    def _redraw(self):
        print(f"\r{GREEN}|", end="")
        # we have 10 whole blocks each 10% section
        # completed = math.ceil(self._current/10)
        completed = self._current // 10
        left = 10 - completed
        for _ in range(completed):
            print("█", end="")
        for _ in range(left):
            print(" ", end="")
        print(f"|{RESET}", end="", flush=True)

    def update(self, value: int):
        # max-min here is needed too
        self._current += value
        self._redraw()
    
    def advance(self, to_value: int):
        self._current = max(self._current, to_value)
        self._current = min(self._current, self._total)
        self._redraw()


def main():
    with Progress() as p:
        for i in range(10):
            time.sleep(0.15)
            p.update(10)
    

if __name__ == "__main__":
    # print(f"{GREEN}hello{RESET} and normal")
    main()