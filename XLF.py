import pandas as pd
import ta

def ripster_test_strategy(df):
    df['ema5'] = ta.trend.ema_indicator(df['close'], window=5)
    df['ema13'] = ta.trend.ema_indicator(df['close'], window=13)

    df['long'] = df['ema5'] > df['ema13']
    df['short'] = df['openprofit'] > 300

    df['signal_long'] = df['long'].shift(1) & ~df['long']
    df['signal_short'] = df['short'].shift(1) & ~df['short']

    df['position'] = 0
    df.loc[df['signal_long'], 'position'] = 1000
    df.loc[df['signal_short'], 'position'] = -1000

    df['position'] = df['position'].ffill().fillna(0)
    df['position'] = df['position'].astype(int)

    df['close_position'] = False
    df.loc[df['signal_long'] & df['short'], 'close_position'] = True
    df.loc[df['signal_short'] & df['long'], 'close_position'] = True

    df['close_position'] = df['close_position'].shift(1).fillna(False)
    df['close_position'] = df['close_position'] | df['long'] | df['short']

    return df

# Example usage
data = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with your actual data file
data['timestamp'] = pd.to_datetime(data['timestamp'])  # Convert timestamp column to datetime if needed
data.set_index('timestamp', inplace=True)

processed_data = ripster_test_strategy(data)
print(processed_data)
