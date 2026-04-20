#required thinks 
'''def function(name,age):
    print(f"My name is {name} and age is {age}.")

function("Abhay",35)
'''
# optional and required parameters
# there is no relation with the name parameter to this optional parameter 
def fun(eng,hin = 0,sst=0,comp=0,pt=0):
    total = eng+sst+hin+comp+pt
    print(f"Total marks are {total}.")
fun(20,30,40,90,80)
# there should be in the sequence of "required parameter should be in left and optional should be in right it will also show the error"

# ==============================
# PYTHON FUNCTIONS (INTERMEDIATE NOTES)
# ==============================

# Function:
# A function is a reusable block of code designed to perform a specific task.
# Instead of writing the same logic multiple times, we define it once and call it whenever needed.
# This improves code readability, modularity, and maintainability.

# Syntax:
# def function_name(parameters):
#     return result

# Example:
# def add(a, b):
#     return a + b

# Calling:
# result = add(2, 3)

# ------------------------------
# Parameters vs Arguments:
# Parameters are variables in the function definition,
# while arguments are actual values passed during the function call.

# ------------------------------
# Types of Arguments (important in real coding):

# 1. Positional:
# Values are assigned based on order.
# add(2, 3)

# 2. Keyword:
# Values are assigned using parameter names → improves clarity.
# add(a=2, b=3)

# 3. Default:
# If no value is passed, default is used.
# def greet(name="User"):
#     return name

# 4. Variable Length:
# *args → multiple values (tuple)
# **kwargs → multiple key-value pairs (dictionary)

# ------------------------------
# Return Statement:
# The return keyword sends the output back to the caller.
# It makes functions reusable and testable.

# Example:
# def square(x):
#     return x * x

# Note:
# If return is not used, Python returns None by default.

# ------------------------------
# Scope (Very Important Concept):
# Variables inside a function are local and cannot be accessed outside.
# Variables defined outside are global.

# ------------------------------
# Lambda Function:
# A short, anonymous function used for simple operations.

# Example:
# square = lambda x: x * x

# Used mostly in:
# - map()
# - filter()
# - sorting

# ------------------------------
# Recursion:
# A function calling itself to solve smaller subproblems.
# Must have a base condition to stop recursion.

# Example:
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# ------------------------------
# Practical Insight:
# In real projects (like data engineering or ML),
# functions are used to:
# - clean data
# - transform datasets
# - reuse ETL logic
# - modularize pipelines

# Always prefer:
# - small, focused functions
# - meaningful names
# - return values instead of print()