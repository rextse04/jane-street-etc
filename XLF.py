import numpy as np
import pandas as pd

from typing import List, Union
from helper import *
from etc_types import *
from typing import List

def ema_strategy(XLF_trade_info: List[TradeInfo]) -> List[Trade]:
   

    This algorithm makes use of exponential moving averages.

    Args:

    Returns:
    
        List[Trade]: A list of trades to perform. May be empty.

    """
    
    
        XLF_trade_price_list: List[int] = list(map(lambda x: x[0], XLF_trade_info))
        result = generate_signals(XLF_trade_price_list)
        if result=="BUY":
            Net_position+=100
            return [{"type" : Action.ADD, "symbol": Symbol.XLF, "dir" : Direction.BUY, "price":XLF_trade_price_list[-1]  , "size": 100}]
           
        elif result=="SELL":
            Net_position-=100
            return [{"type" : Action.ADD, "symbol": Symbol.XLF, "dir" : Direction.SELL, "price":XLF_trade_price_list[-1], "size": 100}]

                    
    return []
   
def ema(values: List[float], period: int) -> float:
    """Calculates exponential moving average for a given list of floats and period."""
    values: np.ndarray = np.array(values)
    return pd.DataFrame(values).ewm(span=period, adjust=False).mean().values[-1][-1]

def generate_signals(values: List[float]) -> str:
    """Generates buy and sell signals based on EMA 5 and EMA 13 crossover.

    Args:
        values (List[float]): A list of float values.

    Returns:
        str: A signal indicating buy ('BUY'), sell ('SELL'), or no action ('HOLD').

    """
    ema5 = ema(values, 5)
    ema13 = ema(values, 13)

    if len(values) > 1:
        prev_ema5 = ema(values[:-1], 5)
        prev_ema13 = ema(values[:-1], 13)

        if prev_ema5 < prev_ema13 and ema5 > ema13:
            return 'BUY'
        elif prev_ema5 > prev_ema13 and ema5 < ema13:
            return 'SELL'

    return 'HOLD'

