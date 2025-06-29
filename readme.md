# KurvaVM: A Minimal Bytecode-Based Virtual Machine in Python

![KurvaVM](https://img.shields.io/badge/KurvaVM-Ready%20to%20Use-brightgreen) ![GitHub release](https://img.shields.io/github/release/Soviska/KurvaVM.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Instruction Set](#instruction-set)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

KurvaVM is a minimal bytecode-based virtual machine designed to execute custom bytecode instructions. Written in Python, this project serves as a proof of concept for a custom virtual machine design and instruction execution. Whether you're a student learning about virtual machines or a developer exploring new ideas, KurvaVM offers a hands-on experience in understanding the fundamentals of stack-based execution.

For the latest releases, visit the [Releases section](https://github.com/Soviska/KurvaVM/releases).

## Features

- **Lightweight**: Minimal overhead for fast execution.
- **Stack-Based**: Utilizes a stack for operations, simplifying instruction execution.
- **Educational**: Great for learning about virtual machines and bytecode.
- **Customizable**: Easy to extend with new instructions and features.
- **Python-Based**: Written in Python for easy modification and understanding.

## Installation

To get started with KurvaVM, clone the repository and install the required dependencies.

```bash
git clone https://github.com/Soviska/KurvaVM.git
cd KurvaVM
pip install -r requirements.txt
```

For the latest executable files, check the [Releases section](https://github.com/Soviska/KurvaVM/releases).

## Usage

KurvaVM can be run directly from the command line. Here’s a simple example to execute a bytecode file:

```bash
python kurvavm.py your_bytecode_file.kvm
```

You can create your own bytecode files by following the instruction set outlined below.

## Architecture

KurvaVM follows a straightforward architecture that includes the following components:

- **Bytecode Loader**: Reads and parses bytecode files.
- **Instruction Executor**: Executes the instructions defined in the bytecode.
- **Stack Management**: Handles stack operations for data storage and retrieval.
- **Error Handling**: Manages exceptions and errors during execution.

This architecture ensures that the virtual machine is both efficient and easy to understand.

## Instruction Set

KurvaVM supports a basic set of instructions. Below is a list of some common instructions:

| Instruction | Description                        |
|-------------|------------------------------------|
| `PUSH`      | Pushes a value onto the stack.     |
| `POP`       | Removes the top value from the stack. |
| `ADD`       | Pops two values, adds them, and pushes the result. |
| `SUB`       | Pops two values, subtracts the second from the first, and pushes the result. |
| `MUL`       | Pops two values, multiplies them, and pushes the result. |
| `DIV`       | Pops two values, divides the first by the second, and pushes the result. |
| `PRINT`     | Pops a value and prints it to the console. |

You can extend this instruction set by modifying the source code.

## Examples

Here are a few examples of bytecode files and how they can be executed.

### Example 1: Simple Addition

Create a file named `add_example.kvm` with the following content:

```
PUSH 5
PUSH 3
ADD
PRINT
```

Run it using:

```bash
python kurvavm.py add_example.kvm
```

This will output `8`.

### Example 2: Subtraction

Create a file named `sub_example.kvm` with the following content:

```
PUSH 10
PUSH 4
SUB
PRINT
```

Run it using:

```bash
python kurvavm.py sub_example.kvm
```

This will output `6`.

## Contributing

We welcome contributions to KurvaVM. If you have ideas for new features or improvements, please fork the repository and submit a pull request. Ensure that your code follows the existing style and includes tests where applicable.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes and commit them.
4. Push to your branch.
5. Open a pull request.

Your contributions help make KurvaVM better for everyone.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out via GitHub issues or directly through the repository.

For the latest releases, check the [Releases section](https://github.com/Soviska/KurvaVM/releases).