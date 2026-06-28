import csv 
import multiprocessing as mp
import requests
from pathlib import Path
from Solution.Logger import Logger

write_Lock = mp.Lock()
fieldnames = ["symbol", "interval", "open_time", "open", "high", "low", 
                  "close", "volume", "close_time", "quote_volume", 
                  "trade_count", "taker_buy_base_volume", "taker_buy_quote_volume"]
path = Path(f"data/clean/clean_market_data.csv")

def fetch_data (symbol: str, interval: str = "1h", limit: int = 1000):
    url = "https://data-api.binance.vision/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
    }
    # Logger.log(f"Fetching data for {symbol} with interval {interval} and limit {limit}")    
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    # Logger.log(f"Successfully fetched data for {symbol} with interval {interval} and limit {limit}")
    return response.json()

def clear_csv_file():
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def save_data_to_csv(records , symbol: str, interval: str, lock):
    with lock:
        save_data_to_csv(records, symbol, interval)
        
# writes contunuasly to file, 
def save_data_to_csv(records , symbol: str, interval: str):
    # Logger.Log(f"Saving data for {symbol} with interval {interval} to CSV")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        for record in records:
            row = {
                "symbol": symbol,
                "interval": interval,
                "open_time": record[0],
                "open": record[1],
                "high": record[2],
                "low": record[3],
                "close": record[4],
                "volume": record[5],
                "close_time": record[6],
                "quote_volume": record[7],
                "trade_count": record[8],
                "taker_buy_base_volume": record[9],
                "taker_buy_quote_volume": record[10],
            }
            writer.writerow(row)
    # Logger.log(f"Successfully saved data for {symbol} with interval {interval} to CSV")
