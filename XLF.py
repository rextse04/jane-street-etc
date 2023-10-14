import numpy as np
import pandas as pd

from typing import List, Union
from helper import *
from etc_types import *
from typing import List

def ema_strategy(vale_trade_info: List[TradeInfo], valbz_trade_info: List[TradeInfo]) -> List[Trade]:
   

    This algorithm makes use of exponential moving averages.

    Args:

    Returns:
    
        List[Trade]: A list of trades to perform. May be empty.

    """
    if len(vale_trade_price_list) >= 10 and len(valbz_trade_price_list) >= 10:
        vale: List[int] = vale_trade_price_list[-10:]
        valbz: List[int] = valbz_trade_price_list[-10:]
        result: List[Union[bool, float]] = adr_signal(valbz, vale)
        if result:
      
            return [{"type" : Action.ADD, "symbol": Symbol.XLF, "dir" : Direction.BUY, "price": result[1]+1, "size": 10},
                    {"type" : Action.CONVERT, "symbol": Symbol.XLF, "dir" : Direction.SELL, "size": 10},
                    {"type" : Action.ADD, "symbol": Symbol.XLF, "dir" : Direction.SELL, "price": result[2]-1, "size": 10}]
    return []
   
def ema(values: List[float], period: int) -> float:
    """Calculates exponential moving average for a given list of floats and period."""
    values: np.ndarray = np.array(values)
    return pd.DataFrame(values).ewm(span=period, adjust=False).mean().values[-1][-1]

def generate_signals(values: List[float], period: int) -> List[str]:
    """Generates buy and sell signals based on EMA 5 and EMA 13 crossover.

    Args:
        values (List[float]): A list of float values.
        period (int): The period or number of periods to consider for EMA calculation.

    Returns:
        List[str]: A list of signals indicating buy ('BUY'), sell ('SELL'), or no action ('HOLD').

    Example:
        >>> values = [100, 102, 101, 105, 104, 108, 107, 109]
        >>> signals = generate_signals(values, 5)
        >>> print(signals)
        ['HOLD', 'HOLD', 'HOLD', 'BUY', 'HOLD', 'BUY', 'HOLD', 'SELL']
    """
    ema5 = ema(values, 5)
    ema13 = ema(values, 13)

    signals = []
    for i in range(len(values)):
        if i >= 1:
            prev_ema5 = ema(values[:i], 5)
            prev_ema13 = ema(values[:i], 13)
            if prev_ema5 < prev_ema13 and ema5 > ema13:
                signals.append('BUY')
            elif prev_ema5 > prev_ema13 and ema5 < ema13:
                signals.append('SELL')
            else:
                signals.append('HOLD')
        else:
            signals.append('HOLD')

    return signals

