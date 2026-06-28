


from Solution.part2_clearn_with_pandas import clean_string_into_datetime, clean_string_into_int, clean_symbol_column, correct_high_low, correct_non_negative, find_and_remove_duplicates, new_column_differance, new_column_percentage, print_data, load_data, set_dirrection

path_messy_data = "data/messy/messy_market_data.csv"

def main():
    # Part 1
    df = load_data(path_messy_data)
    print_data(df)
    # Part 3
    numericChanges = ["open", "high", "low", "close", "volume", "quote_volume", "trade_count"]
    for column in numericChanges:
        clean_string_into_int(df, column)
    print("after cleaning the data")
    print_data(df)

    # Part 4
    dateTimeColumns = ["open_time", "close_time"]
    for column in dateTimeColumns:
        clean_string_into_datetime(df, column)
    clean_symbol_column(df, "symbol")
    # print_data(df)

    # Part 5
    find_and_remove_duplicates(df)


    # Part 6
    numericColumns = ["volume", "trade_count"]
    correct_non_negative(df, numericColumns)
    correct_high_low(df)

    # Part 7
    new_column_differance(df, "high", "low", "price_range")
    new_column_differance(df, "close", "open", "price_change")
    new_column_percentage(df, "price_change", "open", "percent_change")
    set_dirrection(df, "candle_direction")

    print(df.head(50))

if __name__ == "__main__":
    main()