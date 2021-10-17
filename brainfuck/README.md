Interpreter for the [Brainfuck](https://esolangs.org/wiki/Brainfuck) programming language written in Python. Works for versions `3.10` and above.

![triangle](./sierpinski.png)

### Usage

Check `examples` directory and run any of the files like this

```bash
$ ./bf.py examples/hello_world.b
$ python bf.py examples/squares.b  # explicitly select python interpreter to run withs
$ ./bf.py examples/fib.b  # Ctrl+C to terminate
```

### Running tests

```bash
$ python tests.py
```

### TODO

* `test4.b` should fail with an error
* input should be handled for multicharacter lines
* `EOF` should be added to input handling
* `debug` should be as a flag to run
* `xmastree.b` should work?
