# Welcome

## Scenario

You have just been hired as a junior data scientist at **Owl Analytics**, a small company that builds market-monitoring dashboards for clients.

Your line manager, **Stelios**, wants to see whether you can move through the full data pipeline, from data collection to cleaning and analysis. During your first week, he asks you to rotate through three teams:

- Team 1: Data Collection, led by Elena
- Team 2: Data Quality, led by Dara
- Team 3: Analytics, led by Zehra

Each team gives you a different part of the project. At the end, you must send Stelios a short report explaining what you built, what you found, and what you would improve.

## Communication Channel

This is the team channel for the final project:

[Final Project Teams channel](https://teams.microsoft.com/l/channel/19%3A71895f22c3a942288fc6b46a10e82b80%40thread.tacv2/Final%20Project?groupId=8b3672d8-2c38-4134-9725-3b779f03c2b0&tenantId=89d07f47-d258-463c-8700-635ffaeca38e)

You may use this channel to ask for help, request clarifications, discuss problems, and check that you understand the assignment requirements.

## AI Usage

You may use AI tools to debug your code, explore examples, understand errors, or get ideas that help you solve the assignment.

The final code, analysis, report, and reflection must be yours. You must understand what you submit and be able to explain your work.

## Company problem

Owl Analytics wants to monitor recent cryptocurrency market activity for several symbols.

The company wants to understand which symbols are most active, which symbols are most volatile, when trading activity is highest, whether the data pipeline can handle the required 10,000 records, and whether the data is clean enough for analytics.

## API

You will use the Binance public market data API to extract data.

Endpoint:

```txt
https://data-api.binance.vision/api/v3/klines
```

Example request:

```txt
https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=1000
```

To test the API before building your full downloader, run:

```bash
python scripts/get_one_record.py
```

This script downloads one `BTCUSDT` record and saves it as `data/clean/one_record.csv`. Reuse the same API idea when you build `part1_build_dataset.py`.

Useful documentation:

- [Binance Spot REST API documentation](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md)
- [Binance market-data-only FAQ](https://github.com/binance/binance-spot-api-docs/blob/master/faqs/market_data_only.md)

If the Binance API is unavailable, ask your instructor before switching API.

## Dataset specification

Use these ten symbols:

- `BTCUSDT`
- `ETHUSDT`
- `BNBUSDT`
- `SOLUSDT`
- `XRPUSDT`
- `ADAUSDT`
- `DOGEUSDT`
- `AVAXUSDT`
- `LINKUSDT`
- `DOTUSDT`

Use:

- `interval=1h`
- `limit=1000`

This means your downloader should make one request per symbol.

Expected dataset size:

- 10 symbols
- 1,000 records per symbol
- 10,000 records total
- 1 header row in the CSV
- 10,001 lines total in `data/clean/clean_market_data.csv`

The 10,000 records are a mixed collection of market candles across 10 symbols and 1,000 timestamps per symbol.

## Required columns

Field mapping:

| CSV column | Value |
| --- | --- |
| `symbol` | the symbol you requested, for example `BTCUSDT` |
| `interval` | the interval you requested, `1h` |
| `open_time` | `record[0]`, converted to a readable timestamp if possible |
| `open` | `record[1]` |
| `high` | `record[2]` |
| `low` | `record[3]` |
| `close` | `record[4]` |
| `volume` | `record[5]` |
| `close_time` | `record[6]`, converted to a readable timestamp if possible |
| `quote_volume` | `record[7]` |
| `trade_count` | `record[8]` |
| `taker_buy_base_volume` | `record[9]` |
| `taker_buy_quote_volume` | `record[10]` |

Example dataset sample:

| symbol | interval | open_time | open | high | low | close | volume | close_time | quote_volume | trade_count |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| BTCUSDT | 1h | 2026-05-28T00:00:00+00:00 | 108742.01 | 109120.44 | 108330.50 | 108990.32 | 1284.52 | 2026-05-28T00:59:59+00:00 | 139957223.15 | 84231 |
| ETHUSDT | 1h | 2026-05-28T00:00:00+00:00 | 2638.22 | 2661.40 | 2625.12 | 2654.77 | 18452.83 | 2026-05-28T00:59:59+00:00 | 48978103.62 | 53480 |
| SOLUSDT | 1h | 2026-05-28T00:00:00+00:00 | 168.45 | 170.10 | 167.88 | 169.72 | 93211.14 | 2026-05-28T00:59:59+00:00 | 15796231.88 | 42190 |
