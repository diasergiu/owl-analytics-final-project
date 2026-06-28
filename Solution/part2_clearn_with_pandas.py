import pandas as pd

from Solution.Logger import Logger

# part 1
def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        Logger.log(f"Error loading data from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    
# part 1
def print_data(df: pd.DataFrame) -> pd.DataFrame:
    print(df.shape)
    print("--------------------------------")
    print(df.head(10))
    print("--------------------------------")
    print(df.dtypes)
    print("--------------------------------")
    print(df.describe())
#part 2
    print("--------------------------------")
    print(df.isnull().sum())
    print("the buggest missing column is ", df.count().idxmin(), "with", df[df.count().idxmin()].isnull().sum(), "missing values")

# symbol,
# interval,
# open_time
# ,open,high,
# low,close,
# volume,
# close_time,
# quote_volume,
# trade_count,
# taker_buy_base_volume,
# taker_buy_quote_volume

# part 3 I do not differantiate between int and float, I just convert all to float64
def clean_string_into_int(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Convert a string column to integer, handling errors. price, volume, and trade-count"""
    df[column_name] = pd.to_numeric(df[column_name], errors="coerce").astype("float64")
    print(df[column_name].head(10))
    return df


# part 4 
def clean_string_into_datetime(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Convert a string column to datetime, handling errors."""
    df[column_name] = pd.to_numeric(df[column_name], errors="coerce").astype("Int64")
    df[column_name] = pd.to_datetime(df[column_name], unit='ms', utc=True)
    print("correction tadetime", df[column_name].head(50))
    return df

def clean_symbol_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Clean the symbol column by converting to uppercase."""
    df[column_name] = df[column_name].str.replace(r"[^A-Za-z0-9]", "", regex=True).str.upper()
    print(df.head(50))
    return df

# Part 5
def find_and_remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Find and remove duplicate rows in the DataFrame."""
    print("Number of rows before removing duplicates:", df.shape[0])
    print("Number of duplicate rows:", df.duplicated().sum())
    df = df.drop_duplicates()
    print("Number of rows after removing duplicates:", df.shape[0])
    return df

# part6
def correct_non_negative(df: pd.DataFrame, numeric_columns: list) -> pd.DataFrame:
    """Correct numeric columns by converting negative values to zero."""
    for column in numeric_columns:
        df[column] = df[column].apply(lambda x: max(x, 0) if pd.notnull(x) else x)
    return df

def correct_high_low(df: pd.DataFrame) -> pd.DataFrame:
    """Correct the 'high' and 'low' columns to ensure 'high' >= 'low'."""
    df['high'] = df[['high', 'low']].max(axis=1)
    df['low'] = df[['high', 'low']].min(axis=1)
    return df

# part 7
def new_column_differance(df: pd.DataFrame, column1: str, column2: str, new_column_name: str) -> pd.DataFrame:
    """Create a new column that is the difference between two existing columns."""
    df[new_column_name] = df[column1] - df[column2]
    return df

def new_column_percentage(df: pd.DataFrame, column1: str, column2: str, new_column_name: str) -> pd.DataFrame:
    """Create a new column that is the percentage difference between two existing columns."""
    df[new_column_name] = (df[column1] / df[column2]) * 100
    return df

def set_dirrection(df: pd.DataFrame, new_column_name: str) -> pd.DataFrame:
    """Create a new column that indicates the direction of change based on the 'close' and 'open' columns."""
    df[new_column_name] = df.apply(lambda row: "up" if row["close"] > row["open"] else ("down" if row["close"] < row["open"] else "flat"), axis=1)
    return df


def save_data_to_csv(df: pd.DataFrame, file_path: str):
    """Save the DataFrame to a CSV file."""
    try:
        df.to_csv(file_path, index=False)
        Logger.log(f"Data saved to {file_path}")
    except Exception as e:
        Logger.log(f"Error saving data to {file_path}: {e}")

