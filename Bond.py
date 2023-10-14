from typing import List
from etc_types import *

def bond__trade_strategy(buy: List[Resting_order], sell: List[Resting_order]) -> List[Trade]:
    """Generates trades based on resting buy and sell orders for BOND

    Args:
        buy (List[Resting_order]): Resting buy orders of BOND.
        sell (List[Resting_order]): Resting sell orders of BOND.

    Returns:
        List[Trade]: List of trades to perform. May be empty.

    Example:
        >>> bond_strategy([[1001, 4], [999, 8]], [[998, 5], [1002, 7]])
        [{"type": "add", "symbol": "BOND", "dir": "SELL", "price": 1001, "size": 4},
        {"type": "add", "symbol": "BOND", "dir": "BUY", "price": 998, "size": 5}]
    """
    trade_orders = []
    hello_message={"type": "hello", "team": "MARV"}

    for order in buy:
        if order[0] > 1000:
            trade = {
                "type": Action.ADD,
                "symbol": Symbol.BOND,
                "dir": Direction.SELL,
                "price": order[0],
                "size": order[1]
            }
            trade_orders.append(trade)

    for order in sell:
        if order[0] < 1000:
            trade = {
                "type": Action.ADD,
                "symbol": Symbol.BOND,
                "dir": Direction.BUY,
                "price": order[0],
                "size": order[1]
            }
            trade_orders.append(trade)

    return hello_message+trades_orders
