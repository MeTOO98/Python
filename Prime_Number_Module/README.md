
# PrimeNum

A simple Python module for checking whether a number is a prime. It includes two functions: a basic implementation and an optimized version.

## Features

- ✅ Check if a number is prime
- 🚫 Handles negative numbers and zero gracefully
- ⚡ Includes a more optimized function for performance

## Installation

You can clone the repository and import the module into your Python project:

```bash
git clone https://github.com/your-username/PrimeNum.git
```

Then, import the module in your Python script:
```bash
from PrimeNum import prime_num1, prime_num2
```

## Usage
```bash
prime_num1(num)
Basic version of prime number check.


>>> from PrimeNum import prime_num1
>>> prime_num1(7)
True

>>> prime_num1(8)
False

prime_num2(num)
More optimized version of the prime number check.


>>> from PrimeNum import prime_num2
>>> prime_num2(11)
True

>>> prime_num2(-4)
False
```

## Function Descriptions

#### prime_num1(num)
Returns True if num is prime; otherwise False. Handles negatives by converting them to positive. Loops up to num - 1.

#### prime_num2(num)
Optimized prime check that loops only up to num // 2 for better performance on larger values.






