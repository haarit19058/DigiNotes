
# What are those libraries

Certainly! Here’s an overview of the `dataclasses` and `typing` libraries in Python:

### `dataclasses` Library

- **Purpose**: The `dataclasses` module provides a decorator and functions for creating data classes, which are classes primarily used to store values and provide boilerplate code for common methods.
  
- **Features**:
  - **`@dataclass` Decorator**: This decorator automatically generates special methods for classes, such as `__init__`, `__repr__`, `__eq__`, and `__hash__`.
  - **Automatic Method Generation**: The `@dataclass` decorator generates methods like `__init__` for initializing attributes, `__repr__` for a readable string representation, and `__eq__` for equality comparison based on the values of the attributes.
  - **Default Values**: You can specify default values for attributes and use the `field` function for more advanced configurations.

- **Example**:
  ```python
  from dataclasses import dataclass

  @dataclass
  class Person:
      name: str
      age: int

  p1 = Person(name="Alice", age=30)
  print(p1)  # Output: Person(name='Alice', age=30)
  ```

### `typing` Library

- **Purpose**: The `typing` module provides support for type hints, which help with static type checking and improve code readability by specifying the expected types of variables, function arguments, and return values.

- **Features**:
  - **`Literal`**: A type hint that specifies that a value must be one of a specific set of values. It is used for values that are not just of a certain type, but also constrained to a set of literal values.

- **Example**:
  ```python
  from typing import Literal

  def handle_status(status: Literal['success', 'error']) -> None:
      if status == 'success':
          print("Operation was successful!")
      elif status == 'error':
          print("There was an error.")
  
  handle_status('success')  # Valid
  handle_status('failure')  # Type error if checked by a static type checker
  ```

In summary:
- **`dataclasses`** is used for creating classes that are primarily containers for data with automatic method generation.
- **`typing`** is used for providing type hints to help with static type checking and to make the code more understandable.