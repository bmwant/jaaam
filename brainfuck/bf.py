#!/usr/bin/env python
import sys
import argparse
from typing import Optional


class BrainFuck(object):

    MEM_CELLS = 30_000  # as per original implementation
    CHARACTERS = '><+-.,[]'

    def __init__(self, source: str = ''):
        self.debug = False
        self._source : str = source
        self._pointer = 0
        self._memory = [0 for _ in range(self.MEM_CELLS)]

    def load(self, filepath):
        with open(filepath) as f:
            self._source = self.strip_comments(f.read())

    @staticmethod
    def strip_comments(code: str):
        return ''.join(
            filter(
                lambda ch: ch in BrainFuck.CHARACTERS,
                code
            )
        )

    @property
    def data(self):
        return self._memory[self._pointer]

    @data.setter
    def data(self, value):
        self._memory[self._pointer] = value

    def _get_char_at(self, cursor: int) -> Optional[str]:
        try:
            return self._source[cursor]
        except IndexError:
            pass

    def print_state(self):
        print(self._pointer, self._memory[:20])

    def run(self):
        cursor = 0
        while ch := self._get_char_at(cursor):
            if self.debug:
                self.print_state()

            match ch:
                case '>':
                    self._pointer += 1
                case '<':
                    self._pointer -= 1
                case '+':
                    self.data += 1
                case '-':
                    self.data -= 1
                case '.':
                    print(chr(self.data), end='', flush=True)
                case ',':
                    # NOTE: one char input at a time is supported for now
                    self.data = ord(input()[:1])
                case '[':
                    if self.data == 0:
                        cursor = self._find_matching(']', cursor=cursor) + 1
                        continue
                case ']':
                    if self.data != 0:
                        cursor = self._find_matching('[', cursor=cursor)
                        continue
                case _:
                    raise ValueError(f'Wrong command {ch} is found!')
            cursor += 1

    def _find_matching(self, bracket: str, cursor: int = 0) -> Optional[int]:
        direction = -1 if bracket == '[' else 1
        counter = 1
        while counter:
            cursor += direction
            ch = self._get_char_at(cursor)
            if not ch:
                raise ValueError('Cannot find matching bracket!')
            if ch == ']':
                counter -= direction
            if ch == '[':
                counter += direction

        return cursor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='*.b source file you want to run')
    args = parser.parse_args()

    interpreter = BrainFuck()
    interpreter.load(args.filepath)
    try:
        interpreter.run()
    except KeyboardInterrupt:
        print('\nBye!')
        sys.exit(interpreter.data)


if __name__ == '__main__':
    main()
