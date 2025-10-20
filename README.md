# Cloudfide Junior Data Engineer Recruitment Task

## Description
This repository contains the solution for the Cloudfide Junior Data Engineer coding assignment.  
The task involves creating a new virtual column in a Pandas DataFrame based on a textual representation of operations to be performed on existing columns.

---

## Components
`solution.py` - Contains the add_virtual_column function
`test_virtual_column 1.py`  Unit tests for the function
`README.md` - This file

---

## Python Version and Dependencies

- **Python version:** 3.10.1  
- **Required packages:**
  - `pandas`
  - `re`

--- 

## Function Overview
`add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame`

Purpose: Adds a new column to the given DataFrame by evaluating a simple arithmetic operation (+, -, *) between two existing columns.

Parameters:

- df – input Pandas DataFrame

- role – a string defining the operation (e.g., "weight - weight_year_ago")

- new_column – name of the new column to add

Returns: A new DataFrame including the additional virtual column. Returns an empty DataFrame if:

- Column names are invalid (must contain only letters and underscores)

- The role expression is invalid

- Any referenced column in role does not exist
 
