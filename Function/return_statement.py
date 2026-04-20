def cal_marks(eng, hin,comp,sst,pt):
    return eng + hin + comp + sst + pt
# here we store the function to the variable "t" because we can't directly return the 
t= cal_marks(12,43,65,56,78)
print(f"total marks {t}.")
# This code will NOT give an error.

# def cal_marks(eng, hin, comp, sst, pt):
#     return eng + hin + comp + sst + pt

# cal_marks(12,43,65,56,78)

# Explanation:
# The function is being called correctly and it returns a value,
# but you are NOT doing anything with that returned value.

# Python will calculate the result, but it won't display it
# because there is no print statement.

# So:
# - No error will occur ✅
# - But no output will be shown ❗

# To see the result, you must either:
# 1. Store it in a variable and print it
# 2. Directly print the function call

# Example 1:
# t = cal_marks(12,43,65,56,78)
# print(t)

# Example 2:
# print(cal_marks(12,43,65,56,78))

# Key Concept:
# "return" sends value back, but "print" is required to display it.