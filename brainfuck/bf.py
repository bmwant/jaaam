from itertools import filterfalse

class BrainFuck(object):

    CHARACTERS = '><+-.,[]'

    def __init__(self):
        self._source : str = ''

    def load(self, filepath):
        with open(filepath) as f:
            self._source = self.strip_comments(f.read())
            print(self._source)

    @staticmethod
    def strip_comments(code: str):
        return ''.join(
            filter(
                lambda ch: ch in BrainFuck.CHARACTERS,
                code
            )
        )

    def run(self):
        pass


def main():
    interpreter = BrainFuck()
    interpreter.load('./examples/hello_world.bf')
    interpreter.run()


if __name__ == '__main__':
    main()
