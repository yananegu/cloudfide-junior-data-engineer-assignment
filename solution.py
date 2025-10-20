
import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame: 
    
    # Check the validity of the new column name 
    if not new_column.replace('_', '').isalpha():
        return pd.DataFrame()
    
    # Check the validity of all current column names in df
    if not df.columns.str.replace('_', '').str.isalpha().all():
        return pd.DataFrame()
    
    # Check that role has the format "col1 <op> col2"
    # Prevent invalid expressions: unsupported operators, missing operands, double operators, or numbers instead of column names
    pattern = r'^\s*[A-Za-z_]+\s*[\+\-\*]\s*[A-Za-z_]+\s*$'
    if not re.match(pattern, role):
        return pd.DataFrame() 
    
    # Check if columns from role exist in df
    cols = re.findall(r'[A-Za-z_]+', role)
    if any(col not in df.columns for col in cols):
        return pd.DataFrame() 
    
    df = df.copy()  # Create a copy to avoid modifying the original df
    df[new_column] = df.eval(role) #Using df.eval() to evaluate a dynamic expression between columns, after verifying column names
    return df 