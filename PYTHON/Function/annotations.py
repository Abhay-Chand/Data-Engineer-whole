def greet(n:str,a:int,g:str):
    print(f"Name is {n}")
    print(f"Age is {a}")
    print(f"Gender is {g}")

greet("Abhay",66,"male")

# ==============================
# PYTHON ANNOTATIONS (TYPE HINTS)
# ==============================

# Annotation:
# Annotations (also called type hints) are used to specify the expected data types
# of function parameters and return values. They improve code readability and help
# in debugging, but Python does NOT enforce them at runtime.

# Syntax:
# def function_name(parameter: data_type) -> return_type:
#     return value

# Example:
# def add(a: int, b: int) -> int:
#     return a + b

# ------------------------------
# Key Idea:
# Annotations are not mandatory and do not restrict input.
# They act as guidance for developers and tools (like IDEs, linters).

# Example (Python will NOT give error):
# add("2", "3")  # Still works, even though type hints say int

# ------------------------------
# Common Data Types in Annotations:

# int, float, str, bool
# list, tuple, dict, set

# Example:
# def process(data: list) -> dict:
#     return {"length": len(data)}

# ------------------------------
# Using 'Any' (Flexible Type):

# from typing import Any
# def print_data(x: Any) -> None:
#     print(x)

# ------------------------------
# Multiple Types (Union):

# from typing import Union
# def square(x: Union[int, float]) -> float:
#     return x * x

# ------------------------------
# Optional Values:

# from typing import Optional
# def greet(name: Optional[str] = None) -> str:
#     return name if name else "Guest"

# ------------------------------
# List with Specific Type:

# from typing import List
# def total(nums: List[int]) -> int:
#     return sum(nums)

# ------------------------------
# Dictionary Annotation:

# from typing import Dict
# def get_user() -> Dict[str, int]:
#     return {"age": 21}

# ------------------------------
# Practical Importance:

# - Helps in large projects (data engineering, ML pipelines)
# - Improves code clarity for teams
# - Used by tools like mypy for static type checking
# - Makes debugging easier

# ------------------------------
# Important Note:
# Python is dynamically typed → annotations are just hints, not strict rules.