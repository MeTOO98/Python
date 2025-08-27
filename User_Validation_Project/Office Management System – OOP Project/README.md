# Office Management System – OOP Project

This project simulates an office environment using Object-Oriented Programming (OOP) in Python. It includes managing employees, their vehicles, work routines, salaries, and office operations like hiring, firing, and checking lateness.

## Project Description

The project uses four main classes:

  - Person – Represents a general person with attributes like name, mood, health rate, and money.

  - Employee – Inherits from Person and adds attributes like ID, email, salary, and a Car object.

  - Car – Simulates a car with fuel and velocity management.

  - Office – Manages employee operations like hiring, firing, salary management, and attendance checking.

The goal is to model real-life office interactions using OOP principles like inheritance, encapsulation.

## Features

 - Employee management (hire, fire, reward, deduct)

 - Simulate commuting and fuel usage via Car objects

 - Sleep, eat, and work routines affecting mood and health

 - Lateness calculation with automatic salary deduction/reward

 - Track total number of employees with class-level data

## Project Structure

```

OOP_Project/
│
├── OOP Project.py        # Main Python script with all classes and logic
├── README.md             # Project documentation (this file)

```



## How It Works

### Classes & Methods

#### Person Class
- `__init__(name, money=0)`
- `sleep(hours)`
- `eat(meals)`
- `buy(items)`

#### Employee Class (inherits Person)
- `__init__(id, name, car=None, email="", salary=1000, distancetowork=0)`
- `work(hours)`
- `drive(distance)`
- `refuel(gasAmount)`

#### Car Class
- `__init__(velocity, name="", fuelrate=0)`
- `run(distance, velocity)`
- `stop(distance)`

#### Office Class
- `__init__(name)`
- Methods: 
  - `hire_employee(emp)`
  - `fire_employee(emp_id)`
  - `deduct(emp_id, deduction)`
  - `reward(emp_id, reward)`
  - `check_lateness(emp_id, move_hour)`
  - `get_employee(emp_id)`
  - `calculate_lateness(...)` (static)
  - `change_emps_num(num)` (class)

## Example Scenario

1. Create cars and employees.
2. Assign cars to employees.
3. Create an office and hire employees.
4. Check for lateness and adjust salary accordingly.

```python
c1 = Car(20, "Fiat", 70)
e1 = Employee(10, "Ahmed", c1, "ahmed@yahoo.com", 4000, distancetowork=50)

office = Office("HR")
office.hire_employee(e1)
office.check_lateness(10, 7)
```

## Requirements

- Python 3.x

- No external libraries needed


## Getting Started

1. Clone or download the repository.

2. Run OOP Project.py using any Python 3.x environment.

3. Customize employee/car/office instances as needed.



