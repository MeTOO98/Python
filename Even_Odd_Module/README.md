# Even_Odd

**Even_Odd** is a simple Python module that provides two functions to determine whether a given number is even, odd, or zero. The module demonstrates two different methods to perform this check — using the remainder operator and bitwise operations.

## Features

- Check if a number is even, odd, or zero.
- Two different implementation techniques:
  - Modulo-based check.
  - Bitwise-based check.
- Lightweight and beginner-friendly.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/Even_Odd.git
cd Even_Odd
```



Then import the functions into your Python code:

```bash
from Even_Odd import even_odd1, even_odd2
```

## Usage

```bash
even_odd1(10)
# Output: number is Even

even_odd1(5)
# Output: number is Odd

even_odd1(0)
# Output: number is Zero


even_odd2(10)
# Output: number is Even

even_odd2(5)
# Output: number is Odd

even_odd2(0)
# Output: number is Zero

```

| Function         | Description                                                       |
| ---------------- | ----------------------------------------------------------------- |
| `even_odd1(num)` | Uses the modulo operator `%` to check if a number is even or odd. |
| `even_odd2(num)` | Uses bitwise AND `&` to check if a number is even or odd.         |


