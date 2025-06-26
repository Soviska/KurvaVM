# kurvavm

python implementation of a kurva virtual machine with bytecode interpreter. 
(no serious purpose i just did it because i wanted to do it [: )

## install

```bash
pip install -r requirements.txt
```

## usage

**example 1:** - static.py

```python
from core import Engine, LOAD_STRING, LOAD_NUM, ADD, COMP_EQUAL, COND_JUMP, EXIT

code = bytes([
    LOAD_STRING, 200, 13, 105, 109, 32, 107, 97, 110, 121, 101, 32, 119, 101, 115, 116, // im kanye west
    LOAD_NUM, 13, 5,
    LOAD_NUM, 14, 3,
    ADD, 15, 13, 14,
    ADD, 16, 14, 14,
    COMP_EQUAL, 17, 15, 16,
    COND_JUMP, 17, 0,
    EXIT,
])
vm = Engine(code)
vm.run()
```

**example 2:** - main.py: http request
```python
from core import Engine, LOAD_STRING, PUSH, CALL_BIND, BIND_HTTP_REQ, EXIT

code = bytes([
    LOAD_STRING, 200, 18, 104, 116, 116, 112, 115, 58, 47, 47, 103, 111, 111, 103, 108, 101, 46, 99, 111, 109,
    PUSH, 19,
    PUSH, 18,
    PUSH, 0,
    CALL_BIND, BIND_HTTP_REQ,
    EXIT,
])
vm = Engine(code)
vm.run()
```

## run

```bash
python static.py
python main.py
```

## inspiration

- https://github.com/0xF7A4C6/TinyVM
- https://github.com/jwillbold/rusty-jsyc
- https://github.com/toddmaustin/spectre-rust 
