import multiprocessing as mp
import os
import time
from Solution.Logger import Logger
from Solution.part1_build_dataset import fetch_data, save_data_to_csv, clear_csv_file
from multiprocessing import Lock


symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "SOLUSDT", "DOGEUSDT", "DOTUSDT", "MATICUSDT", "LTCUSDT"]

def main():
    manager = mp.Manager()
    lock = manager.Lock()  # This lock can be shared across processes    
    clear_csv_file()
    # Use Pool with processes equal to number of symbols
    start = time.perf_counter()
    with mp.Pool(processes=len(symbols)) as pool:
        # Use apply_async for better control with shared objects
        results = []
        for symbol in symbols:
            result = pool.apply_async(process_symbol, args=(symbol, lock))
            results.append(result)

        # Wait for all results to complete
        for result in results:
            result.wait()
    end = time.perf_counter()
    print(f"Total execution time in parallel: {end - start:.2f} seconds")
    execution_sequentailly() 

def execution_sequentailly():
    start = time.perf_counter()
    for symbol in symbols:
        save_data_to_csv(fetch_data(symbol, "1h", 1000), symbol, "1h")
    end = time.perf_counter()
    print(f"Total execution time sequentially: {end - start:.2f} seconds")

def process_symbol(symbol, lock):
    """Function to be called by each process"""
    try:
        Logger.log(f"Process {os.getpid()}: Fetching data for {symbol}")
        data = fetch_data(symbol, "1h", 1000)
        save_data_to_csv(data, symbol, "1h")
        Logger.log(f"Process {os.getpid()}: Completed {symbol} - {len(data)} records")
        return f"Success: {symbol}"
    except Exception as e:
        Logger.log(f"Process {os.getpid()}: Error with {symbol}: {e}", logLevel="ERROR")
        return f"Error: {symbol}"

if __name__ == "__main__":
    main()