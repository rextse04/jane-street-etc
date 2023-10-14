from typing import List
from etc_types import *

def bond__trade_strategy(buy: List[Resting_order], sell: List[Resting_order]) -> List[Trade]:
    """Generates trades based on resting buy and sell orders for BOND
    Args:
        buy (List[Resting_order]): Resting buy orders
        sell (List[Resting_order]): Resting sell orders 
    Returns:
        List[Trade]: List of trades to perform. May be empty.
    """
    trade_orders = []
    for order in buy:
        if order[0] > 1000:
            trade = {
                "type": Action.ADD,
                "symbol": Symbol.BOND,
                "dir": Direction.SELL,
                "price": order[0],
                "size": 1
            }
            trade_orders.append(trade)

    for order in sell:
        if order[0] < 1000:
            trade = {
                "type": Action.ADD,
                "symbol": Symbol.BOND,
                "dir": Direction.BUY,
                "price": order[0],
                "size": 1
            }
            trade_orders.append(trade)

    return trades_orders
