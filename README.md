# Uncommon Python Error: ZeroDivisionError in Average Calculation

This repository demonstrates a subtle error in a Python function designed to calculate the average of a list of numbers. The function handles empty lists correctly, but it fails when encountering a list containing a zero. This failure isn't a simple `ZeroDivisionError`; it's about the function's behavior in unexpected situations.

## The Bug

The primary issue is that the function doesn't explicitly check for zero values within the list before performing the division, leading to unexpected results if zeros are present.  This is more than just a `ZeroDivisionError` because the function should be robust to these values.

## The Solution

The solution implements a check for zero values, handling cases where a list contains zeros by returning 0, making the function robust to different types of input.

## How to Run

1. Clone this repository.
2. Run `bug.py` to see the original behavior and the resulting error.
3. Run `bugSolution.py` to see the corrected version and its correct handling of edge cases.