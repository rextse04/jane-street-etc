import numpy as np
import pandas as pd

from typing import List, Union
from helper import *
from etc_types import *

def ema_strategy(vale_trade_info: List[TradeInfo], valbz_trade_info: List[TradeInfo]) -> List[Trade]:
   

    This algorithm makes use of exponential moving averages.

    Args:

      

    Returns:
    
        List[Trade]: A list of trades to perform. May be empty.

    """
   
def ema(values: List[float], period: int) -> float:
    """Calculates exponential moving average for a given list of floats and period."""
    values: np.ndarray = np.array(values)
    return pd.DataFrame(values).ewm(span=period, adjust=False).mean().values[-1][-1]

