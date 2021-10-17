class BrainFuck(object):

    MEM_CELLS = 30_000  # as per original implementation
    CHARACTERS = '><+-.,[]'

    def __init__(self):
        self._source : str = ''
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

    def run(self):
        for i, c in enumerate(self._source):
            match c:
                case '>':
                    self._pointer += 1
                case '<':
                    self._pointer -= 1
                case '+':
                    raise NotImplementedError('+ is not here yet')
                case '-':
                    raise NotImplementedError('- is not here yet')
                case '.':
                    raise NotImplementedError('+ is not here yet')
                case ',':
                    raise NotImplementedError('+ is not here yet')
                case '[':
                    raise NotImplementedError('+ is not here yet')
                case ']':
                    raise NotImplementedError('+ is not here yet')
                case _:
                    raise ValueError(f'Wrong command {c} is found!')


def main():
    interpreter = BrainFuck()
    interpreter.load('./examples/hello_world.b')
    interpreter.run()


if __name__ == '__main__':
    main()
